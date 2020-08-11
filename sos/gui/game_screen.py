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
        self.state = 0
        self.setAlignment(Qt.AlignCenter)

    def set_style(self, letter, color):
        self.setText(letter)
        self.setStyleSheet(f"background-color:{color};color:white;font-size:48pt;font-weight:bold;")

    def mousePressEvent(self, event):
        if self.state == 0:
            if event.button() == Qt.MouseButton.LeftButton:
                self.sWanted.emit(self.row, self.column)
            elif event.button() == Qt.MouseButton.RightButton:
                self.oWanted.emit(self.row, self.column)

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
        self.my_turn = False

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
                color = response["data"]["colors"][player_username]
                usernameLabel = QLabel(player_username)
                scoreLabel = QLabel(player_score)
                usernameLabel.setStyleSheet(f"color:{color};")
                usernameLabel.setAlignment(Qt.AlignCenter)
                scoreLabel.setAlignment(Qt.AlignCenter)
                self.leaderBoard.addWidget(usernameLabel, row, 0)
                self.leaderBoard.addWidget(scoreLabel, row, 1)
                self.leaderBoardRows.append([usernameLabel, scoreLabel])
        elif response["command"] == "game_runner_board_status":
            for i in range(self.board_size):
                for j in range(self.board_size):
                    self.board[i][j].state = 0 if response["data"]["board"][i][j][1] == "" else 1
                    self.board[i][j].set_style(response["data"]["board"][i][j][1], response["data"]["board"][i][j][0])
        elif response["command"] == "game_runner_your_turn":
            self.my_turn = True
            self.yourTurnLabel.setVisible(True)

    def handle_s_wanted(self, row, column):
        if self.my_turn:
            self.board[row][column].set_style("S", self.color)
            self.board[row][column].state = 1
            self.my_turn = False
            self.yourTurnLabel.setVisible(False)
            request = Packet()
            request["command"] = "game_runner_my_turn"
            request["data"] = {
                "row" : row,
                "column" : column,
                "letter" : "S"
            }
            request.send(self.sock)

    def handle_o_wanted(self, row, column):
        if self.my_turn:
            self.board[row][column].set_style("O", self.color)
            self.board[row][column].state = 1
            self.my_turn = False
            self.yourTurnLabel.setVisible(False)
            request = Packet()
            request["command"] = "game_runner_my_turn"
            request["data"] = {
                "row" : row,
                "column" : column,
                "letter" : "O"
            }
            request.send(self.sock)            

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
        self.yourTurnLabel.setVisible(False)
        self.clear_leader_board()
        self.gameIDLabel.setText(str(self.game_id))
        self.creatorUsernameLabel.setText(self.creator_username)
        self.boardSizeLabel.setText(str(self.board_size))
        self.playersCountLabel.setText(str(self.player_count))

    def setup_game_screen(self, sock, game_id, creator_username, board_size, player_count, color):
        self.game_id = game_id
        self.sock = sock
        self.color = color
        self.creator_username = creator_username
        self.board_size = board_size
        self.player_count = player_count
        self.setup_leader_board()
        self.setup_game_board()
        self.setup_game_listener()