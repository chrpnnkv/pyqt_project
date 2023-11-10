# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'moreHLJICN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_More(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(715, 470)
        Form.setStyleSheet(u"background-color: rgb(169, 176, 143);")
        self.picture = QLabel(Form)
        self.picture.setObjectName(u"picture")
        self.picture.setGeometry(QRect(410, 30, 271, 381))
        self.description = QPlainTextEdit(Form)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(20, 20, 351, 421))
        self.description.setStyleSheet(u"background-color: rgb(234, 241, 210);\n"
"font: 10pt \"Century Gothic\";\n"
"selection-background-color: rgb(105, 109, 88);\n"
"selection-color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.picture.setText("")
        self.description.setPlainText("")
    # retranslateUi

