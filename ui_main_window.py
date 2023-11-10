# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maineFVeEN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(620, 420)
        MainWindow.setStyleSheet(u"background-color: rgb(233, 237, 201);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 95, 401, 101))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(105, 109, 88);")
        self.findButton = QPushButton(self.centralwidget)
        self.findButton.setObjectName(u"findButton")
        self.findButton.setGeometry(QRect(90, 205, 201, 61))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.findButton.setFont(font1)
        self.findButton.setStyleSheet(u"background-color: rgb(145, 150, 122);\n"
"color: rgb(255, 255, 255);")
        self.createButton = QPushButton(self.centralwidget)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(310, 205, 201, 61))
        self.createButton.setFont(font1)
        self.createButton.setStyleSheet(u"background-color:rgb(145, 150, 122);\n"
"color: rgb(255, 255, 255);")
        self.picture2 = QLabel(self.centralwidget)
        self.picture2.setObjectName(u"picture2")
        self.picture2.setGeometry(QRect(40, 300, 531, 81))
        self.picture1 = QLabel(self.centralwidget)
        self.picture1.setObjectName(u"picture1")
        self.picture1.setGeometry(QRect(40, 15, 521, 81))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 620, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u042f\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.findButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435", None))
        self.picture2.setText("")
        self.picture1.setText("")
    # retranslateUi

