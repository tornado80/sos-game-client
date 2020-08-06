# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account_screen_ui.ui'
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


class Ui_AccountScreen(object):
    def setupUi(self, AccountScreen):
        if not AccountScreen.objectName():
            AccountScreen.setObjectName(u"AccountScreen")
        AccountScreen.resize(937, 748)
        self.verticalLayout = QVBoxLayout(AccountScreen)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.backButton = QPushButton(AccountScreen)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout.addWidget(self.backButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(AccountScreen)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 868, 673))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.firstnameLineEdit = QLineEdit(self.groupBox)
        self.firstnameLineEdit.setObjectName(u"firstnameLineEdit")

        self.gridLayout.addWidget(self.firstnameLineEdit, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lastnameLineEdit = QLineEdit(self.groupBox)
        self.lastnameLineEdit.setObjectName(u"lastnameLineEdit")

        self.gridLayout.addWidget(self.lastnameLineEdit, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.usernameLineEdit = QLineEdit(self.groupBox_2)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.gridLayout_2.addWidget(self.usernameLineEdit, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)

        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.newPasswordLineEdit = QLineEdit(self.groupBox_3)
        self.newPasswordLineEdit.setObjectName(u"newPasswordLineEdit")
        self.newPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.newPasswordLineEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.repeatPasswordLineEdit = QLineEdit(self.groupBox_3)
        self.repeatPasswordLineEdit.setObjectName(u"repeatPasswordLineEdit")
        self.repeatPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.repeatPasswordLineEdit, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)

        self.ratingSpinBox = QSpinBox(self.groupBox_4)
        self.ratingSpinBox.setObjectName(u"ratingSpinBox")
        self.ratingSpinBox.setReadOnly(True)
        self.ratingSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_4.addWidget(self.ratingSpinBox, 0, 1, 1, 1)

        self.winsSpinBox = QSpinBox(self.groupBox_4)
        self.winsSpinBox.setObjectName(u"winsSpinBox")
        self.winsSpinBox.setReadOnly(True)
        self.winsSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_4.addWidget(self.winsSpinBox, 1, 1, 1, 1)

        self.gamesSpinBox = QSpinBox(self.groupBox_4)
        self.gamesSpinBox.setObjectName(u"gamesSpinBox")
        self.gamesSpinBox.setReadOnly(True)
        self.gamesSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_4.addWidget(self.gamesSpinBox, 2, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(1, 1)

        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)

        self.joinedDateTimeEdit = QDateTimeEdit(self.groupBox_5)
        self.joinedDateTimeEdit.setObjectName(u"joinedDateTimeEdit")
        self.joinedDateTimeEdit.setReadOnly(True)
        self.joinedDateTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_5.addWidget(self.joinedDateTimeEdit, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)

        self.lastLoginDateTimeEdit = QDateTimeEdit(self.groupBox_5)
        self.lastLoginDateTimeEdit.setObjectName(u"lastLoginDateTimeEdit")
        self.lastLoginDateTimeEdit.setReadOnly(True)
        self.lastLoginDateTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_5.addWidget(self.lastLoginDateTimeEdit, 1, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(1, 1)

        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.currentPasswordLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.currentPasswordLineEdit.setObjectName(u"currentPasswordLineEdit")
        self.currentPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.currentPasswordLineEdit)

        self.updateAccountButton = QPushButton(self.scrollAreaWidgetContents)
        self.updateAccountButton.setObjectName(u"updateAccountButton")

        self.horizontalLayout_3.addWidget(self.updateAccountButton)

        self.removeAccountButton = QPushButton(self.scrollAreaWidgetContents)
        self.removeAccountButton.setObjectName(u"removeAccountButton")

        self.horizontalLayout_3.addWidget(self.removeAccountButton)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(AccountScreen)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AccountScreen)
    # setupUi

    def retranslateUi(self, AccountScreen):
        AccountScreen.setWindowTitle(QCoreApplication.translate("AccountScreen", u"Form", None))
        self.backButton.setText(QCoreApplication.translate("AccountScreen", u"Back", None))
        self.groupBox.setTitle(QCoreApplication.translate("AccountScreen", u"First name && Last name", None))
        self.label.setText(QCoreApplication.translate("AccountScreen", u"First name:", None))
        self.label_2.setText(QCoreApplication.translate("AccountScreen", u"Last name:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AccountScreen", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("AccountScreen", u"Username:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("AccountScreen", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("AccountScreen", u"New password:", None))
        self.label_5.setText(QCoreApplication.translate("AccountScreen", u"Repeat password:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("AccountScreen", u"Rating", None))
        self.label_6.setText(QCoreApplication.translate("AccountScreen", u"Total rating:", None))
        self.label_7.setText(QCoreApplication.translate("AccountScreen", u"Total wins:", None))
        self.label_8.setText(QCoreApplication.translate("AccountScreen", u"Total games:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("AccountScreen", u"Date stuff", None))
        self.label_9.setText(QCoreApplication.translate("AccountScreen", u"Joined at:", None))
        self.joinedDateTimeEdit.setDisplayFormat(QCoreApplication.translate("AccountScreen", u"dd/MM/yyyy HH:mm:ss.zzzzzz", None))
        self.label_10.setText(QCoreApplication.translate("AccountScreen", u"Last login:", None))
        self.lastLoginDateTimeEdit.setDisplayFormat(QCoreApplication.translate("AccountScreen", u"dd/MM/yyyy HH:mm:ss.zzzzzz", None))
        self.label_11.setText(QCoreApplication.translate("AccountScreen", u"Current password:", None))
        self.updateAccountButton.setText(QCoreApplication.translate("AccountScreen", u"Update account", None))
        self.removeAccountButton.setText(QCoreApplication.translate("AccountScreen", u"Remove account", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("AccountScreen", u"Profile && Rating", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AccountScreen", u"Games History", None))
    # retranslateUi

