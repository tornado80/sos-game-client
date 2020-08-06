from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Signal
import socket
from sos.gui.account_screen_ui import Ui_AccountScreen
from sos.utils.protocol import Packet

class AccountScreen(QWidget, Ui_AccountScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)