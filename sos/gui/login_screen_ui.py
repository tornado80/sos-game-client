# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_screen_ui.ui'
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


class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(668, 494)
        self.gridLayout = QGridLayout(LoginScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(LoginScreen)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.usernameLineEdit = QLineEdit(self.frame)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.usernameLineEdit)

        self.passwordLineEdit = QLineEdit(self.frame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.passwordLineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.loginButton = QPushButton(self.frame)
        self.loginButton.setObjectName(u"loginButton")

        self.horizontalLayout_2.addWidget(self.loginButton)

        self.signupButton = QPushButton(self.frame)
        self.signupButton.setObjectName(u"signupButton")

        self.horizontalLayout_2.addWidget(self.signupButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)


        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoginScreen", u"SOS Game", None))
        self.label_2.setText(QCoreApplication.translate("LoginScreen", u"Client Login Page", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Username", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("LoginScreen", u"Sign In", None))
        self.signupButton.setText(QCoreApplication.translate("LoginScreen", u"Sign Up", None))
    # retranslateUi

