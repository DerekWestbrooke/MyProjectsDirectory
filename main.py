import sys

from PyQt5.QtWidgets import QApplication
from calculator import Calculator

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())