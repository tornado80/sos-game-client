# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup_screen_ui.ui'
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


class Ui_SignUpScreen(object):
    def setupUi(self, SignUpScreen):
        if not SignUpScreen.objectName():
            SignUpScreen.setObjectName(u"SignUpScreen")
        SignUpScreen.resize(668, 494)
        self.gridLayout = QGridLayout(SignUpScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(SignUpScreen)
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

        self.firstnameLineEdit = QLineEdit(self.frame)
        self.firstnameLineEdit.setObjectName(u"firstnameLineEdit")
        self.firstnameLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.firstnameLineEdit)

        self.lastnameLineEdit = QLineEdit(self.frame)
        self.lastnameLineEdit.setObjectName(u"lastnameLineEdit")
        self.lastnameLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lastnameLineEdit)

        self.usernameLineEdit = QLineEdit(self.frame)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.usernameLineEdit)

        self.passwordLineEdit = QLineEdit(self.frame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.passwordLineEdit)

        self.repeatPasswordLineEdit = QLineEdit(self.frame)
        self.repeatPasswordLineEdit.setObjectName(u"repeatPasswordLineEdit")
        self.repeatPasswordLineEdit.setEchoMode(QLineEdit.Password)
        self.repeatPasswordLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.repeatPasswordLineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.backButton = QPushButton(self.frame)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout_2.addWidget(self.backButton)

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


        self.retranslateUi(SignUpScreen)

        QMetaObject.connectSlotsByName(SignUpScreen)
    # setupUi

    def retranslateUi(self, SignUpScreen):
        SignUpScreen.setWindowTitle(QCoreApplication.translate("SignUpScreen", u"Form", None))
        self.label.setText(QCoreApplication.translate("SignUpScreen", u"SOS Game", None))
        self.label_2.setText(QCoreApplication.translate("SignUpScreen", u"Client Sign Up Page", None))
        self.firstnameLineEdit.setPlaceholderText(QCoreApplication.translate("SignUpScreen", u"First name", None))
        self.lastnameLineEdit.setPlaceholderText(QCoreApplication.translate("SignUpScreen", u"Last name", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("SignUpScreen", u"Username", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("SignUpScreen", u"Password", None))
        self.repeatPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("SignUpScreen", u"Repeat password", None))
        self.backButton.setText(QCoreApplication.translate("SignUpScreen", u"Back", None))
        self.signupButton.setText(QCoreApplication.translate("SignUpScreen", u"Sign Up", None))
    # retranslateUi

