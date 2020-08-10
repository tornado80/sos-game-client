from PySide2.QtWidgets import QWidget, QMessageBox, QLabel
from PySide2.QtCore import Signal, Qt
import socket
from sos.gui.game_screen_ui import Ui_GameScreen
from sos.utils.protocol import Packet

class Cell(QLabel):
    def __init__(self):
        super().__init__()
        self.row = None
        self.column = None
        self.state = None # 0 for free, 1 for O, 2 for S
        self.background_color = None # silver for free, red for used S or O (in a triple SOS), blue for S or O
        self.set_to_free()
        self.setAlignment(Qt.AlignCenter)

    def set_style(self):
        self.setStyleSheet(f"background-color:{self.background_color};color:white;font-size:48pt;font-weight:bold;")

    def set_to_used(self):
        self.background_color = "red"
        self.set_style()

    def set_to_free(self):
        self.state = 0
        self.setText("")
        self.background_color = "silver"
        self.set_style()

    def set_to_o(self):
        self.state = 1
        self.setText("O")
        self.background_color = "blue"
        self.set_style()

    def set_to_s(self):
        self.state = 2
        self.setText("S")
        self.background_color = "blue"
        self.set_style()        

class GameScreen(QWidget, Ui_GameScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
