# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_tbl_meals.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):

    def loadData(self):
        connection = sqlite3.connect('mydatabase.db')
        query = "SELECT * FROM tbl_meals"
        result = connection.execute(query)
        self.tableView.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableView.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableView.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))

        connection.close()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableView(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 781, 271))
        self.tableView.setObjectName("tableView")
        self.btn_get_meal_list = QtWidgets.QPushButton(self.centralwidget)
        self.btn_get_meal_list.setGeometry(QtCore.QRect(330, 340, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_get_meal_list.setFont(font)
        self.btn_get_meal_list.setObjectName("btn_get_meal_list")

        self.btn_get_meal_list.clicked.connect(self.loadData)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_get_meal_list.setText(_translate("MainWindow", "Get Meal List"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save the current file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy selected text"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste copied text"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

