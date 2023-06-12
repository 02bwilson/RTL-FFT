from PyQt6.QtWidgets import QMainWindow

from RTLFFTWidget import MainWidget

class RTLFFT(QMainWindow): 
    
    _VERSION = "1.0.0"
    
    def __init__(self, center_freq: float) -> None:
        QMainWindow.__init__(self)
        
        self.setWindowTitle("RTLFFT v%s" % self._VERSION)
        
        self.widget = MainWidget(center_freq)
        
        self.setCentralWidget(self.widget)
        
        