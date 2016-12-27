# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bodypart.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BodyPart(object):
    def setupUi(self, BodyPart):
        BodyPart.setObjectName("BodyPart")
        BodyPart.resize(251, 238)
        self.verticalLayout = QtWidgets.QVBoxLayout(BodyPart)
        self.verticalLayout.setObjectName("verticalLayout")
        self.body_part_label = QtWidgets.QLabel(BodyPart)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.body_part_label.setFont(font)
        self.body_part_label.setObjectName("body_part_label")
        self.verticalLayout.addWidget(self.body_part_label)
        self.symptom_list = QtWidgets.QListWidget(BodyPart)
        self.symptom_list.setObjectName("symptom_list")
        self.verticalLayout.addWidget(self.symptom_list)

        self.retranslateUi(BodyPart)
        QtCore.QMetaObject.connectSlotsByName(BodyPart)

    def retranslateUi(self, BodyPart):
        _translate = QtCore.QCoreApplication.translate
        BodyPart.setWindowTitle(_translate("BodyPart", "Form"))
        self.body_part_label.setText(_translate("BodyPart", "Body Part"))

