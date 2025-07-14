import sys
import os

from PyQt5.QtWidgets import QApplication
from calculator import Calculator
from PyQt5.QtCore import QFile, QTextStream


# Creating a function to launch application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    file = QFile(os.getcwd() + '/widget_styles.qss')
    if file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(file)
        qss = stream.readAll()
        app.setStyleSheet(qss)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())