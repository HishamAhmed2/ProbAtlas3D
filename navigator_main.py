import sys
from PyQt6 import QtWidgets
from gui import STRviewerUI

# Running the GUI
def main():
    qapp = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)
    window = STRviewerUI()
    window.show()
    qapp.exec()

if __name__ == "__main__":
    main()
