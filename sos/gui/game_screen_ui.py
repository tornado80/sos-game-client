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
        GameScreen.resize(965, 850)
        self.verticalLayout_2 = QVBoxLayout(GameScreen)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(GameScreen)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 90, 830))
        self.gameBoard = QGridLayout(self.widget)
        self.gameBoard.setObjectName(u"gameBoard")
        self.scrollArea.setWidget(self.widget)
        self.splitter.addWidget(self.scrollArea)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.gameIDLabel = QLabel(self.layoutWidget)
        self.gameIDLabel.setObjectName(u"gameIDLabel")
        self.gameIDLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.gameIDLabel, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.boardSizeLabel = QLabel(self.layoutWidget)
        self.boardSizeLabel.setObjectName(u"boardSizeLabel")
        self.boardSizeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.boardSizeLabel, 1, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.playersCountLabel = QLabel(self.layoutWidget)
        self.playersCountLabel.setObjectName(u"playersCountLabel")
        self.playersCountLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.playersCountLabel, 2, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.maxHintLabel = QLabel(self.layoutWidget)
        self.maxHintLabel.setObjectName(u"maxHintLabel")
        self.maxHintLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.maxHintLabel, 3, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.creatorUsernameLabel = QLabel(self.layoutWidget)
        self.creatorUsernameLabel.setObjectName(u"creatorUsernameLabel")
        self.creatorUsernameLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.creatorUsernameLabel, 4, 1, 1, 1)

        self.scrollArea_2 = QScrollArea(self.layoutWidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.Box)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 847, 682))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line_2)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line_3)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line_4)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout)

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

        self.yourTurnLabel = QLabel(self.scrollAreaWidgetContents)
        self.yourTurnLabel.setObjectName(u"yourTurnLabel")
        self.yourTurnLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.yourTurnLabel)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea_2, 5, 0, 1, 2)

        self.getHintButton = QPushButton(self.layoutWidget)
        self.getHintButton.setObjectName(u"getHintButton")

        self.gridLayout.addWidget(self.getHintButton, 6, 0, 1, 1)

        self.backButton = QPushButton(self.layoutWidget)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout.addWidget(self.backButton, 6, 1, 1, 1)

        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout_2.addWidget(self.splitter)


        self.retranslateUi(GameScreen)

        QMetaObject.connectSlotsByName(GameScreen)
    # setupUi

    def retranslateUi(self, GameScreen):
        GameScreen.setWindowTitle(QCoreApplication.translate("GameScreen", u"Form", None))
        self.label.setText(QCoreApplication.translate("GameScreen", u"Game ID:", None))
        self.gameIDLabel.setText(QCoreApplication.translate("GameScreen", u"0", None))
        self.label_2.setText(QCoreApplication.translate("GameScreen", u"Board size:", None))
        self.boardSizeLabel.setText(QCoreApplication.translate("GameScreen", u"0", None))
        self.label_3.setText(QCoreApplication.translate("GameScreen", u"Players count:", None))
        self.playersCountLabel.setText(QCoreApplication.translate("GameScreen", u"0", None))
        self.label_5.setText(QCoreApplication.translate("GameScreen", u"Max hint:", None))
        self.maxHintLabel.setText(QCoreApplication.translate("GameScreen", u"0", None))
        self.label_4.setText(QCoreApplication.translate("GameScreen", u"Creator:", None))
        self.creatorUsernameLabel.setText("")
        self.label_7.setText(QCoreApplication.translate("GameScreen", u"Players joined:", None))
        self.label_6.setText(QCoreApplication.translate("GameScreen", u"username", None))
        self.label_8.setText(QCoreApplication.translate("GameScreen", u"score", None))
        self.label_9.setText(QCoreApplication.translate("GameScreen", u"hints used", None))
        self.label_10.setText(QCoreApplication.translate("GameScreen", u"status", None))
        self.noPlayerJoinedLabel.setText(QCoreApplication.translate("GameScreen", u"No player joined yet!", None))
        self.yourTurnLabel.setText(QCoreApplication.translate("GameScreen", u"<html><head/><body><p><span style=\" font-weight:600; color:#ef2929;\">YOUR TURN</span></p></body></html>", None))
        self.getHintButton.setText(QCoreApplication.translate("GameScreen", u"Get hint", None))
        self.backButton.setText(QCoreApplication.translate("GameScreen", u"Back", None))
    # retranslateUi

