from PyQt6.QtWidgets import QMainWindow

from RTLFFTWidget import MainWidget

class RTLFFT(QMainWindow): 
    
    _VERSION = "1.0.0"
    
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        
        self.setWindowTitle("RTLFFT v%s" % self._VERSION)
        
        self.widget = MainWidget()
        
        self.setCentralWidget(self.widget)
        
        