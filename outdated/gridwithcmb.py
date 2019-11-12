# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gridwithcmb.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 60, 131, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 3, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 5, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 4, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_7.setText(_translate("MainWindow", "CheckBox"))

