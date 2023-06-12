from threading import Thread

import pyqtgraph as pg

from numpy import log10
from scipy.fft import fft, fftshift

from PyQt6 import QtCore
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QWidget, QGridLayout

from SDRManager import SDRManager

class MainWidget(QWidget):
    
    def __init__(self) -> None:
        QWidget.__init__(self)
        
        self.plot_widget = None
        self.layout = None
        self.grid_layout = None
        self.data = None
        self.fft_data = None
        self.magnitude_data = None
        self.iir_data = None
        self.final_data = None
        self.data_capture_thread = None
        self.sdr = None
        self.data_capture_flag = None
        self.plot_refresh_thread = None
        self.plot_refresh_rate = None
        self.plot_line = None
        self.rtl_devices_box = None
        
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        
        self.sdr = SDRManager()
        self.sdr.createSDRObject()
        
        self.data_capture_flag = True
        self.data_capture_thread = Thread(target=self.fetchSDRData, args=())
        self.data_capture_thread.setDaemon(True)
        self.data_capture_thread.start()
        
        self.plot_refresh_rate = 33 # ms
        
        self.data = list()
        self.fft_data = list()
        self.magnitude_data = [None] * 1024
        self.iir_data = list()
        
        self.plot_refresh_thread = QTimer()
        self.plot_refresh_thread.timeout.connect(self.updatePlot)
        self.plot_refresh_thread.start(self.plot_refresh_rate)
        
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setMouseEnabled(x=False, y=False)
        
        self.plot_line = self.plot_widget.plot([0])

        self.grid_layout.addWidget(self.plot_widget, 0, 0, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        self.sdr.setSDRSettings(2.56e6, 100e6, 0, 15)
        
        
    def fetchSDRData(self):
        """Fetch the SDR data from the device .
        """
        while(self.data_capture_flag):
            self.data = self.sdr.getSamples(1024)
            self.performFFT()
            self.toMagnitude()
            self.applyIIRFilter(.9975)
            
    def applyIIRFilter(self, alpha: float):
        if len(self.iir_data) == 0:
            self.iir_data = self.magnitude_data
        else: 
            oma = 1 - alpha
            tiir = [None] * 1024
            for i in range(len(self.fft_data)):
                tiir[i] = (alpha * self.iir_data[i])  + (oma * self.magnitude_data[i])
            self.iir_data = tiir
    def toMagnitude(self):
        for i in range(len(self.fft_data)):
            curData = self.fft_data[i]
            isqr = curData.real ** 2
            qsqr =  curData.imag ** 2
            self.magnitude_data[i] = log10(isqr + qsqr)
    
    def performFFT(self):
        self.fft_data = fftshift(fft(self.data))
        fft_data_len = len(self.fft_data)
        self.fft_data[int(fft_data_len / 2)] = self.fft_data[int((fft_data_len / 2)) - 1]
       
            
    def updatePlot(self):
        """Updates the plot widget .
        """
        if self.iir_data is not None:
            self.plot_line.setData(self.iir_data)

        
        
        
        