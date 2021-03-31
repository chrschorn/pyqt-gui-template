import time

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from .progress import long_operation
from .ui.appgui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.app = app
        self.btn_thebutton.pressed.connect(self.button_press)

    def button_press(self):
        text = self.operation()
        QMessageBox.information(self, "Message Box", text)

    @long_operation("Calculation")
    def operation(self):
        return self.app.calculation(3)
