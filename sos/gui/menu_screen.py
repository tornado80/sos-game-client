from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Signal
import socket
from sos.gui.menu_screen_ui import Ui_MenuScreen
from sos.utils.protocol import Packet

class MenuScreen(QWidget, Ui_MenuScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signoutButton.clicked.connect(self.handle_signout)
        self.myAccountButton.clicked.connect(self.handle_my_account)
        self.createGameButton.clicked.connect(self.handle_new_game)
        self.joinGameButton.clicked.connect(self.handle_join_game)

    def handle_join_game(self):
        pass

    def handle_new_game(self):
        board_size = self.boardSizeSpinBox.value()
        player_count = self.playerCountSpinBox.value()
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.main_window.get_server_address())
                request = Packet()
                request["command"] = "new_game_request"
                request["data"] = {
                    "session_id" : self.main_window.user_session_id,
                    "board_size" : board_size,
                    "player_count" : player_count,
                    "is_public" : self.publicRadioButton.isChecked()
                }
                request.send(sock)
                response = Packet.recv(sock)
                if response["command"] == "new_game_response":
                    if "game_id" in response["data"]:
                        self.main_window.navigate_to_game_screen(sock, response["data"]["game_id"], response["data"]["creator_username"], board_size, player_count)
                    elif "error" in response["data"]:
                        QMessageBox.critical(self, "Error", response["data"]["error"])
                    else:
                        QMessageBox.critical(self, "Error", "Connection was interrupted. Please try again later.")
        except Exception as error:
            QMessageBox.critical(self, "Error", str(error))
    
    def handle_my_account(self):
        self.main_window.navigate_to_account_screen()

    def handle_signout(self):
        session_id = self.main_window.user_session_id
        self.main_window.navigate_to_login_screen()
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.main_window.get_server_address())
                request = Packet()
                request["command"] = "signout_request"
                request["data"] = {
                    "session_id" : session_id
                }
                request.send(sock)
                response = Packet.recv(sock)
                if response["command"] == "signout_response":
                    if "ok" in response["data"]:
                        pass
                        #QMessageBox.information(self, "Information", "You were signed out of system.")
                    elif "error" in response["data"]:
                        QMessageBox.critical(self, "Error", response["data"]["error"])
                    else:
                        QMessageBox.critical(self, "Error", "Connection was interrupted. Please try again later.")
        except Exception as error:
            QMessageBox.critical(self, "Error", str(error))
