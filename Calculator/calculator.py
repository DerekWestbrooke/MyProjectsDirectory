import os
import re


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
from static_values import buttons
from asteval import Interpreter

# Creating class Calculator
class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Setting a style for main window
        self.setWindowTitle('Calculator')
        if os.path.exists(os.getcwd() + '/icons/calc.ico'):
            self.setWindowIcon(QIcon(os.getcwd() + '/icons/calc.ico'))
        self.resize(400, 400)

        # Creating LineEdits for input and result
        self.le_result = QtWidgets.QLineEdit()
        self.le_result.setReadOnly(True)
        self.le_input = QtWidgets.QLineEdit()
        self.le_input.setReadOnly(True)

        # Creating GridLayout for buttons
        self.grlo_buttons = QtWidgets.QGridLayout()
        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                if buttons[i][j] is not None:
                    button = QtWidgets.QPushButton(buttons[i][j])
                    button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
                    button.clicked.connect(self.click_the_button)
                    if buttons[i][j] != '=':
                        self.grlo_buttons.addWidget(button, i, j, 1, 1)
                    else:
                        self.grlo_buttons.addWidget(button, i, j, 2, 1)
                    if buttons[i][j] in '0123456789':
                        button.setObjectName('btn_digit')
                    elif buttons[i][j] == '=':
                        button.setObjectName('btn_equal')
                    else:
                        button.setObjectName('btn_operator')

        # Main layout
        self.vlo_main = QtWidgets.QVBoxLayout()
        self.vlo_main.addWidget(self.le_result)
        self.vlo_main.addWidget(self.le_input)
        self.vlo_main.addLayout(self.grlo_buttons)
        self.setLayout(self.vlo_main)

    # Creating a main function to click buttons
    def click_the_button(self, text=None):
        if text is not None:
            button_text = text
        else:
            button = self.sender()
            button_text = button.text()
        funcs_dict = {
            '0123456789(': lambda: self.call_digits_func(button_text),
            'C': self.call_clear_func,
            ',+-*/√%R)': lambda: self.call_operators_func(button_text),
            'x²': lambda: self.call_operators_func(button_text),
            '=': self.call_equal_func,
            'π': self.call_pi_func
        }
        for key in funcs_dict.keys():
            if button_text in key:
                funcs_dict[key]()
                break

    # Creating function to input C
    def call_clear_func(self):
        self.le_input.clear()

    # Creating function to input digits
    def call_digits_func(self, button_text):
        self.le_input.setText(self.le_input.text() + button_text)

    # Creating function to input pi
    def call_pi_func(self):
        if self.le_input.text():
            if self.le_input.text()[-1] != 'π':
                self.le_input.setText(self.le_input.text() + 'π')
            else:
                self.le_input.setText(self.le_input.text()[:-1])
        else:
            self.le_input.setText('π')

    # Creating function to input operators
    def call_operators_func(self, button_text):
        text = self.le_input.text()
        if button_text == 'x²':
            button_text = '²'
        if text:
            if text[-1] in '0123456789)π':
                    self.le_input.setText(text + button_text)
            elif text.endswith(button_text) and button_text == text[-1]:
                self.le_input.setText(text[:-1])
            elif button_text in ',+-*/√%²R)' and button_text != text[-1]:
                self.le_input.setText(text[:-1] + button_text)
        else:
            if button_text in '-√':
                self.le_input.setText(button_text)

    # Creating function to input =
    def call_equal_func(self):
        if self.le_input.text():
            expression = (self.le_input.text()).replace(',', '.')
            expression = re.sub('π', 'pi', expression)
            expression = re.sub('%', '/100', expression)
            expression = re.sub('R', '%', expression)
            expression = re.sub('²', '**2', expression)
            expression = re.sub(r'√(\d+(\.\d+)?|\([^)]+\))', r'sqrt(\1)', expression)
            aeval = Interpreter()
            result = aeval(expression)
            if aeval.error:
                self.le_result.setText('Calculation error!')
                self.le_input.clear()
            else:
                if str(result).endswith('.0'):
                    result = str(result)[:-2]
                else:
                    result = str(result)
                self.le_result.setText(self.le_input.text() + '=' + str(result))
                self.le_input.setText(str(result))

    # Creating function to input symbols physically
    def keyPressEvent(self, event):
        key_text = event.text()
        key = event.key()

        if key_text in '0123456789+-*/.()':
            self.click_the_button(key_text)
        elif key_text == '=' or key == QtCore.Qt.Key.Key_Enter:
            self.click_the_button('=')
        elif key == QtCore.Qt.Key.Key_Delete:
            self.click_the_button('C')
        else:
            super().keyPressEvent(event)


