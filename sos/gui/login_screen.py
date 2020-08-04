from PySide2.QtWidgets import QWidget, QMessageBox
import socket
from sos.gui.login_screen_ui import Ui_LoginScreen
from sos.utils.protocol import Packet

class LoginScreen(QWidget, Ui_LoginScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.handle_login)
        self.signupButton.clicked.connect(self.handle_signup)

    def handle_signup(self):
        print("sign up button clicked")

    def handle_login(self):
        if self.usernameLineEdit.text() == "" or self.passwordLineEdit.text() == "":
            QMessageBox.critical(self, "Error", "Username or password is empty.")
            return
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.parent().get_server_address())
            request = Packet()
            request["commad"] = "login"
            request["data"] = {
                "username" : self.usernameLineEdit.text(),
                "password" : self.passwordLineEdit.text()
            }
            request.send(sock)
            response = Packet.recv(sock)
            print(response)
