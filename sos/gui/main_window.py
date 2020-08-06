from PySide2.QtWidgets import QMainWindow
from sos.gui.main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginScreen.main_window = self
        self.signupScreen.main_window = self
        self.loginScreen.loginSuccessful.connect(self.navigate_to_menu_screen)
        self.signupScreen.signupSuccessful.connect(self.navigate_to_login_screen)
    
    def navigate_to_signup_screen(self):
        self.stackedWidget.setCurrentWidget(self.signupScreen)

    def navigate_to_login_screen(self):
        self.stackedWidget.setCurrentWidget(self.loginScreen)

    def navigate_to_menu_screen(self, session_id):
        print("session_id from MainWindow", session_id)

    def get_server_address(self):
        part1 = str(self.serverIP1SpinBox.value())
        part2 = str(self.serverIP2SpinBox.value())
        part3 = str(self.serverIP3SpinBox.value())
        part4 = str(self.serverIP4SpinBox.value())
        port = self.serverPortSpinBox.value()
        host = f"{part1}.{part2}.{part3}.{part4}"
        return host, port
        
