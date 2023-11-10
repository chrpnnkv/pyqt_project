# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_newplacezUkAzf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_CreateNewPlace(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(345, 366)
        Form.setStyleSheet(u"background-color: rgb(234, 241, 210);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(105, 109, 88);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 91, 20))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(9)
        self.label.setFont(font)
        self.nameEdit = QLineEdit(Form)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setGeometry(QRect(20, 40, 281, 31))
        self.nameEdit.setStyleSheet(u"font: 9pt \"Century Gothic\";\n"
"background-color: rgb(254, 253, 239);")
        self.opentimeEdit = QTimeEdit(Form)
        self.opentimeEdit.setObjectName(u"opentimeEdit")
        self.opentimeEdit.setGeometry(QRect(81, 170, 101, 31))
        self.opentimeEdit.setStyleSheet(u"font: 9pt \"Century Gothic\";\n"
"background-color: rgb(254, 253, 239);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 150, 111, 16))
        self.label_2.setFont(font)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 180, 16, 16))
        self.label_4.setFont(font)
        self.createButton = QPushButton(Form)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(90, 300, 111, 31))
        self.createButton.setFont(font)
        self.createButton.setStyleSheet(u"background-color: rgb(105, 109, 88);\n"
"color: rgb(255, 255, 255);")
        self.addressEdit = QLineEdit(Form)
        self.addressEdit.setObjectName(u"addressEdit")
        self.addressEdit.setGeometry(QRect(20, 100, 281, 31))
        self.addressEdit.setStyleSheet(u"font: 9pt \"Century Gothic\";\n"
"background-color: rgb(254, 253, 239);")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 81, 61, 20))
        self.label_3.setFont(font)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 220, 31, 16))
        self.label_5.setFont(font)
        self.closetimeEdit = QTimeEdit(Form)
        self.closetimeEdit.setObjectName(u"closetimeEdit")
        self.closetimeEdit.setGeometry(QRect(81, 210, 101, 31))
        self.closetimeEdit.setStyleSheet(u"font: 9pt \"Century Gothic\";\n"
"background-color: rgb(254, 253, 239);")
        self.error_label = QLabel(Form)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(40, 260, 221, 20))
        self.error_label.setStyleSheet(u"font: 9pt \"Century Gothic\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0427\u0430\u0441\u044b \u0440\u0430\u0431\u043e\u0442\u044b:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0441:", None))
        self.createButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0434\u043e:", None))
        self.error_label.setText("")
    # retranslateUi

