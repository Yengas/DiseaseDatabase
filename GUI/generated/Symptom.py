# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'symptom.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Symptom(object):
    def setupUi(self, Symptom):
        Symptom.setObjectName("Symptom")
        Symptom.resize(400, 40)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Symptom)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.symptom_name = QtWidgets.QLabel(Symptom)
        self.symptom_name.setObjectName("symptom_name")
        self.horizontalLayout.addWidget(self.symptom_name)
        self.remove_button = QtWidgets.QPushButton(Symptom)
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout.addWidget(self.remove_button)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 3)

        self.retranslateUi(Symptom)
        QtCore.QMetaObject.connectSlotsByName(Symptom)

    def retranslateUi(self, Symptom):
        _translate = QtCore.QCoreApplication.translate
        Symptom.setWindowTitle(_translate("Symptom", "Form"))
        self.symptom_name.setText(_translate("Symptom", "Symptom"))
        self.remove_button.setText(_translate("Symptom", "Remove"))

