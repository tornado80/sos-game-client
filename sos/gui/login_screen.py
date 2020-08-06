from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Signal
import socket
from sos.gui.login_screen_ui import Ui_LoginScreen
from sos.utils.protocol import Packet

class LoginScreen(QWidget, Ui_LoginScreen):
    loginSuccessful = Signal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.handle_login)
        self.signupButton.clicked.connect(self.handle_signup)

    def handle_signup(self):
        self.main_window.navigate_to_signup_screen()
        self.refresh_form()

    def refresh_form(self):
        self.usernameLineEdit.setText("")
        self.passwordLineEdit.setText("")

    def handle_login(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        if username == "" or password == "":
            QMessageBox.warning(self, "Error", "Username or password is empty.")
            return
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.main_window.get_server_address())
                request = Packet()
                request["commad"] = "login_request"
                request["data"] = {
                    "username" : username,
                    "password" : password
                }
                request.send(sock)
                response = Packet.recv(sock)
                if response["command"] == "login_response":
                    if "session_id" in response["data"]:
                        self.loginSuccessful.emit(response["data"]["session_id"])
                        self.refresh_form()
                    elif "error" in response["data"]:
                        QMessageBox.critical(self, "Error", response["data"]["error"])
                    else:
                        QMessageBox.critical(self, "Error", "Connection was interrupted. Please try again later.")
        except Exception as error:
            QMessageBox.critical(self, "Error", str(error))