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
        self.changeUsernameButton.clicked.connect(self.handle_change_username)
        self.changePasswordButton.clicked.connect(self.handle_change_password)
        self.removeAccountButton.clicked.connect(self.handle_remove_account)
    
    def handle_back(self):
        self.main_window.navigate_to_menu_screen(self.main_window.user_session_id)
    
    def handle_change_password(self):
        current_password = self.currentPasswordLineEdit.text()
        new_password = self.newPasswordLineEdit.text()
        repeat_new_password = self.repeatPasswordLineEdit.text()
        if new_password != repeat_new_password:
            QMessageBox.critical(self, "Error", "Given passwords do not match.")
            return
        if new_password == "":
            QMessageBox.critical(self, "Error", "Password should not be empty.")
            return            
        if current_password == "":
            QMessageBox.critical(self, "Error", "You should key in current password to complete the operation.")          
            return
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.main_window.get_server_address())
                request = Packet()
                request["command"] = "edit_password_request"
                request["data"] = {
                    "session_id" : self.main_window.user_session_id,
                    "new_password" : new_password,
                    "current_password" : current_password
                }
                request.send(sock)
                response = Packet.recv(sock)
                if response["command"] == "edit_password_response":
                    if "ok" in response["data"]:
                        QMessageBox.information(self, "Information", "Your account password was successfully updated. You will be navigated to login screen to enter again.")
                        self.main_window.navigate_to_login_screen()
                    elif "error" in response["data"]:
                        QMessageBox.critical(self, "Error", response["data"]["error"])
                    else:
                        QMessageBox.critical(self, "Error", "Connection was interrupted. Please try again later.")
        except Exception as error:
            QMessageBox.critical(self, "Error", str(error))

    def handle_change_username(self):
        current_password = self.currentPasswordLineEdit.text()
        username = self.usernameLineEdit.text()
        if username == "":
            QMessageBox.critical(self, "Error", "Username should not be empty.")
            return            
        if current_password == "":
            QMessageBox.critical(self, "Error", "You should key in current password to complete the operation.")          
            return
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.main_window.get_server_address())
                request = Packet()
                request["command"] = "edit_username_request"
                request["data"] = {
                    "session_id" : self.main_window.user_session_id,
                    "username" : username,
                    "current_password" : current_password
                }
                request.send(sock)
                response = Packet.recv(sock)
                if response["command"] == "edit_username_response":
                    if "ok" in response["data"]:
                        QMessageBox.information(self, "Information", "Your account username was successfully updated. You will be navigated to login screen to enter again.")
                        self.main_window.navigate_to_login_screen()
                    elif "error" in response["data"]:
                        QMessageBox.critical(self, "Error", response["data"]["error"])
                    else:
                        QMessageBox.critical(self, "Error", "Connection was interrupted. Please try again later.")
        except Exception as error:
            QMessageBox.critical(self, "Error", str(error))

    def handle_remove_account(self):
        current_password = self.currentPasswordLineEdit.text()
        if current_password == "":
            QMessageBox.critical(self, "Error", "You should key in current password to complete the operation.")
            return
        if QMessageBox.question(self, 
            "User Consent", 
            "Do you really want to delete your account? This action couldn't be undone, and all your game data, profile, username, etc. will be deleted permanently.", 
            QMessageBox.No, QMessageBox.Yes) == QMessageBox.No:
            return             
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.main_window.get_server_address())
                request = Packet()
                request["command"] = "remove_account_request"
                request["data"] = {
                    "session_id" : self.main_window.user_session_id,
                    "current_password" : current_password
                }
                request.send(sock)
                response = Packet.recv(sock)
                if response["command"] == "remove_account_response":
                    if "ok" in response["data"]:
                        QMessageBox.information(self, "Information", "Your account was successfully deleted. You will be navigated to login screen.")
                        self.main_window.navigate_to_login_screen()
                    elif "error" in response["data"]:
                        QMessageBox.critical(self, "Error", response["data"]["error"])
                    else:
                        QMessageBox.critical(self, "Error", "Connection was interrupted. Please try again later.")
        except Exception as error:
            QMessageBox.critical(self, "Error", str(error))
    
    def handle_update_account(self):
        current_password = self.currentPasswordLineEdit.text()
        firstname = self.firstnameLineEdit.text()
        lastname = self.lastnameLineEdit.text()
        if firstname == "" or lastname == "":
            QMessageBox.critical(self, "Error", "First name and last name should not be empty.")
            return
        if current_password == "":
            QMessageBox.critical(self, "Error", "You should key in current password to complete the operation.")
            return
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.main_window.get_server_address())
                request = Packet()
                request["command"] = "edit_profile_request"
                request["data"] = {
                    "session_id" : self.main_window.user_session_id,
                    "current_password" : current_password,
                    "first_name" : firstname,
                    "last_name" : lastname
                }
                request.send(sock)
                response = Packet.recv(sock)
                if response["command"] == "edit_profile_response":
                    if "ok" in response["data"]:
                        QMessageBox.information(self, "Information", "Your profile was successfully updated.")
                        self.refresh_form()
                    elif "error" in response["data"]:
                        QMessageBox.critical(self, "Error", response["data"]["error"])
                    else:
                        QMessageBox.critical(self, "Error", "Connection was interrupted. Please try again later.")
        except Exception as error:
            QMessageBox.critical(self, "Error", str(error))

    def refresh_form(self):
        self.usernameLineEdit.setText("")
        self.firstnameLineEdit.setText("")
        self.lastnameLineEdit.setText("")
        self.currentPasswordLineEdit.setText("")
        self.newPasswordLineEdit.setText("")
        self.repeatPasswordLineEdit.setText("")
        self.ratingSpinBox.setValue(0)
        self.winsSpinBox.setValue(0)
        self.gamesSpinBox.setValue(0)        
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
