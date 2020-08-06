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
                    if "error" in response["data"]:
                        QMessageBox.critical(self, "Error", response["data"]["error"])
                    else:
                        QMessageBox.critical(self, "Error", "Connection was interrupted. Please try again later.")
        except Exception as error:
            QMessageBox.critical(self, "Error", str(error))

    def handle_my_account(self):
        print("my account clicked")