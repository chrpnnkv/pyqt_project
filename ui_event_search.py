# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'event_searchPfumkV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_SearchEvent(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1323, 667)
        MainWindow.setStyleSheet(u"background-color: rgb(204, 213, 174);\n"
"selection-background-color: rgb(169, 176, 143);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(290, 0, 1021, 591))
        self.tableWidget.setStyleSheet(u"QHeaderView\n"
"{\n"
"	background-color: rgb(169, 176, 143);\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"	background-color: rgb(169, 176, 143);\n"
"	font: 8pt \"Century Gothic\";\n"
"}\n"
"\n"
"QTableWidget::item::selected \n"
"{\n"
" \n"
"	color: rgb(254, 253, 239);\n"
"	background-color: rgb(105, 109, 88);\n"
"	font: 8pt \"Century Gothic\";\n"
"}\n"
" ")
        self.typeBox = QComboBox(self.centralwidget)
        self.typeBox.addItem("")
        self.typeBox.setObjectName(u"typeBox")
        self.typeBox.setGeometry(QRect(20, 40, 241, 31))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(9)
        self.typeBox.setFont(font)
        self.typeBox.setStyleSheet(u"background-color:rgb(234, 241, 210);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 151, 16))
        self.label.setFont(font)
        self.placeBox = QComboBox(self.centralwidget)
        self.placeBox.addItem("")
        self.placeBox.setObjectName(u"placeBox")
        self.placeBox.setGeometry(QRect(20, 120, 241, 31))
        self.placeBox.setFont(font)
        self.placeBox.setStyleSheet(u"background-color:rgb(234, 241, 210);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 161, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 180, 141, 16))
        self.label_3.setFont(font)
        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(60, 380, 121, 31))
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet(u"background-color:rgb(105, 109, 88);\n"
"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 280, 151, 16))
        self.label_4.setFont(font)
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 200, 241, 31))
        self.dateEdit.setStyleSheet(u"background-color: rgb(234, 241, 210);\n"
"font: 9pt \"Century Gothic\";")
        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(20, 300, 241, 31))
        self.timeEdit.setStyleSheet(u"background-color: rgb(234, 241, 210);\n"
"font: 9pt \"Century Gothic\";")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 440, 191, 16))
        self.label_5.setFont(font)
        self.moreButton = QPushButton(self.centralwidget)
        self.moreButton.setObjectName(u"moreButton")
        self.moreButton.setGeometry(QRect(80, 510, 101, 31))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(8)
        self.moreButton.setFont(font1)
        self.moreButton.setStyleSheet(u"background-color:rgb(105, 109, 88);\n"
"color: rgb(255, 255, 255);")
        self.more = QLineEdit(self.centralwidget)
        self.more.setObjectName(u"more")
        self.more.setGeometry(QRect(20, 470, 221, 22))
        self.more.setStyleSheet(u"background-color: rgb(234, 241, 210);\n"
"font: 9pt \"Century Gothic\";")
        self.anydate = QCheckBox(self.centralwidget)
        self.anydate.setObjectName(u"anydate")
        self.anydate.setGeometry(QRect(20, 240, 111, 20))
        self.anydate.setStyleSheet(u"QCheckBox::indicator {\n"
"	border: 1px solid;\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: rgb(125, 130, 105);\n"
"}\n"
"QCheckBox {\n"
"	font: 9pt \"Century Gothic\";\n"
"}")
        self.anytime = QCheckBox(self.centralwidget)
        self.anytime.setObjectName(u"anytime")
        self.anytime.setGeometry(QRect(20, 340, 141, 20))
        self.anytime.setStyleSheet(u"QCheckBox::indicator {\n"
"	border: 1px solid;\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: rgb(125, 130, 105);\n"
"}\n"
"QCheckBox {\n"
"	font: 9pt \"Century Gothic\";\n"
"}")
        self.picture = QLabel(self.centralwidget)
        self.picture.setObjectName(u"label_6")
        self.picture.setGeometry(QRect(-20, 515, 275, 135))
        MainWindow.setCentralWidget(self.centralwidget)
        self.picture.raise_()
        self.tableWidget.raise_()
        self.typeBox.raise_()
        self.label.raise_()
        self.placeBox.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.searchButton.raise_()
        self.label_4.raise_()
        self.dateEdit.raise_()
        self.timeEdit.raise_()
        self.label_5.raise_()
        self.moreButton.raise_()
        self.more.raise_()
        self.anydate.raise_()
        self.anytime.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1323, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.typeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f:", None))
        self.placeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f:", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u043d\u0430\u0442\u044c \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435:", None))
        self.moreButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.more.setText("")
        self.more.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 ID", None))
        self.anydate.setText(QCoreApplication.translate("MainWindow", u"\u043b\u044e\u0431\u0430\u044f \u0434\u0430\u0442\u0430", None))
        self.anytime.setText(QCoreApplication.translate("MainWindow", u"\u043b\u044e\u0431\u043e\u0435 \u0432\u0440\u0435\u043c\u044f", None))
        self.picture.setText("")
    # retranslateUi

