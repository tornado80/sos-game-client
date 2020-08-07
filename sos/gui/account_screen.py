from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Signal, QDateTime, QDate, QTime
import socket
import datetime
from sos.gui.account_screen_ui import Ui_AccountScreen
from sos.utils.protocol import Packet

class AccountScreen(QWidget, Ui_AccountScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.handle_back)
        self.updateAccountButton.clicked.connect(self.handle_update_account)
        self.removeAccountButton.clicked.connect(self.handle_remove_account)
    
    def handle_back(self):
        self.main_window.navigate_to_menu_screen(self.main_window.user_session_id)
    
    def handle_remove_account(self):
        print("Remove account")
    
    def handle_update_account(self):
        print("Update account")

    def refresh_form(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.main_window.get_server_address())
                request = Packet()
                request["command"] = "get_account_request"
                request["data"] = {
                    "session_id" : self.main_window.user_session_id
                }
                request.send(sock)
                response = Packet.recv(sock)
                if response["command"] == "get_account_response":
                    if "ok" in response["data"]:
                        data = response["data"]
                        self.usernameLineEdit.setText(data["username"])
                        self.firstnameLineEdit.setText(data["firstname"])
                        self.lastnameLineEdit.setText(data["lastname"])
                        self.ratingSpinBox.setValue(data["rating"])
                        self.winsSpinBox.setValue(data["wins"])
                        self.gamesSpinBox.setValue(data["games"])
                        joined_dt_obj = datetime.datetime.strptime(data["joined_at"], "%Y-%m-%d %H:%M:%S.%f")
                        login_dt_obj = datetime.datetime.strptime(data["last_login"], "%Y-%m-%d %H:%M:%S.%f")
                        self.joinedDateTimeEdit.setDateTime(
                            QDateTime(
                                QDate(
                                    joined_dt_obj.year,
                                    joined_dt_obj.month,
                                    joined_dt_obj.day
                                ), 
                                QTime(
                                    joined_dt_obj.hour,
                                    joined_dt_obj.minute,
                                    joined_dt_obj.second,
                                    int(joined_dt_obj.microsecond/1000)
                                )
                            )
                        )
                        self.lastLoginDateTimeEdit.setDateTime(
                            QDateTime(
                                QDate(
                                    login_dt_obj.year,
                                    login_dt_obj.month,
                                    login_dt_obj.day
                                ), 
                                QTime(
                                    login_dt_obj.hour,
                                    login_dt_obj.minute,
                                    login_dt_obj.second,
                                    int(login_dt_obj.microsecond/1000)
                                )
                            )
                        )
                    elif "error" in response["data"]:
                        QMessageBox.critical(self, "Error", response["data"]["error"])
                    else:
                        QMessageBox.critical(self, "Error", "Connection was interrupted. Please try again later.")
        except Exception as error:
            QMessageBox.critical(self, "Error", str(error))
