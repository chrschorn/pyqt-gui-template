import time

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from .progress import long_operation
from .utils import resource_path
from .ui.appgui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.btn_thebutton.pressed.connect(self.button_press)

    def button_press(self):
        text = self.calculation(3)
        QMessageBox.information(self, "Message Box", text)

    @long_operation("Calculation")
    def calculation(self, sleep):
        print("Start")
        with open(resource_path('example.txt')) as file:
            text = file.read()
        time.sleep(sleep)
        print("End")
        return text
