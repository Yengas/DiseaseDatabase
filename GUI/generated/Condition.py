# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'condition.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_condition(object):
    def setupUi(self, condition):
        condition.setObjectName("condition")
        condition.resize(385, 106)
        self.verticalLayout = QtWidgets.QVBoxLayout(condition)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(condition)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.condition_name = QtWidgets.QLabel(condition)
        self.condition_name.setObjectName("condition_name")
        self.horizontalLayout.addWidget(self.condition_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(condition)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.weight_value = QtWidgets.QLabel(condition)
        self.weight_value.setObjectName("weight_value")
        self.horizontalLayout.addWidget(self.weight_value)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(condition)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.condition_about = QtWidgets.QLabel(condition)
        self.condition_about.setObjectName("condition_about")
        self.horizontalLayout_2.addWidget(self.condition_about)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(condition)
        QtCore.QMetaObject.connectSlotsByName(condition)

    def retranslateUi(self, condition):
        _translate = QtCore.QCoreApplication.translate
        condition.setWindowTitle(_translate("condition", "Form"))
        self.label.setText(_translate("condition", "Name:"))
        self.condition_name.setText(_translate("condition", "TextLabel"))
        self.label_2.setText(_translate("condition", "Ocurrence:"))
        self.weight_value.setText(_translate("condition", "TextLabel"))
        self.label_3.setText(_translate("condition", "About:"))
        self.condition_about.setText(_translate("condition", "TextLabel"))

