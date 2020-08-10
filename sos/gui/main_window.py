from PySide2.QtWidgets import QMainWindow
from sos.gui.main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginScreen.main_window = self
        self.signupScreen.main_window = self
        self.menuScreen.main_window = self
        self.accountScreen.main_window = self
        self.gameScreen.main_window = self
        self.loginScreen.loginSuccessful.connect(self.navigate_to_menu_screen)
        self.signupScreen.signupSuccessful.connect(self.navigate_to_login_screen)
        self.user_session_id = None
    
    def navigate_to_signup_screen(self):
        self.set_server_address_readonly(False)
        self.signupScreen.refresh_form()
        self.stackedWidget.setCurrentWidget(self.signupScreen)

    def navigate_to_account_screen(self):
        self.stackedWidget.setCurrentWidget(self.accountScreen)
        self.accountScreen.refresh_form()

    def navigate_to_game_screen(self, *args):
        self.stackedWidget.setCurrentWidget(self.gameScreen)
        self.gameScreen.setup_game_screen(*args)

    def navigate_to_login_screen(self):
        self.user_session_id = None
        self.loginScreen.refresh_form()
        self.set_server_address_readonly(False)
        self.stackedWidget.setCurrentWidget(self.loginScreen)

    def navigate_to_menu_screen(self, session_id):
        self.user_session_id = session_id
        self.set_server_address_readonly(True)
        self.stackedWidget.setCurrentWidget(self.menuScreen)

    def set_server_address_readonly(self, readonly):
        self.serverIP1SpinBox.setReadOnly(readonly)
        self.serverIP2SpinBox.setReadOnly(readonly)
        self.serverIP3SpinBox.setReadOnly(readonly)
        self.serverIP4SpinBox.setReadOnly(readonly)
        self.serverPortSpinBox.setReadOnly(readonly)

    def get_server_address(self):
        part1 = str(self.serverIP1SpinBox.value())
        part2 = str(self.serverIP2SpinBox.value())
        part3 = str(self.serverIP3SpinBox.value())
        part4 = str(self.serverIP4SpinBox.value())
        port = self.serverPortSpinBox.value()
        host = f"{part1}.{part2}.{part3}.{part4}"
        return host, port

    def closeEvent(self, event):
        if self.user_session_id:
            self.menuScreen.handle_signout()
        event.accept()