import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
from static_values import buttons


class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon(os.getcwd() + '/icons/calc.ico'))
        self.setMinimumSize(self.size())

        self.le_result = QtWidgets.QLineEdit()

        self.le_input = QtWidgets.QLineEdit()

        self.grlo_buttons = QtWidgets.QGridLayout()
        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                if buttons[i][j] is not None:
                    button = QtWidgets.QPushButton(buttons[i][j])
                    button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                    if buttons[i][j] != '=':
                        self.grlo_buttons.addWidget(button, i, j, 1, 1)
                    else:
                        self.grlo_buttons.addWidget(button, i, j, 2, 1)

        self.vlo_main = QtWidgets.QVBoxLayout()
        self.vlo_main.addWidget(self.le_result)
        self.vlo_main.addWidget(self.le_input)
        self.vlo_main.addLayout(self.grlo_buttons)

        self.setLayout(self.vlo_main)