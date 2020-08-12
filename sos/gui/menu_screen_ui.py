# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_screen_ui.ui'
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


class Ui_MenuScreen(object):
    def setupUi(self, MenuScreen):
        if not MenuScreen.objectName():
            MenuScreen.setObjectName(u"MenuScreen")
        MenuScreen.resize(862, 660)
        self.verticalLayout = QVBoxLayout(MenuScreen)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.signoutButton = QPushButton(MenuScreen)
        self.signoutButton.setObjectName(u"signoutButton")

        self.horizontalLayout.addWidget(self.signoutButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.myAccountButton = QPushButton(MenuScreen)
        self.myAccountButton.setObjectName(u"myAccountButton")

        self.horizontalLayout.addWidget(self.myAccountButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.toolBox = QToolBox(MenuScreen)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 844, 547))
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 2)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)

        self.joinGameButton = QPushButton(self.frame_2)
        self.joinGameButton.setObjectName(u"joinGameButton")

        self.gridLayout_3.addWidget(self.joinGameButton, 4, 1, 1, 1)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_3, 1, 0, 1, 2)

        self.gameIDSpinBox = QSpinBox(self.frame_2)
        self.gameIDSpinBox.setObjectName(u"gameIDSpinBox")
        self.gameIDSpinBox.setAlignment(Qt.AlignCenter)
        self.gameIDSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.gameIDSpinBox.setMaximum(2147483647)
        self.gameIDSpinBox.setValue(0)

        self.gridLayout_3.addWidget(self.gameIDSpinBox, 3, 1, 1, 1)

        self.creatorUsernameLineEdit = QLineEdit(self.frame_2)
        self.creatorUsernameLineEdit.setObjectName(u"creatorUsernameLineEdit")
        self.creatorUsernameLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.creatorUsernameLineEdit, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 1, 1, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 2, 1, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 0, 1, 1, 2)

        self.toolBox.addItem(self.page, u"Join Game")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 844, 547))
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.playerCountSpinBox = QSpinBox(self.frame)
        self.playerCountSpinBox.setObjectName(u"playerCountSpinBox")
        self.playerCountSpinBox.setAlignment(Qt.AlignCenter)
        self.playerCountSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.playerCountSpinBox.setMinimum(2)
        self.playerCountSpinBox.setMaximum(20)

        self.gridLayout_2.addWidget(self.playerCountSpinBox, 2, 1, 1, 1)

        self.boardSizeSpinBox = QSpinBox(self.frame)
        self.boardSizeSpinBox.setObjectName(u"boardSizeSpinBox")
        self.boardSizeSpinBox.setAlignment(Qt.AlignCenter)
        self.boardSizeSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.boardSizeSpinBox.setMinimum(1)
        self.boardSizeSpinBox.setMaximum(100)
        self.boardSizeSpinBox.setValue(10)

        self.gridLayout_2.addWidget(self.boardSizeSpinBox, 3, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.publicRadioButton = QRadioButton(self.frame)
        self.publicRadioButton.setObjectName(u"publicRadioButton")
        self.publicRadioButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.publicRadioButton)

        self.privateRadioButton = QRadioButton(self.frame)
        self.privateRadioButton.setObjectName(u"privateRadioButton")
        self.privateRadioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.privateRadioButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)

        self.createGameButton = QPushButton(self.frame)
        self.createGameButton.setObjectName(u"createGameButton")

        self.gridLayout_2.addWidget(self.createGameButton, 6, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.maxHintSpinBox = QSpinBox(self.frame)
        self.maxHintSpinBox.setObjectName(u"maxHintSpinBox")
        self.maxHintSpinBox.setAlignment(Qt.AlignCenter)
        self.maxHintSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.maxHintSpinBox.setMaximum(10)
        self.maxHintSpinBox.setValue(3)

        self.gridLayout_2.addWidget(self.maxHintSpinBox, 4, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(159, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.toolBox.addItem(self.page_2, u"New Game")

        self.verticalLayout.addWidget(self.toolBox)


        self.retranslateUi(MenuScreen)

        QMetaObject.connectSlotsByName(MenuScreen)
    # setupUi

    def retranslateUi(self, MenuScreen):
        MenuScreen.setWindowTitle(QCoreApplication.translate("MenuScreen", u"Form", None))
        self.signoutButton.setText(QCoreApplication.translate("MenuScreen", u"Sign Out", None))
        self.myAccountButton.setText(QCoreApplication.translate("MenuScreen", u"My Account", None))
        self.label_5.setText(QCoreApplication.translate("MenuScreen", u"Creator username:", None))
        self.label_6.setText(QCoreApplication.translate("MenuScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ef2929;\">NOTE</span></p><p><span style=\" font-weight:600;\">1.</span> First choose the game type (public or private).</p><p><span style=\" font-weight:600;\">2. </span>In case of public game, choose a game available globally.</p><p><span style=\" font-weight:600;\">3. </span>In case of private game, enter game creator username and game id to enter game screen. You can also see who has invited you to a game. Double click on the item and join the game.</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MenuScreen", u"Game ID:", None))
        self.joinGameButton.setText(QCoreApplication.translate("MenuScreen", u"Join game", None))
        self.creatorUsernameLineEdit.setPlaceholderText(QCoreApplication.translate("MenuScreen", u"username", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MenuScreen", u"Join Game", None))
        self.label.setText(QCoreApplication.translate("MenuScreen", u"Player count:", None))
        self.label_4.setText(QCoreApplication.translate("MenuScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ef2929;\">NOTE</span></p><p><span style=\" font-weight:600;\">1.</span> You can setup multiplayer game by increasing players upto 20.</p><p><span style=\" font-weight:600;\">2. </span>You can also increase board size upto 100. Board will be a square with given dimention.</p><p><span style=\" font-weight:600;\">3. </span>Note that limits mentioned above are due to graphical limits not game server.</p><p><span style=\" font-weight:600;\">4.</span> You can also let your game to be public or private. Namely you can give game id and your username to your friends to start game (private) or let it to be open by anyone connecting to server (public).</p><p><span style=\" font-weight:600;\">5.</span> Finally press <span style=\" font-style:italic;\">Create game</span> to broadcast the game and wait for players to join. As soon as number of players reach the given amount, game will be started automatically.</p></body></html>", None))
        self.publicRadioButton.setText(QCoreApplication.translate("MenuScreen", u"Public", None))
        self.privateRadioButton.setText(QCoreApplication.translate("MenuScreen", u"Private", None))
        self.createGameButton.setText(QCoreApplication.translate("MenuScreen", u"Create game", None))
        self.label_3.setText(QCoreApplication.translate("MenuScreen", u"Visibility:", None))
        self.label_2.setText(QCoreApplication.translate("MenuScreen", u"Board size:", None))
        self.label_7.setText(QCoreApplication.translate("MenuScreen", u"Max hint:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MenuScreen", u"New Game", None))
    # retranslateUi

