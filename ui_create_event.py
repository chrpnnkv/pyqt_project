# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_eventbBulPu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_CreateEvent(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(836, 743)
        MainWindow.setStyleSheet(u"background-color: rgb(204, 213, 174);\n"
"selection-background-color: rgb(169, 176, 143);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 841, 700))
        font = QFont()
        font.setFamily(u"Century Gothic")
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"	boder: 1px;\n"
"	background: rgb(204, 213, 174);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	background: rgb(227, 231, 196);\n"
"	min-width: 200 px;\n"
"	min-height: 30 px;\n"
"	margin-left: 1px;\n"
"	left: -1px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background: rgb(204, 213, 174);\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"	background: rgb(233, 237, 201);\n"
"}\n"
"\n"
"")
        self.edit_tab = QWidget()
        self.edit_tab.setObjectName(u"edit_tab")
        self.edit_tab.setFont(font)
        self.tableWidget = QTableWidget(self.edit_tab)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 10, 831, 581))
        self.tableWidget.setStyleSheet(u"background-color: rgb(204, 213, 174);\n"
"QHeaderView\n"
"{\n"
"	background-color: rgb(169, 176, 143);\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"	background-color: rgb(169, 176, 143);\n"
"	font: 9pt \"Century Gothic\";\n"
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
        self.changeButton = QPushButton(self.edit_tab)
        self.changeButton.setObjectName(u"changeButton")
        self.changeButton.setGeometry(QRect(350, 597, 141, 41))
        self.changeButton.setStyleSheet(u"background-color: rgb(105, 109, 88);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Century Gothic\";")
        self.syntax_label = QLabel(self.edit_tab)
        self.syntax_label.setObjectName(u"syntax_label")
        self.syntax_label.setGeometry(QRect(70, 610, 251, 20))
        self.syntax_label.setStyleSheet(u"font: 9pt \"Century Gothic\";")
        self.tabWidget.addTab(self.edit_tab, "")
        self.add_tab = QWidget()
        self.add_tab.setObjectName(u"add_tab")
        self.label_4 = QLabel(self.add_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 0, 221, 31))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(10)
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.add_tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 490, 81, 16))
        font2 = QFont()
        font2.setFamily(u"Century Gothic")
        font2.setPointSize(9)
        self.label_5.setFont(font2)
        self.label_2 = QLabel(self.add_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 200, 161, 16))
        self.label_2.setFont(font2)
        self.add_placeButton = QPushButton(self.add_tab)
        self.add_placeButton.setObjectName(u"add_placeButton")
        self.add_placeButton.setGeometry(QRect(20, 260, 211, 28))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(8)
        self.add_placeButton.setFont(font3)
        self.add_placeButton.setStyleSheet(u"background-color: rgb(105, 109, 88);\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.add_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 320, 221, 16))
        self.label_3.setFont(font2)
        self.description = QPlainTextEdit(self.add_tab)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(360, 30, 431, 481))
        self.description.setFont(font2)
        self.description.setStyleSheet(u"background-color: rgb(234, 241, 210);")
        self.createButton = QPushButton(self.add_tab)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(300, 590, 181, 41))
        font4 = QFont()
        font4.setFamily(u"Century Gothic")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.createButton.setFont(font4)
        self.createButton.setStyleSheet(u"background-color: rgb(105, 109, 88);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Century Gothic\";")
        self.imgButton = QPushButton(self.add_tab)
        self.imgButton.setObjectName(u"imgButton")
        self.imgButton.setGeometry(QRect(20, 510, 221, 31))
        self.imgButton.setFont(font3)
        self.imgButton.setStyleSheet(u"background-color: rgb(105, 109, 88);\n"
"color: rgb(255, 255, 255);")
        self.typeBox = QComboBox(self.add_tab)
        self.typeBox.addItem("")
        self.typeBox.setObjectName(u"typeBox")
        self.typeBox.setGeometry(QRect(20, 100, 241, 31))
        self.typeBox.setFont(font2)
        self.typeBox.setStyleSheet(u"background-color: rgb(234, 241, 210);")
        self.label = QLabel(self.add_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 151, 16))
        self.label.setFont(font2)
        self.placeBox = QComboBox(self.add_tab)
        self.placeBox.addItem("")
        self.placeBox.setObjectName(u"placeBox")
        self.placeBox.setGeometry(QRect(20, 220, 241, 31))
        self.placeBox.setFont(font2)
        self.placeBox.setStyleSheet(u"background-color: rgb(234, 241, 210);")
        self.add_typeButton = QPushButton(self.add_tab)
        self.add_typeButton.setObjectName(u"add_typeButton")
        self.add_typeButton.setGeometry(QRect(20, 140, 161, 28))
        self.add_typeButton.setFont(font3)
        self.add_typeButton.setStyleSheet(u"background-color: rgb(105, 109, 88);\n"
"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.add_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 390, 16, 16))
        self.label_6.setFont(font2)
        self.label_7 = QLabel(self.add_tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 430, 31, 16))
        self.label_7.setFont(font2)
        self.begintimeEdit = QTimeEdit(self.add_tab)
        self.begintimeEdit.setObjectName(u"begintimeEdit")
        self.begintimeEdit.setGeometry(QRect(110, 380, 121, 31))
        self.begintimeEdit.setStyleSheet(u"background-color: rgb(234, 241, 210);\n"
"font: 9pt \"Century Gothic\";")
        self.endtimeEdit = QTimeEdit(self.add_tab)
        self.endtimeEdit.setObjectName(u"endtimeEdit")
        self.endtimeEdit.setGeometry(QRect(110, 420, 121, 31))
        self.endtimeEdit.setStyleSheet(u"background-color: rgb(234, 241, 210);\n"
"font: 9pt \"Century Gothic\";")
        self.dateEdit = QDateEdit(self.add_tab)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 340, 211, 31))
        self.dateEdit.setStyleSheet(u"background-color: rgb(234, 241, 210);\n"
"font: 9pt \"Century Gothic\";")
        self.error_label = QLabel(self.add_tab)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(270, 550, 271, 16))
        self.error_label.setStyleSheet(u"font: 9pt \"Century Gothic\";")
        self.label_8 = QLabel(self.add_tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 10, 151, 16))
        self.label_8.setFont(font2)
        self.name = QLineEdit(self.add_tab)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(20, 31, 241, 31))
        self.name.setStyleSheet(u"background-color: rgb(234, 241, 210);\n"
"font: 9pt \"Century Gothic\";\n"
"border: 1px solid rgb(105, 109, 88);")
        self.picture1 = QLabel(self.add_tab)
        self.picture1.setObjectName(u"picture1")
        self.picture1.setGeometry(QRect(580, 520, 201, 140))
        self.picture2 = QLabel(self.add_tab)
        self.picture2.setObjectName(u"picture2")
        self.picture2.setGeometry(QRect(50, 560, 161, 120))
        self.tabWidget.addTab(self.add_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 836, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.changeButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.syntax_label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.edit_tab), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0444\u0438\u0448\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f:", None))
        self.add_placeButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f:", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.imgButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.typeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f:", None))
        self.placeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.add_typeButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0442\u0438\u043f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0441:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e:", None))
        self.error_label.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.name.setText("")
        self.picture1.setText("")
        self.picture2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_tab), QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435", None))
    # retranslateUi

