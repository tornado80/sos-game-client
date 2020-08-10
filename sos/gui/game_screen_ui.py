# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_screen_ui.ui'
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


class Ui_GameScreen(object):
    def setupUi(self, GameScreen):
        if not GameScreen.objectName():
            GameScreen.setObjectName(u"GameScreen")
        GameScreen.resize(827, 697)
        self.gridLayout_3 = QGridLayout(GameScreen)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.decreasePlayerButton = QPushButton(GameScreen)
        self.decreasePlayerButton.setObjectName(u"decreasePlayerButton")

        self.gridLayout_3.addWidget(self.decreasePlayerButton, 6, 2, 1, 1)

        self.label_4 = QLabel(GameScreen)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 3, 1, 1, 1)

        self.scrollArea_2 = QScrollArea(GameScreen)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.Box)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 232, 492))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.noPlayerJoinedLabel = QLabel(self.scrollAreaWidgetContents)
        self.noPlayerJoinedLabel.setObjectName(u"noPlayerJoinedLabel")
        self.noPlayerJoinedLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.noPlayerJoinedLabel)

        self.leaderBoard = QGridLayout()
        self.leaderBoard.setObjectName(u"leaderBoard")

        self.verticalLayout.addLayout(self.leaderBoard)

        self.verticalSpacer = QSpacerItem(20, 408, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea_2, 4, 1, 1, 2)

        self.scrollArea = QScrollArea(GameScreen)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.gameBoard = QWidget()
        self.gameBoard.setObjectName(u"gameBoard")
        self.gameBoard.setGeometry(QRect(0, 0, 567, 677))
        self.gridLayout_2 = QGridLayout(self.gameBoard)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea.setWidget(self.gameBoard)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 8, 1)

        self.boardSizeLabel = QLabel(GameScreen)
        self.boardSizeLabel.setObjectName(u"boardSizeLabel")
        self.boardSizeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.boardSizeLabel, 1, 2, 1, 1)

        self.label_3 = QLabel(GameScreen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 2, 1, 1, 1)

        self.backButton = QPushButton(GameScreen)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout_3.addWidget(self.backButton, 7, 2, 1, 1)

        self.label = QLabel(GameScreen)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.creatorUsernameLabel = QLabel(GameScreen)
        self.creatorUsernameLabel.setObjectName(u"creatorUsernameLabel")
        self.creatorUsernameLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.creatorUsernameLabel, 3, 2, 1, 1)

        self.playersCountLabel = QLabel(GameScreen)
        self.playersCountLabel.setObjectName(u"playersCountLabel")
        self.playersCountLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.playersCountLabel, 2, 2, 1, 1)

        self.leaveGameButton = QPushButton(GameScreen)
        self.leaveGameButton.setObjectName(u"leaveGameButton")

        self.gridLayout_3.addWidget(self.leaveGameButton, 7, 1, 1, 1)

        self.label_2 = QLabel(GameScreen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)

        self.increasePlayerButton = QPushButton(GameScreen)
        self.increasePlayerButton.setObjectName(u"increasePlayerButton")

        self.gridLayout_3.addWidget(self.increasePlayerButton, 6, 1, 1, 1)

        self.gameIDLabel = QLabel(GameScreen)
        self.gameIDLabel.setObjectName(u"gameIDLabel")
        self.gameIDLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.gameIDLabel, 0, 2, 1, 1)

        self.pushButton = QPushButton(GameScreen)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 5, 1, 1, 2)


        self.retranslateUi(GameScreen)

        QMetaObject.connectSlotsByName(GameScreen)
    # setupUi

    def retranslateUi(self, GameScreen):
        GameScreen.setWindowTitle(QCoreApplication.translate("GameScreen", u"Form", None))
        self.decreasePlayerButton.setText(QCoreApplication.translate("GameScreen", u"Decrease player", None))
        self.label_4.setText(QCoreApplication.translate("GameScreen", u"Creator:", None))
        self.label_7.setText(QCoreApplication.translate("GameScreen", u"Players:", None))
        self.noPlayerJoinedLabel.setText(QCoreApplication.translate("GameScreen", u"No player joined yet!", None))
        self.boardSizeLabel.setText(QCoreApplication.translate("GameScreen", u"0", None))
        self.label_3.setText(QCoreApplication.translate("GameScreen", u"Players count:", None))
        self.backButton.setText(QCoreApplication.translate("GameScreen", u"Back", None))
        self.label.setText(QCoreApplication.translate("GameScreen", u"Game ID:", None))
        self.creatorUsernameLabel.setText(QCoreApplication.translate("GameScreen", u"username", None))
        self.playersCountLabel.setText(QCoreApplication.translate("GameScreen", u"0", None))
        self.leaveGameButton.setText(QCoreApplication.translate("GameScreen", u"Leave game", None))
        self.label_2.setText(QCoreApplication.translate("GameScreen", u"Board size:", None))
        self.increasePlayerButton.setText(QCoreApplication.translate("GameScreen", u"Increase player", None))
        self.gameIDLabel.setText(QCoreApplication.translate("GameScreen", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("GameScreen", u"Get hint (3)", None))
    # retranslateUi

