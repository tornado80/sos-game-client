from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Signal
import socket
from sos.gui.signup_screen_ui import Ui_SignUpScreen
from sos.utils.protocol import Packet

class SignUpScreen(QWidget, Ui_SignUpScreen):
    signupSuccessful = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.handle_back)
        self.signupButton.clicked.connect(self.handle_signup)

    def handle_back(self):
        self.main_window.navigate_to_login_screen()
        self.refresh_form()

    def refresh_form(self):
        self.usernameLineEdit.setText("")
        self.passwordLineEdit.setText("")
        self.firstnameLineEdit.setText("")
        self.lastnameLineEdit.setText("")

    def handle_signup(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        firstname = self.firstnameLineEdit.text()
        lastname = self.lastnameLineEdit.text()
        repeat_password = self.repeatPasswordLineEdit.text()
        if username == "" or firstname == "" or lastname == "" or password == "" or repeat_password == "":
            QMessageBox.warning(self, "Error", "All of the fields are necessary.")
            return
        if password != repeat_password:
            QMessageBox.warning(self, "Error", "Password and confirmation password do not match.")
            return
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.main_window.get_server_address())
                request = Packet()
                request["commad"] = "signup_request"
                request["data"] = {
                    "username" : username,
                    "password" : password,
                    "firstname" : firstname,
                    "lastname" : lastname
                }
                request.send(sock)
                response = Packet.recv(sock)
                if response["command"] == "signup_response":
                    if "ok" in response["data"]:
                        QMessageBox.information(self, "Sign Up Successful", 
                        "Your account was successfully created. You will be navigated to login page to dive into your account.")
                        self.signupSuccessful.emit()
                        self.refresh_form()
                    elif "error" in response["data"]:
                        QMessageBox.critical(self, "Error", response["data"]["error"])
                    else:
                        QMessageBox.critical(self, "Error", "Connection was interrupted. Please try again later.")
        except Exception as error:
            QMessageBox.critical(self, "Error", str(error))
            