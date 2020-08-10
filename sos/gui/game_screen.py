from PySide2.QtWidgets import QWidget, QMessageBox, QLabel
from PySide2.QtCore import Signal, Qt
import socket
from sos.gui.game_screen_ui import Ui_GameScreen
from sos.utils.protocol import Packet

class Cell(QLabel):
    def __init__(self, row=None, column=None):
        super().__init__()
        self.row = row
        self.column = column
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

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("now free")
            self.set_to_free()
        elif event.button() == Qt.MouseButton.RightButton:
            print("now used")
            self.set_to_used()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("now S")
            self.set_to_s()
        elif event.button() == Qt.MouseButton.RightButton:
            print("now O")
            self.set_to_o()

class GameScreen(QWidget, Ui_GameScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.handle_back)

    def handle_back(self):
        self.main_window.navigate_to_menu_screen(self.main_window.user_session_id)

    def setup_game_screen(self, sock, game_id, creator_username, board_size, player_count):
        self.game_id = game_id
        self.sock = sock
        self.creator_username = creator_username
        self.board_size = board_size
        self.player_count = player_count
        self.gameIDLabel.setText(str(game_id))
        self.creatorUsernameLabel.setText(creator_username)
        self.boardSizeLabel.setText(str(board_size))
        self.playersCountLabel.setText(str(player_count))
        for i in range(board_size):
            for j in range(board_size):
                self.gameBoard.addWidget(Cell(i + 1, j + 1), i, j)