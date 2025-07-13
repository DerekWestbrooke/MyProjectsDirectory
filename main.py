import sys

from calculator import Calculator
from PyQt5 import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())