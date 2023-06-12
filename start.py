from PyQt6.QtWidgets import QApplication

from RTLFFT import RTLFFT

import sys


def main() -> None:
    app = QApplication([])
    
    window = RTLFFT()
    window.show()
    
    app.exec()
    
    
if __name__ == "__main__":
    main()