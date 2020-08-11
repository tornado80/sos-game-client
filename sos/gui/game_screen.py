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
        self.state = 0 # 0 for free, 1 for O, 2 for S, 3 for used O, 4 for used S
        self.background_color = "silver" # silver for free, red for used S or O (in a triple SOS), blue for S or O
        self.set_to_free()
        self.setAlignment(Qt.AlignCenter)

    def set_style(self):
        self.setStyleSheet(f"background-color:{self.background_color};color:white;font-size:48pt;font-weight:bold;")

    def set_by_state(self, state):
        self.state = state
        if self.state == 0:
            self.set_to_free()
        elif self.state == 1:
            self.set_to_o()
        elif self.state == 2:
            self.set_to_s()
        elif self.state == 3:
            self.set_to_used_o()
        elif self.state == 4:
            self.set_to_used_s()

    def set_to_used_s(self):
        self.state = 4
        self.setText("S")
        self.background_color = "red"
        self.set_style()

    def set_to_used_o(self):
        self.state = 3
        self.setText("O")
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
    newEvent = Signal(dict)
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        while True:
            response = Packet.recv(self.sock)
            self.newEvent.emit(response)
            if response["command"] == "game_runner_abort":
                self.sock.close()
                return

class GameScreen(QWidget, Ui_GameScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.handle_back)
        self.leaderBoardRows = []

    def handle_back(self):
        if QMessageBox.question(self, 
            "User Consent", 
            "Do you really want to quit the game? If all the players hit back, game is automatically deleted and you may lose points.", 
            QMessageBox.No, QMessageBox.Yes) == QMessageBox.No:
            return        
        request = Packet()
        request["command"] = "game_runner_disconnect"
        request.send(self.sock)
        self.main_window.navigate_to_menu_screen(self.main_window.user_session_id)

    def setup_game_listener(self):
        self.listener = GameServerListener(self.sock)
        self.listener.newEvent.connect(self.handle_new_event)
        self.listener.start()

    def handle_new_event(self, response):
        if response["command"] == "game_runner_players_status":
            self.clear_leader_board()
            if self.noPlayerJoinedLabel.isVisible():
                self.noPlayerJoinedLabel.setVisible(False)
            players = response["data"]["players"]
            for player_username, player_score in players.items():
                row = self.leaderBoard.rowCount()
                usernameLabel = QLabel(player_username)
                scoreLabel = QLabel(player_score)
                usernameLabel.setAlignment(Qt.AlignCenter)
                scoreLabel.setAlignment(Qt.AlignCenter)
                self.leaderBoard.addWidget(usernameLabel, row, 0)
                self.leaderBoard.addWidget(scoreLabel, row, 1)
                self.leaderBoardRows.append([usernameLabel, scoreLabel])

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

    def clear_leader_board(self):
        for row in self.leaderBoardRows:
            self.leaderBoard.removeWidget(row[0])
            row[0].setParent(None)
            self.leaderBoard.removeWidget(row[1])
            row[1].setParent(None)
        self.leaderBoardRows.clear()

    def setup_leader_board(self):
        self.noPlayerJoinedLabel.setVisible(True)
        self.clear_leader_board()
        self.gameIDLabel.setText(str(self.game_id))
        self.creatorUsernameLabel.setText(self.creator_username)
        self.boardSizeLabel.setText(str(self.board_size))
        self.playersCountLabel.setText(str(self.player_count))

    def setup_game_screen(self, sock, game_id, creator_username, board_size, player_count):
        self.game_id = game_id
        self.sock = sock
        self.creator_username = creator_username
        self.board_size = board_size
        self.player_count = player_count
        self.setup_leader_board()
        self.setup_game_board()
        self.setup_game_listener()