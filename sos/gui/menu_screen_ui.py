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
        MenuScreen.resize(894, 624)
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
        self.page.setGeometry(QRect(0, 0, 876, 511))
        self.toolBox.addItem(self.page, u"Join Game")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 98, 28))
        self.toolBox.addItem(self.page_2, u"New Game")

        self.verticalLayout.addWidget(self.toolBox)


        self.retranslateUi(MenuScreen)

        QMetaObject.connectSlotsByName(MenuScreen)
    # setupUi

    def retranslateUi(self, MenuScreen):
        MenuScreen.setWindowTitle(QCoreApplication.translate("MenuScreen", u"Form", None))
        self.signoutButton.setText(QCoreApplication.translate("MenuScreen", u"Sign Out", None))
        self.myAccountButton.setText(QCoreApplication.translate("MenuScreen", u"My Account", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MenuScreen", u"Join Game", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MenuScreen", u"New Game", None))
    # retranslateUi

