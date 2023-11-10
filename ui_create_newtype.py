# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_newtypeoJZktb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_CreateNewType(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(277, 191)
        Form.setStyleSheet(u"background-color: rgb(233, 237, 201);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(105, 109, 88);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 151, 16))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(9)
        self.label.setFont(font)
        self.createButton = QPushButton(Form)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(80, 100, 101, 31))
        self.createButton.setStyleSheet(u"font: 9pt \"Century Gothic\";\n"
"background-color: rgb(105, 109, 88);\n"
"color: rgb(255, 255, 255);")
        self.typeEdit = QLineEdit(Form)
        self.typeEdit.setObjectName(u"typeEdit")
        self.typeEdit.setGeometry(QRect(30, 50, 181, 31))
        self.typeEdit.setStyleSheet(u"background-color: rgb(254, 253, 239);\n"
"font: 9pt \"Century Gothic\";")
        self.error_label = QLabel(Form)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(30, 150, 211, 16))
        self.error_label.setStyleSheet(u"font: 9pt \"Century Gothic\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f:", None))
        self.createButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.typeEdit.setText("")
        self.error_label.setText("")
    # retranslateUi

