import PyQt6
from PyQt6.QtWidgets import QMainWindow, QApplication
from unt import Ui_new_two_window
import sys


class NewWindow(QMainWindow, Ui_new_two_window):
    def __init__(self):
        super(NewWindow, self).__init__()
        self.setupUi(self)
        self.push_button.clicked.connect(self.open_new_window)
        self.push_button_2.clicked.connect(self.open_else_window)

    def open_new_window(self):
        self.close()
        second_window.show()

    def open_else_window(self):
        self.close()
        third_win.show()


app = QApplication(sys.argv)
new_two_window = NewWindow()

new_two_window.show()
app.exec()
