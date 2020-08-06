# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from sos.gui.login_screen import LoginScreen
from sos.gui.signup_screen import SignUpScreen


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.loginScreen = LoginScreen()
        self.loginScreen.setObjectName(u"loginScreen")
        self.stackedWidget.addWidget(self.loginScreen)
        self.signupScreen = SignUpScreen()
        self.signupScreen.setObjectName(u"signupScreen")
        self.stackedWidget.addWidget(self.signupScreen)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.serverIP1SpinBox = QSpinBox(self.centralwidget)
        self.serverIP1SpinBox.setObjectName(u"serverIP1SpinBox")
        self.serverIP1SpinBox.setFrame(False)
        self.serverIP1SpinBox.setAlignment(Qt.AlignCenter)
        self.serverIP1SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.serverIP1SpinBox.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.serverIP1SpinBox)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.serverIP2SpinBox = QSpinBox(self.centralwidget)
        self.serverIP2SpinBox.setObjectName(u"serverIP2SpinBox")
        self.serverIP2SpinBox.setFrame(False)
        self.serverIP2SpinBox.setAlignment(Qt.AlignCenter)
        self.serverIP2SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.serverIP2SpinBox.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.serverIP2SpinBox)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.serverIP3SpinBox = QSpinBox(self.centralwidget)
        self.serverIP3SpinBox.setObjectName(u"serverIP3SpinBox")
        self.serverIP3SpinBox.setFrame(False)
        self.serverIP3SpinBox.setAlignment(Qt.AlignCenter)
        self.serverIP3SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.serverIP3SpinBox.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.serverIP3SpinBox)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.serverIP4SpinBox = QSpinBox(self.centralwidget)
        self.serverIP4SpinBox.setObjectName(u"serverIP4SpinBox")
        self.serverIP4SpinBox.setFrame(False)
        self.serverIP4SpinBox.setAlignment(Qt.AlignCenter)
        self.serverIP4SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.serverIP4SpinBox.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.serverIP4SpinBox)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.serverPortSpinBox = QSpinBox(self.centralwidget)
        self.serverPortSpinBox.setObjectName(u"serverPortSpinBox")
        self.serverPortSpinBox.setFrame(False)
        self.serverPortSpinBox.setAlignment(Qt.AlignCenter)
        self.serverPortSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.serverPortSpinBox.setMaximum(65535)

        self.horizontalLayout_2.addWidget(self.serverPortSpinBox)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(5, 1)
        self.horizontalLayout_2.setStretch(7, 1)
        self.horizontalLayout_2.setStretch(9, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SOS Game Client", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Server IPV4 address and port:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u":", None))
    # retranslateUi

