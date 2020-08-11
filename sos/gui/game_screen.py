from PySide2.QtWidgets import QWidget, QMessageBox, QLabel
from PySide2.QtCore import Signal, Qt, QThread
import socket
from sos.gui.game_screen_ui import Ui_GameScreen
from sos.utils.protocol import Packet

class Cell(QLabel):
    oWanted = Signal(int, int)
    sWanted = Signal(int, int)
    def __init__(self, row=None, column=None):
        super().__init__()
        self.row = row
        self.column = column
        self.state = 0 # 0 for free, 1 for O, 2 for S
        self.background_color = "silver" # silver for free, red for used S or O (in a triple SOS), blue for S or O
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

    def mousePressEvent(self, event):
        if self.state == 0:
            if event.button() == Qt.MouseButton.LeftButton:
                self.sWanted.emit(self.row, self.column)
                self.set_to_s()
            elif event.button() == Qt.MouseButton.RightButton:
                self.oWanted.emit(self.row, self.column)
                self.set_to_o()

class GameServerListener(QThread):
    newMessage = Signal(dict)
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        while True:
            response = Packet.recv(self.sock)
            self.newMessage.emit(response)
            if response["command"] == "game_runner_abort":
                self.sock.close()
                return

class GameScreen(QWidget, Ui_GameScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.handle_back)
        self._leader_board_players = {}

    def handle_back(self):
        request = Packet()
        request["command"] = "game_runner_disconnect"
        request.send(self.sock)
        self.main_window.navigate_to_menu_screen(self.main_window.user_session_id)

    def setup_game_listener(self):
        self.listener = GameServerListener(self.sock)
        self.listener.newMessage.connect(self.handle_new_message)
        self.listener.start()

    def handle_new_message(self, response):
        if response["command"] == "game_runner_new_player_connected":
            if self.noPlayerJoinedLabel.isVisible():
                self.noPlayerJoinedLabel.setVisible(False)
            new_player = response["data"]["player"]
            new_player_account_id = new_player[0]
            new_player_username = new_player[1]
            new_player_score = new_player[2]
            usernameLabel = QLabel(new_player_username)
            scoreLabel = QLabel(str(new_player_score))
            if new_player_account_id in self._leader_board_players:
                row = self._leader_board_players[new_player_account_id][0]
            else:
                row = self.leaderBoard.rowCount()
            self._leader_board_players[new_player_account_id] = [row, usernameLabel, scoreLabel]
            self.leaderBoard.addWidget(usernameLabel, row, 0)
            self.leaderBoard.addWidget(scoreLabel, row, 1)

    def handle_s_wanted(self, row, column):
        print("s wanted")

    def handle_o_wanted(self, row, column):
        print("o wanted")

    def setup_game_board(self):
        self.board = []
        for i in range(self.board_size):
            self.board.append([])
            for j in range(self.board_size):
                cell = Cell(i, j)
                cell.sWanted.connect(self.handle_s_wanted)
                cell.oWanted.connect(self.handle_o_wanted)
                self.board[i].append(cell)
                self.gameBoard.addWidget(cell, i, j)

    def setup_leader_board(self):
        self.noPlayerJoinedLabel.setVisible(True)
        self.gameIDLabel.setText(str(self.game_id))
        self.creatorUsernameLabel.setText(self.creator_username)
        self.boardSizeLabel.setText(str(self.board_size))
        self.playersCountLabel.setText(str(self.player_count))
        for player_row in self._leader_board_players.values():
            self.leaderBoard.removeWidget(player_row[1])
            self.leaderBoard.removeWidget(player_row[2])

    def setup_game_screen(self, sock, game_id, creator_username, board_size, player_count):
        self.game_id = game_id
        self.sock = sock
        self.creator_username = creator_username
        self.board_size = board_size
        self.player_count = player_count
        self.setup_leader_board()
        self.setup_game_board()
        self.setup_game_listener()