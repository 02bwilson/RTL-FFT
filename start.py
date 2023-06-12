from PyQt6.QtWidgets import QApplication

from RTLFFT import RTLFFT

import sys


def main() -> None:
    args = sys.argv[1:]
    app = QApplication([])
    
    window = RTLFFT(args[0])
    window.show()
    
    app.exec()
    
    
if __name__ == "__main__":
    main()