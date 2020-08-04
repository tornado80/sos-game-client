from PySide2.QtWidgets import QApplication
import sys
from sos.gui.main_window import MainWindow

class SOSGameClientApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_window = MainWindow()
        self.main_window.show()

app = SOSGameClientApp(sys.argv)
app.exec_()
