# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mealPlanner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
"""
#todo edit meal list tab:
#todo   add function for deleting, adding, editing

"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import sqlite3
from sqlite3 import Error
import re


class Ui_win_MealPlanner(object):
    db_file = "mydatabase.db"

    # def create_connection():
    #     conn = None
    #     try:
    #         conn = sqlite3.connect('mydatabase.db')
    #     except Error as e:
    #         print(e)

    #     return conn

    def loadEditTable(self):
        horzheaders = ["ID #", "Meal Type", "Meal Name", "Recipe",
                       "Grocery List"]
        connection = sqlite3.connect('mydatabase.db')
        query = "SELECT * FROM tbl_menulist"
        result = connection.execute(query)
        self.tbl_Edit.setColumnCount(5)
        self.tbl_Edit.setRowCount(0)
        self.tbl_Edit.setColumnWidth(1, 100)
        self.tbl_Edit.setColumnWidth(0, 0)
        self.tbl_Edit.setColumnWidth(2, 200)
        self.tbl_Edit.setColumnWidth(3, 200)
        self.tbl_Edit.setColumnWidth(4, 500)
        for row_number, row_data in enumerate(result):
            self.tbl_Edit.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tbl_Edit.setItem(row_number, column_number,
                                      QtWidgets.QTableWidgetItem(str(data)))
                self.tbl_Edit.setHorizontalHeaderLabels(horzheaders)
        self.tbl_Edit.verticalHeader().setVisible(False)
        self.tbl_Edit.resizeRowsToContents()
        connection.close()

    def addMeal(self, meal):
        connection = sqlite3.connect('mydatabase.db')
        crsr = connection.cursor()
        crsr.execute("INSERT INTO tbl_menulist (mealType, mealName, recipe, groceryList) VALUES (?,?,?,?)", meal)
        connection.commit()
        connection.close()

    def messageBox(self, msg, title):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect(msgButtonClick)

        returnValue = msgBox.exec()
        # if returnValue == QtWidgets.QMessageBox.Ok:
        #     print("OK clicked")

    def mealToAdd(self):
        mealType = self.cmbBx_MealType.currentText()
        mealName = self.txtbox_mealName.text()
        recipe = self.txtbox_recipe.text()
        grocerylist = self.txtbox_GroceryList.text()
        if mealType == "Select Meal Type":
            msg = "Tried to add meal without meal type.\nPlease select meal type and add the meal again."
            title = "Missing meal type"
            self.messageBox(msg, title)
            return
        if mealName == "":
            msg = "Tried to add meal without meal name.\nPlease enter a meal name and add the meal again."
            title = "Missing meal name"
            self.messageBox(msg, title)
            return
        if recipe == "":
            msg = "Adding a meal without a recipe. This meal will be added without a recipe."
            title = "Alert"
            self.messageBox(msg, title)
        if grocerylist == "":
            msg = "Tried to add meal without grocery items.\nPlease enter grocery items and add the meal again."
            title = "Missing grocery list"
            self.messageBox(msg, title)
            return
        meal = (mealType, mealName, recipe, grocerylist)
        self.addMeal(meal)
        self.txtbox_GroceryList.setText("")
        self.txtbox_mealName.setText("")
        self.txtbox_recipe.setText("")
        self.cmbBx_MealType.setCurrentIndex(0)
        self.loadEditTable()

    def deleteMeal(self):
        rowNum = self.tbl_Edit.currentRow()
        item = self.tbl_Edit.item(rowNum, 0)
        item = item.text()
        print(item)
        connection = sqlite3.connect('mydatabase.db')
        crsr = connection.cursor()
        crsr.execute("DELETE FROM tbl_menulist WHERE id=" + str(item))

        mT = self.tbl_Edit.item(rowNum, 1)
        mT = mT.text()
        print(mT)
        mealType = ["Breakfast", "Breakfast/Dinner", "Lunch", "Lunch/Dinner", "Dinner"]
        if mealType.index(mT) == 0:
            self.cmbBx_MealType.setCurrentIndex(1)
        elif mealType.index(mT) == 1:
            self.cmbBx_MealType.setCurrentIndex(2)
        elif mealType.index(mT) == 2:
            self.cmbBx_MealType.setCurrentIndex(3)
        elif mealType.index(mT) == 3:
            self.cmbBx_MealType.setCurrentIndex(4)
        elif mealType.index(mT) == 4:
            self.cmbBx_MealType.setCurrentIndex(5)
        mN = self.tbl_Edit.item(rowNum, 2)
        mN = mN.text()
        self.txtbox_mealName.setText(mN)
        rec = self.tbl_Edit.item(rowNum, 3)
        rec = rec.text()
        self.txtbox_recipe.setText(rec)
        gL = self.tbl_Edit.item(rowNum, 4)
        gL = gL.text()
        self.txtbox_GroceryList.setText(gL)
        connection.commit()
        connection.close()
        # self.txtbox_GroceryList.setText("")
        # self.txtbox_mealName.setText("")
        # self.txtbox_recipe.setText("")
        # self.cmbBx_MealType.setCurrentIndex(0)
        self.loadEditTable()

    def breakfast_count(self):
        br_count = 0
        for br in self.grpBx_Breakfast.findChildren(QtWidgets.QCheckBox):
            if br.isChecked():
                br_count += 1
        return br_count

    def lunch_count(self):
        lu_count = 0
        for lu in self.grpBx_Lunch.findChildren(QtWidgets.QCheckBox):
            if lu.isChecked():
                lu_count += 1
        return lu_count

    def dinner_count(self):
        di_count = 0
        for di in self.grpBx_Dinner.findChildren(QtWidgets.QCheckBox):
            if di.isChecked():
                di_count += 1
        return di_count

    def createMealPlanTable(self, lookups):
        horzheaders = ["ID #", "Meal Type", "Meal Name", "Recipe",
                       "Grocery List"]
        connection = sqlite3.connect('mydatabase.db')
        crsr = connection.cursor()
        self.tbl_CreateMealPlan.setColumnCount(5)
        self.tbl_CreateMealPlan.setRowCount(0)
        self.tbl_CreateMealPlan.setColumnWidth(0, 0)
        self.tbl_CreateMealPlan.setColumnWidth(1, 100)
        self.tbl_CreateMealPlan.setColumnWidth(2, 200)
        self.tbl_CreateMealPlan.setColumnWidth(3, 200)
        self.tbl_CreateMealPlan.setColumnWidth(4, 500)
        for lookup in lookups:
            crsr.execute(lookup)
            for row_number, row_data in enumerate(crsr):
                self.tbl_CreateMealPlan.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tbl_CreateMealPlan.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.tbl_CreateMealPlan.setHorizontalHeaderLabels(horzheaders)
        self.tbl_CreateMealPlan.resizeRowsToContents()
        self.tbl_CreateMealPlan.verticalHeader().setVisible(False)
        self.tbl_CreateMealPlan.showMaximized()
        connection.close()

    def createMealPlan(self, table):
        lookups = []
        self.breakfast_count()
        self.lunch_count()
        self.dinner_count()
        print("Breakfast: " + str(self.breakfast_count()))
        print("Lunches: " + str(self.lunch_count()))
        print("Dinners: " + str(self.dinner_count()))

        if self.breakfast_count() > 0:
            br_lookup = "SELECT * FROM tbl_menulist WHERE mealType='Breakfast' OR mealType='Breakfast/Dinner' ORDER BY RANDOM() LIMIT " + str(self.breakfast_count())
            lookups.append(br_lookup)

        if self.lunch_count() > 0:
            lu_lookup = "SELECT * FROM tbl_menulist WHERE (mealType='Lunch/Dinner' OR mealType='Lunch') ORDER BY RANDOM() LIMIT " + str(self.lunch_count())
            lookups.append(lu_lookup)

        if self.dinner_count() > 0:
            di_lookup = "SELECT * FROM tbl_menulist WHERE (mealType='Dinner' OR mealType='Breakfast/Dinner') ORDER BY RANDOM() LIMIT " + str(self.dinner_count())
            lookups.append(di_lookup)

        self.createMealPlanTable(lookups)

    def selectAllBreakfastChkBx(self):
        for br in self.grpBx_Breakfast.findChildren(QtWidgets.QCheckBox):
            br.setChecked(True)

    def selectAllLunchChkBx(self):
        for lu in self.grpBx_Lunch.findChildren(QtWidgets.QCheckBox):
            lu.setChecked(True)

    def selectAllDinnerChkBx(self):
        for di in self.grpBx_Dinner.findChildren(QtWidgets.QCheckBox):
            di.setChecked(True)

    def selectNoneBreakfastChkBx(self):
        for br in self.grpBx_Breakfast.findChildren(QtWidgets.QCheckBox):
            br.setChecked(False)

    def selectNoneLunchChkBx(self):
        for lu in self.grpBx_Lunch.findChildren(QtWidgets.QCheckBox):
            lu.setChecked(False)

    def selectNoneDinnerChkBx(self):
        for di in self.grpBx_Dinner.findChildren(QtWidgets.QCheckBox):
            di.setChecked(False)

    def checkAll(self):
        check_state = self.chkbx_All.checkState()
        if check_state == 2:
            for chk in self.grpBx_Multi.findChildren(QtWidgets.QCheckBox):
                chk.setChecked(True)
            self.checkAll_br()
            self.checkAll_lu()
            self.checkAll_di()
        else:
            for chk in self.grpBx_Multi.findChildren(QtWidgets.QCheckBox):
                chk.setChecked(False)
            self.checkAll_br()
            self.checkAll_lu()
            self.checkAll_di()

    def checkAll_br(self):
        check_state = self.chkbx_All_br.checkState()
        if check_state > 0:
            self.selectAllBreakfastChkBx()
        else:
            self.selectNoneBreakfastChkBx()

    def checkAll_lu(self):
        check_state = self.chkbx_All_lu.checkState()
        if check_state == 2:
            self.selectAllLunchChkBx()
        else:
            self.selectNoneLunchChkBx()

    def checkAll_di(self):
        check_state = self.chkbx_All_di.checkState()
        if check_state == 2:
            self.selectAllDinnerChkBx()
        else:
            self.selectNoneDinnerChkBx()

    def groceryList(self):
        # item = self.tbl_CreateMealPlan.horizontalHeaderItem(4).text()
        # print(item)
        count = self.tbl_CreateMealPlan.rowCount()
        print(count)
        col = 4
        groceryList = []
        for row in range(count):
            item = self.tbl_CreateMealPlan.item(row, col)
            item = item.text()
            # print(item)
            mealList = re.split(r'[,/]', item)
            for item in mealList:
                item = item.strip()
                item = item.capitalize()
                groceryList.append(item)
        # print(groceryList)

            # groceries = item.text()
            # print(groceries)
        groceryList = list(filter(None, groceryList))
        groceryItem = ''
        print(groceryList)
        for l in groceryList:
            groceryItem += str(l) + '\n'
            # print(item)
            self.groceries.setText(groceryItem)

    def setupUi(self, win_MealPlanner):
        app_window_color = "background-color: #DCE4F2;"
        create_meal_tab_bg_color = "background-color: #ADD4F7;"
        edit_meal_tab_bg_color = ("background-color: #99AAFF")
        default_btn_color = ()
        add_btn_color = ()
        delete_btn_color = ()
        create_meal_btn_color = ()
        lbl_font_style = "color: #2B0799; font-weight: bold; font-size: 14px;"

        MAX_HEIGHT = (16, 16)
        font = QtGui.QFont("Helvetica", 13)
        chk_bx_style = ("QCheckBox::indicator { width:26px; height: 26px; }"
                        "QCheckBox::indicator:unchecked {image: url(imgs/icons8-unchecked-checkbox-50.png);}"
                        "QCheckBox::indicator:checked {image: url(imgs/icons8-checked-checkbox-50.png);}")
        chk_bx_width = 26
        chk_bx_height = 26

        br_chk_bx_x_loc = 43
        lu_chk_bx_horz_loc = 18
        di_chk_bx_horz_loc = 22

        Mon_chkBx_Vert_Loc = 23
        Tue_chkBx_Vert_Loc = 58
        Wed_chkBx_Vert_Loc = 97
        Thu_chkBx_Vert_Loc = 136
        Fri_chkBx_Vert_Loc = 172
        Sat_chkBx_Vert_Loc = 211
        Sun_chkBx_Vert_Loc = 250

        win_MealPlanner.setObjectName("win_MealPlanner")
        win_MealPlanner.setEnabled(True)
        win_MealPlanner.resize(1080, 810)
        # win_MealPlanner.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        # win_MealPlanner.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.centralwidget = QtWidgets.QWidget(win_MealPlanner)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1060, 780))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        # Meal plan configuration
        self.tab_MealPlan = QtWidgets.QWidget()
        self.tab_MealPlan.setStyleSheet(app_window_color + "; color: blue")
        self.tab_MealPlan.setObjectName("tab_MealPlan")

        self.frm_Planner = QtWidgets.QFrame(self.tab_MealPlan)
        self.frm_Planner.setGeometry(QtCore.QRect(10, 10, 1035, 320))
        self.frm_Planner.setStyleSheet(create_meal_tab_bg_color)
        self.frm_Planner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_Planner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_Planner.setObjectName("frm_Planner")
        
        # Breakfast group box configuration
        self.grpBx_Breakfast = QtWidgets.QGroupBox(self.frm_Planner)
        self.grpBx_Breakfast.setGeometry(QtCore.QRect(170, 13, 111, 288))
        self.grpBx_Breakfast.setToolTipDuration(-3)
        self.grpBx_Breakfast.setStyleSheet(lbl_font_style)
        self.grpBx_Breakfast.setAlignment(QtCore.Qt.AlignCenter)
        self.grpBx_Breakfast.setFlat(False)
        self.grpBx_Breakfast.setCheckable(False)
        self.grpBx_Breakfast.setChecked(False)
        self.grpBx_Breakfast.setObjectName("grpBx_Breakfast")

        # Breakfast checkmark configuration
        self.chkbx_Mon_Br = QtWidgets.QCheckBox(self.grpBx_Breakfast)
        self.chkbx_Mon_Br.setFont(font)
        self.chkbx_Mon_Br.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Mon_Br.setStyleSheet(chk_bx_style)
        self.chkbx_Mon_Br.setText("")
        self.chkbx_Mon_Br.setGeometry(br_chk_bx_x_loc, Mon_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Mon_Br.setObjectName("chkbx_Mon_Br")
        self.chkbx_Tue_Br = QtWidgets.QCheckBox(self.grpBx_Breakfast)
        self.chkbx_Tue_Br.setFont(font)
        self.chkbx_Tue_Br.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Tue_Br.setText("")
        self.chkbx_Tue_Br.setGeometry(br_chk_bx_x_loc, Tue_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Tue_Br.setObjectName("chkbx_Tue_Br")
        self.chkbx_Tue_Br.setStyleSheet(chk_bx_style)
        self.chkbx_Wed_Br = QtWidgets.QCheckBox(self.grpBx_Breakfast)
        self.chkbx_Wed_Br.setFont(font)
        self.chkbx_Wed_Br.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Wed_Br.setText("")
        self.chkbx_Wed_Br.setGeometry(br_chk_bx_x_loc, Wed_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Wed_Br.setObjectName("chkbx_Wed_Br")
        self.chkbx_Wed_Br.setStyleSheet(chk_bx_style)
        self.chkbx_Thu_Br = QtWidgets.QCheckBox(self.grpBx_Breakfast)
        self.chkbx_Thu_Br.setFont(font)
        self.chkbx_Thu_Br.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Thu_Br.setText("")
        self.chkbx_Thu_Br.setGeometry(br_chk_bx_x_loc, Thu_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Thu_Br.setObjectName("chkbx_Thu_Br")
        self.chkbx_Thu_Br.setStyleSheet(chk_bx_style)
        self.chkbx_Fri_Br = QtWidgets.QCheckBox(self.grpBx_Breakfast)
        self.chkbx_Fri_Br.setFont(font)
        self.chkbx_Fri_Br.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Fri_Br.setText("")
        self.chkbx_Fri_Br.setGeometry(br_chk_bx_x_loc, Fri_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Fri_Br.setObjectName("chkbx_Fri_Br")
        self.chkbx_Fri_Br.setStyleSheet(chk_bx_style)
        self.chkbx_Sat_Br = QtWidgets.QCheckBox(self.grpBx_Breakfast)
        self.chkbx_Sat_Br.setFont(font)
        self.chkbx_Sat_Br.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Sat_Br.setText("")
        self.chkbx_Sat_Br.setGeometry(br_chk_bx_x_loc, Sat_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Sat_Br.setObjectName("chkbx_Sat_Br")
        self.chkbx_Sat_Br.setStyleSheet(chk_bx_style)
        self.chkbx_Sun_Br = QtWidgets.QCheckBox(self.grpBx_Breakfast)
        self.chkbx_Sun_Br.setFont(font)
        self.chkbx_Sun_Br.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Sun_Br.setText("")
        self.chkbx_Sun_Br.setGeometry(br_chk_bx_x_loc, Sun_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Sun_Br.setObjectName("chkbx_Sun_Br")
        self.chkbx_Sun_Br.setStyleSheet(chk_bx_style)

        # Lunch group box configuration
        self.grpBx_Lunch = QtWidgets.QGroupBox(self.frm_Planner)
        self.grpBx_Lunch.setGeometry(QtCore.QRect(280, 13, 61, 288))
        self.grpBx_Lunch.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBx_Lunch.setStyleSheet(lbl_font_style)
        self.grpBx_Lunch.setAlignment(QtCore.Qt.AlignCenter)
        self.grpBx_Lunch.setFlat(False)
        self.grpBx_Lunch.setCheckable(False)
        self.grpBx_Lunch.setObjectName("grpBx_Lunch")

        # Lunch check mark configuration
        self.chkbx_Mon_Lu = QtWidgets.QCheckBox(self.grpBx_Lunch)
        self.chkbx_Mon_Lu.setFont(font)
        self.chkbx_Mon_Lu.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Mon_Lu.setStyleSheet(chk_bx_style)
        self.chkbx_Mon_Lu.setText("")
        self.chkbx_Mon_Lu.setGeometry(lu_chk_bx_horz_loc, Mon_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Mon_Lu.setObjectName("chkbx_Mon_Lu")
        self.chkbx_Tue_Lu = QtWidgets.QCheckBox(self.grpBx_Lunch)
        self.chkbx_Tue_Lu.setFont(font)
        self.chkbx_Tue_Lu.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Tue_Lu.setStyleSheet(chk_bx_style)
        self.chkbx_Tue_Lu.setText("")
        self.chkbx_Tue_Lu.setGeometry(lu_chk_bx_horz_loc, Tue_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Tue_Lu.setObjectName("chkbx_Tue_Lu")
        self.chkbx_Wed_Lu = QtWidgets.QCheckBox(self.grpBx_Lunch)
        self.chkbx_Wed_Lu.setFont(font)
        self.chkbx_Wed_Lu.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Wed_Lu.setStyleSheet(chk_bx_style)
        self.chkbx_Wed_Lu.setText("")
        self.chkbx_Wed_Lu.setGeometry(lu_chk_bx_horz_loc, Wed_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Wed_Lu.setObjectName("chkbx_Wed_Lu")
        self.chkbx_Thu_Lu = QtWidgets.QCheckBox(self.grpBx_Lunch)
        self.chkbx_Thu_Lu.setFont(font)
        self.chkbx_Thu_Lu.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Thu_Lu.setStyleSheet(chk_bx_style)
        self.chkbx_Thu_Lu.setText("")
        self.chkbx_Thu_Lu.setGeometry(lu_chk_bx_horz_loc, Thu_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Thu_Lu.setObjectName("chkbx_Thu_Lu")
        self.chkbx_Fri_Lu = QtWidgets.QCheckBox(self.grpBx_Lunch)
        self.chkbx_Fri_Lu.setFont(font)
        self.chkbx_Fri_Lu.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Fri_Lu.setStyleSheet(chk_bx_style)
        self.chkbx_Fri_Lu.setText("")
        self.chkbx_Fri_Lu.setGeometry(lu_chk_bx_horz_loc, Fri_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Fri_Lu.setObjectName("chkbx_Fri_Lu")
        self.chkbx_Sat_Lu = QtWidgets.QCheckBox(self.grpBx_Lunch)
        self.chkbx_Sat_Lu.setFont(font)
        self.chkbx_Sat_Lu.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Sat_Lu.setStyleSheet(chk_bx_style)
        self.chkbx_Sat_Lu.setText("")
        self.chkbx_Sat_Lu.setGeometry(lu_chk_bx_horz_loc, Sat_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Sat_Lu.setObjectName("chkbx_Sat_Lu")
        self.chkbx_Sun_Lu = QtWidgets.QCheckBox(self.grpBx_Lunch)
        self.chkbx_Sun_Lu.setFont(font)
        self.chkbx_Sun_Lu.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Sun_Lu.setStyleSheet(chk_bx_style)
        self.chkbx_Sun_Lu.setText("")
        self.chkbx_Sun_Lu.setGeometry(lu_chk_bx_horz_loc, Sun_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Sun_Lu.setObjectName("chkbx_Sun_Lu")

        # Dinner group box configuration
        self.grpBx_Dinner = QtWidgets.QGroupBox(self.frm_Planner)
        self.grpBx_Dinner.setGeometry(QtCore.QRect(340, 13, 71, 288))
        self.grpBx_Dinner.setStyleSheet(lbl_font_style)
        self.grpBx_Dinner.setAlignment(QtCore.Qt.AlignCenter)
        self.grpBx_Dinner.setFlat(False)
        self.grpBx_Dinner.setCheckable(False)
        self.grpBx_Dinner.setChecked(False)
        self.grpBx_Dinner.setObjectName("grpBx_Dinner")

        # Dinner checkmark configuration
        self.chkbx_Mon_Di = QtWidgets.QCheckBox(self.grpBx_Dinner)
        self.chkbx_Mon_Di.setEnabled(True)
        self.chkbx_Mon_Di.setFont(font)
        self.chkbx_Mon_Di.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Mon_Di.setStyleSheet(chk_bx_style)
        self.chkbx_Mon_Di.setText("")
        self.chkbx_Mon_Di.setGeometry(di_chk_bx_horz_loc, Mon_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Mon_Di.setTristate(False)
        self.chkbx_Mon_Di.setObjectName("chkbx_Mon_Di")
        self.chkbx_Tue_Di = QtWidgets.QCheckBox(self.grpBx_Dinner)
        self.chkbx_Tue_Di.setFont(font)
        self.chkbx_Tue_Di.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Tue_Di.setStyleSheet(chk_bx_style)
        self.chkbx_Tue_Di.setText("")
        self.chkbx_Tue_Di.setGeometry(di_chk_bx_horz_loc, Tue_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Tue_Di.setObjectName("chkbx_Tue_Di")
        self.chkbx_Wed_Di = QtWidgets.QCheckBox(self.grpBx_Dinner)
        self.chkbx_Wed_Di.setFont(font)
        self.chkbx_Wed_Di.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Wed_Di.setStyleSheet(chk_bx_style)
        self.chkbx_Wed_Di.setText("")
        self.chkbx_Wed_Di.setGeometry(di_chk_bx_horz_loc, Wed_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Wed_Di.setObjectName("chkbx_Wed_Di")
        self.chkbx_Thu_Di = QtWidgets.QCheckBox(self.grpBx_Dinner)
        self.chkbx_Thu_Di.setFont(font)
        self.chkbx_Thu_Di.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Thu_Di.setStyleSheet(chk_bx_style)
        self.chkbx_Thu_Di.setText("")
        self.chkbx_Thu_Di.setGeometry(di_chk_bx_horz_loc, Thu_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Thu_Di.setObjectName("chkbx_Thu_Di")
        self.chkbx_Fri_Di = QtWidgets.QCheckBox(self.grpBx_Dinner)
        self.chkbx_Fri_Di.setFont(font)
        self.chkbx_Fri_Di.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Fri_Di.setStyleSheet(chk_bx_style)
        self.chkbx_Fri_Di.setText("")
        self.chkbx_Fri_Di.setGeometry(di_chk_bx_horz_loc, Fri_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Fri_Di.setObjectName("chkbx_Fri_Di")
        self.chkbx_Sat_Di = QtWidgets.QCheckBox(self.grpBx_Dinner)
        self.chkbx_Sat_Di.setFont(font)
        self.chkbx_Sat_Di.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Sat_Di.setStyleSheet(chk_bx_style)
        self.chkbx_Sat_Di.setText("")
        self.chkbx_Sat_Di.setGeometry(di_chk_bx_horz_loc, Sat_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Sat_Di.setObjectName("chkbx_Sat_Di")
        self.chkbx_Sun_Di = QtWidgets.QCheckBox(self.grpBx_Dinner)
        self.chkbx_Sun_Di.setFont(font)
        self.chkbx_Sun_Di.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbx_Sun_Di.setStyleSheet(chk_bx_style)
        self.chkbx_Sun_Di.setText("")
        self.chkbx_Sun_Di.setGeometry(di_chk_bx_horz_loc, Sun_chkBx_Vert_Loc, chk_bx_width, chk_bx_height)
        self.chkbx_Sun_Di.setObjectName("chkbx_Sun_Di")

        # Multi-Checkbox group box configuration
        self.grpBx_Multi = QtWidgets.QGroupBox(self.frm_Planner)
        self.grpBx_Multi.setGeometry(QtCore.QRect(410, 21, 200, 280))
        self.grpBx_Multi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBx_Multi.setStyleSheet(lbl_font_style + "font-size: 14px")
        self.grpBx_Multi.setAlignment(QtCore.Qt.AlignCenter)
        self.grpBx_Multi.setFlat(False)
        self.grpBx_Multi.setCheckable(False)
        self.grpBx_Multi.setObjectName("grpBx_Multi")

        # Check All or None for Breakfast, Lunch and Dinner
        self.chkbx_All = QtWidgets.QCheckBox(self.grpBx_Multi)
        # self.chkbx_All.setFont(font)
        self.chkbx_All.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkbx_All.setStyleSheet("QCheckBox::indicator { width:26px; height: 26px; }"
                                        "QCheckBox::indicator:unchecked {image: url(imgs/icons8-uncheck-all-50.png);}"
                                        "QCheckBox::indicator:checked {image: url(imgs/icons8-check-all-50.png);}")
        self.chkbx_All.setText("Check All")
        self.chkbx_All.setGeometry(10, 10, 100, chk_bx_height)
        self.chkbx_All.setObjectName("chkbx_All")

        # Check All or None for Breakfast, Lunch and Dinner
        self.chkbx_All_br = QtWidgets.QCheckBox(self.grpBx_Multi)
        # self.chkbx_All_br.setFont(font)
        self.chkbx_All_br.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkbx_All_br.setStyleSheet("QCheckBox::indicator { width:26px; height: 26px; }"
                                        "QCheckBox::indicator:unchecked {image: url(imgs/icons8-uncheck-all-50.png);}"
                                        "QCheckBox::indicator:checked {image: url(imgs/icons8-check-all-50.png);}")
        self.chkbx_All_br.setText("Check All Breakfast")
        self.chkbx_All_br.setGeometry(15, 41, 175, chk_bx_height)
        self.chkbx_All_br.setObjectName("chkbx_All_br")

        self.chkbx_All_lu = QtWidgets.QCheckBox(self.grpBx_Multi)
        # self.chkbx_All_lu.setFont(font)
        self.chkbx_All_lu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkbx_All_lu.setStyleSheet("QCheckBox::indicator { width:26px; height: 26px; }"
                                        "QCheckBox::indicator:unchecked {image: url(imgs/icons8-uncheck-all-50.png);}"
                                        "QCheckBox::indicator:checked {image: url(imgs/icons8-check-all-50.png);}")
        self.chkbx_All_lu.setText("Check All Lunch")
        self.chkbx_All_lu.setGeometry(15, 70, 175, chk_bx_height)
        self.chkbx_All_lu.setObjectName("chkbx_All_lu")

        # Check All or None for Dinner
        self.chkbx_All_di = QtWidgets.QCheckBox(self.grpBx_Multi)
        # self.chkbx_All_di.setFont(font)
        self.chkbx_All_di.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkbx_All_di.setStyleSheet("QCheckBox::indicator { width:26px; height: 26px; }"
                                        "QCheckBox::indicator:unchecked {image: url(imgs/icons8-uncheck-all-50.png);}"
                                        "QCheckBox::indicator:checked {image: url(imgs/icons8-check-all-50.png);}")
        self.chkbx_All_di.setText("Check All Dinner")
        self.chkbx_All_di.setGeometry(15, 99, 175, chk_bx_height)
        self.chkbx_All_di.setObjectName("chkbx_All_di")

        # Days of week group box
        self.grpBx_DaysOfWeek = QtWidgets.QGroupBox(self.frm_Planner)
        self.grpBx_DaysOfWeek.setEnabled(True)
        self.grpBx_DaysOfWeek.setGeometry(QtCore.QRect(21, 21, 150, 280))
        self.grpBx_DaysOfWeek.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBx_DaysOfWeek.setStyleSheet(lbl_font_style + "font-size: 20px")
        self.grpBx_DaysOfWeek.setTitle("")
        self.grpBx_DaysOfWeek.setAlignment(QtCore.Qt.AlignLeft)
        self.grpBx_DaysOfWeek.setFlat(False)
        self.grpBx_DaysOfWeek.setObjectName("grpBx_DaysOfWeek")

        # Days of week label configuration
        self.lbl_Tue = QtWidgets.QLabel(self.grpBx_DaysOfWeek)
        self.lbl_Tue.setGeometry(QtCore.QRect(10, 49, 130, 31))
        self.lbl_Tue.setFont(font)
        self.lbl_Tue.setObjectName("lbl_Tue")
        self.lbl_Wed = QtWidgets.QLabel(self.grpBx_DaysOfWeek)
        self.lbl_Wed.setGeometry(QtCore.QRect(10, 88, 130, 31))
        self.lbl_Wed.setFont(font)
        self.lbl_Wed.setObjectName("lbl_Wed")
        self.lbl_Mon = QtWidgets.QLabel(self.grpBx_DaysOfWeek)
        self.lbl_Mon.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.lbl_Mon.setFont(font)
        self.lbl_Mon.setObjectName("lbl_Mon")
        self.lbl_Thu = QtWidgets.QLabel(self.grpBx_DaysOfWeek)
        self.lbl_Thu.setGeometry(QtCore.QRect(10, 126, 111, 31))
        self.lbl_Thu.setFont(font)
        self.lbl_Thu.setObjectName("lbl_Thu")
        self.lbl_Fri = QtWidgets.QLabel(self.grpBx_DaysOfWeek)
        self.lbl_Fri.setGeometry(QtCore.QRect(10, 161, 111, 31))
        self.lbl_Fri.setFont(font)
        self.lbl_Fri.setObjectName("lbl_Fri")
        self.lbl_Sat = QtWidgets.QLabel(self.grpBx_DaysOfWeek)
        self.lbl_Sat.setGeometry(QtCore.QRect(10, 200, 111, 31))
        self.lbl_Sat.setFont(font)
        self.lbl_Sat.setObjectName("lbl_Sat")
        self.lbl_Sun = QtWidgets.QLabel(self.grpBx_DaysOfWeek)
        self.lbl_Sun.setGeometry(QtCore.QRect(10, 240, 111, 31))
        self.lbl_Sun.setFont(font)
        self.lbl_Sun.setObjectName("lbl_Sun")

        self.tbl_CreateMealPlan = QtWidgets.QTableWidget(self.tab_MealPlan)
        self.tbl_CreateMealPlan.setGeometry(QtCore.QRect(10, 340, 1035, 405))
        self.tbl_CreateMealPlan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tbl_CreateMealPlan.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tbl_CreateMealPlan.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_CreateMealPlan.setTabKeyNavigation(False)
        self.tbl_CreateMealPlan.setProperty("showDropIndicator", False)
        self.tbl_CreateMealPlan.setDragDropOverwriteMode(False)
        self.tbl_CreateMealPlan.setShowGrid(True)
        self.tbl_CreateMealPlan.setWordWrap(True)
        self.tbl_CreateMealPlan.setObjectName("tbl_CreateMealPlan")
        self.tbl_CreateMealPlan.setStyleSheet("font-size: 16px; color: black; font-family: calibri;")
        self.tbl_CreateMealPlan.horizontalHeader().setCascadingSectionResizes(True)
        self.tbl_CreateMealPlan.verticalHeader().setCascadingSectionResizes(True)

        self.btn_CreateMealPlan = QtWidgets.QPushButton(self.grpBx_Multi)
        self.btn_CreateMealPlan.setGeometry(QtCore.QRect(10, 160, 180, 41))
        self.btn_CreateMealPlan.setObjectName("btn_CreateMealPlan")

        self.btn_SaveMealPlan = QtWidgets.QPushButton(self.grpBx_Multi)
        self.btn_SaveMealPlan.setGeometry(QtCore.QRect(10, 211, 180, 41))
        self.btn_SaveMealPlan.setObjectName("btn_SaveMealPlan")

        self.groceries = QtWidgets.QTextBrowser(self.frm_Planner)
        self.groceries.setGeometry(QtCore.QRect(610, 21, 405, 280))
        self.groceries.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.groceries.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.groceries.setStyleSheet("font-size: 16px; color: black;")
        
        

        # Edit Meal List Tab Configuration
        self.tabWidget.addTab(self.tab_MealPlan, "")
        self.tab_Edit = QtWidgets.QWidget()
        self.tab_Edit.setObjectName("tab_Edit")
        self.tab_Edit.setStyleSheet(edit_meal_tab_bg_color)
        self.tabWidget.setCurrentIndex(1)
        # self.lbl_MealType = QtWidgets.QLabel(self.tab_Edit)
        # self.lbl_MealType.setGeometry(QtCore.QRect(10, 10, 110, 30))
        # self.lbl_MealType.setFont(font)
        # self.lbl_MealType.setObjectName("lbl_MealType")
        self.cmbBx_MealType = QtWidgets.QComboBox(self.tab_Edit)
        self.cmbBx_MealType.setGeometry(QtCore.QRect(10, 35, 200, 30))
        self.cmbBx_MealType.setFont(font)
        self.cmbBx_MealType.setObjectName("cmbBx_MealType")
        self.cmbBx_MealType.addItem("Select Meal Type")
        self.cmbBx_MealType.addItem("Breakfast")
        self.cmbBx_MealType.addItem("Breakfast/Dinner")
        self.cmbBx_MealType.addItem("Lunch")
        self.cmbBx_MealType.addItem("Lunch/Dinner")
        self.cmbBx_MealType.addItem("Dinner")
        # self.lbl_mealName = QtWidgets.QLabel(self.tab_Edit)
        # self.lbl_mealName.setGeometry(QtCore.QRect(220, 10, 110, 30))
        # self.lbl_mealName.setFont(font)
        # self.lbl_mealName.setObjectName("lbl_mealName")
        self.txtbox_mealName = QtWidgets.QLineEdit(self.tab_Edit)
        self.txtbox_mealName.setGeometry(QtCore.QRect(220, 35, 200, 30))
        self.txtbox_mealName.setFont(font)
        self.txtbox_mealName.setPlaceholderText(" Enter Meal Name")
        self.txtbox_mealName.setObjectName("txtbox_mealName")
        # self.lbl_recipe = QtWidgets.QLabel(self.tab_Edit)
        # self.lbl_recipe.setGeometry(QtCore.QRect(670, 10, 110, 40))
        # self.lbl_recipe.setFont(font)
        # self.lbl_recipe.setObjectName("lbl_recipe")
        self.txtbox_recipe = QtWidgets.QLineEdit(self.tab_Edit)
        self.txtbox_recipe.setGeometry(QtCore.QRect(740, 35, 300, 30))
        self.txtbox_recipe.setFont(font)
        self.txtbox_recipe.setPlaceholderText(" Recipe / Special notes")
        self.txtbox_recipe.setObjectName("txtbox_recipe")
        # self.lbl_GroceryList = QtWidgets.QLabel(self.tab_Edit)
        # self.lbl_GroceryList.setGeometry(QtCore.QRect(1000, 10, 110, 30))
        # self.lbl_GroceryList.setFont(font)
        # self.lbl_GroceryList.setObjectName("lbl_GroceryList")
        self.txtbox_GroceryList = QtWidgets.QLineEdit(self.tab_Edit)
        self.txtbox_GroceryList.setGeometry(QtCore.QRect(430, 35, 300, 30))
        self.txtbox_GroceryList.setFont(font)
        self.txtbox_GroceryList.setPlaceholderText(" Enter items to make meal")
        self.txtbox_GroceryList.setObjectName("txtbox_GroceryList")

        self.tab_Edit.setTabOrder(self.cmbBx_MealType, self.txtbox_mealName)
        self.tab_Edit.setTabOrder(self.txtbox_mealName, self.txtbox_GroceryList)
        self.tab_Edit.setTabOrder(self.txtbox_GroceryList, self.txtbox_recipe)
        



        self.btn_add_meal = QtWidgets.QPushButton(self.tab_Edit)
        self.btn_add_meal.setGeometry(QtCore.QRect(10, 75, 160, 50))
        self.btn_add_meal.setFont(font)
        self.btn_add_meal.setStyleSheet("background-color: #28AB00; color: white;")
        self.btn_add_meal.setIcon(QtGui.QIcon("imgs/add_bw.png"))
        self.btn_add_meal.setIconSize(QtCore.QSize(50, 50))
        self.btn_add_meal.setObjectName("btn_add_meal")

        self.btn_LoadEditTable = QtWidgets.QPushButton(self.tab_Edit)
        self.btn_LoadEditTable.setGeometry(QtCore.QRect(180, 75, 160, 50))
        self.btn_LoadEditTable.setFont(font)
        self.btn_LoadEditTable.setStyleSheet("background-color: #74b9ff;\n"
                                          "color: white;")
        self.btn_LoadEditTable.setIcon(QtGui.QIcon("imgs/refresh_bw.png"))
        self.btn_LoadEditTable.setIconSize(QtCore.QSize(50, 50))
        self.btn_LoadEditTable.setObjectName("btn_LoadEditTable")

        self.btn_DeleteEdit = QtWidgets.QPushButton(self.tab_Edit)
        self.btn_DeleteEdit.setGeometry(QtCore.QRect(820, 75, 220, 50))
        self.btn_DeleteEdit.setFont(font)
        self.btn_DeleteEdit.setAutoFillBackground(False)
        self.btn_DeleteEdit.setStyleSheet("background-color: rgb(205, 0, 0);\n"
                                          "color: white;")
        self.btn_DeleteEdit.setIcon(QtGui.QIcon("imgs/trashcan_bw.png"))
        self.btn_DeleteEdit.setIconSize(QtCore.QSize(50, 50))
        self.btn_DeleteEdit.setObjectName("btn_DeleteEdit")

        self.tbl_Edit = QtWidgets.QTableWidget(self.tab_Edit)
        self.tbl_Edit.setGeometry(QtCore.QRect(10, 135, 1030, 610))
        self.tbl_Edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tbl_Edit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        #self.tbl_Edit.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_Edit.setStyleSheet("background-color: white; font-size: 16px; color: black; font-family: calibri;")
        self.tbl_Edit.setAlternatingRowColors(True)
        self.tbl_Edit.setShowGrid(True)
        self.tbl_Edit.setCornerButtonEnabled(False)
        self.tbl_Edit.setObjectName("tbl_Edit")
        self.tbl_Edit.setColumnCount(0)
        self.tbl_Edit.setRowCount(0)
        self.tbl_Edit.verticalHeader().setVisible(False)


        # Edit tab configuration
        self.lbl_EditHeading = QtWidgets.QLabel(self.tab_Edit)
        self.lbl_EditHeading.setGeometry(QtCore.QRect(10, 10, 311, 21))
        self.lbl_EditHeading.setFont(font)
        self.lbl_EditHeading.setObjectName("lbl_EditHeading")
        self.lbl_EditHeading.setStyleSheet("color: White;")
        # self.lbl_Heading_2 = QtWidgets.QLabel(self.tab_Edit)
        # self.lbl_Heading_2.setGeometry(QtCore.QRect(10, 10, 311, 21))
        # self.lbl_Heading_2.setFont(font)
        # self.lbl_Heading_2.setObjectName("lbl_Heading_2")
        self.tabWidget.addTab(self.tab_Edit, "")

        win_MealPlanner.setCentralWidget(self.centralwidget)

        # Status Bar configuration
        self.statusbar = QtWidgets.QStatusBar(win_MealPlanner)
        self.statusbar.setObjectName("statusbar")
        win_MealPlanner.setStatusBar(self.statusbar)
        self.statusbar.setSizeGripEnabled(False)

        # Menu bar configuration
        self.actionNew = QtWidgets.QAction(win_MealPlanner)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(win_MealPlanner)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(win_MealPlanner)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(win_MealPlanner)
        self.actionPaste.setObjectName("actionPaste")

        self.retranslateUi(win_MealPlanner)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.blockSignals(False)
        self.tabWidget.currentChanged.connect(self.onChange)
        
    def onChange(self, i):
        # QMessageBox.information(self, "Tab Index Changed!", "Current Tab Index: %d" % i)
        self.loadEditTable()


        
        QtCore.QMetaObject.connectSlotsByName(win_MealPlanner)

        self.btn_LoadEditTable.clicked.connect(self.loadEditTable)
        self.chkbx_All.clicked.connect(self.checkAll)
        # self.chkbx_All.clicked.connect(self.selectNone)
        self.btn_CreateMealPlan.clicked.connect(self.createMealPlan)
        self.btn_add_meal.clicked.connect(self.mealToAdd)
        self.btn_DeleteEdit.clicked.connect(self.deleteMeal)
        self.chkbx_All_lu.clicked.connect(self.checkAll_lu)
        self.chkbx_All_br.clicked.connect(self.checkAll_br)
        self.chkbx_All_di.clicked.connect(self.checkAll_di)
        self.btn_SaveMealPlan.clicked.connect(self.groceryList)
        # self.cmbBx_MealType.returnPressed.connect(self.mealToAdd)
        self.txtbox_GroceryList.returnPressed.connect(self.mealToAdd)
        self.txtbox_mealName.returnPressed.connect(self.mealToAdd)
        self.txtbox_recipe.returnPressed.connect(self.mealToAdd)
        # self.tab_Edit.connect(self.loadEditTable)

    def retranslateUi(self, win_MealPlanner):
        _translate = QtCore.QCoreApplication.translate
        win_MealPlanner.setWindowTitle(_translate("win_MealPlanner", "Meal Planner"))
        self.grpBx_Breakfast.setTitle(_translate("win_MealPlanner", "Breakfast"))
        self.grpBx_Lunch.setTitle(_translate("win_MealPlanner", "Lunch"))
        self.grpBx_Dinner.setTitle(_translate("win_MealPlanner", "Dinner"))
        self.lbl_Tue.setText(_translate("win_MealPlanner", "Tuesday"))
        self.lbl_Wed.setText(_translate("win_MealPlanner", "Wednesday"))
        self.lbl_Mon.setText(_translate("win_MealPlanner", "Monday"))
        self.lbl_Thu.setText(_translate("win_MealPlanner", "Thursday"))
        self.lbl_Fri.setText(_translate("win_MealPlanner", "Friday"))
        self.lbl_Sat.setText(_translate("win_MealPlanner", "Saturday"))
        self.lbl_Sun.setText(_translate("win_MealPlanner", "Sunday"))
        # self.btn_SelectAll.setText(_translate("win_MealPlanner", "Select All"))
        # self.btn_SelectNone.setText(_translate("win_MealPlanner", "Select None"))
        self.btn_CreateMealPlan.setText(_translate("win_MealPlanner", "Create Meal Plan"))
        self.btn_SaveMealPlan.setText(_translate("win_MealPlanner", "Save Meal Plan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_MealPlan), _translate("win_MealPlanner", "Create Meal Plan"))
        self.btn_add_meal.setText(_translate("win_MealPlanner", "  Add Meal"))
        self.tbl_Edit.setSortingEnabled(False)
        self.lbl_EditHeading.setText(_translate("win_MealPlanner", "Enter new meals into database:"))
        # self.lbl_MealType.setText(_translate("win_MealPlanner", "Meal Type:"))
        # self.lbl_Entree.setText(_translate("win_MealPlanner", "Entree:"))
        # self.lbl_Components.setText(_translate("win_MealPlanner", "Components:"))
        # self.lbl_SideItems.setText(_translate("win_MealPlanner", "Side Items:"))
        # self.lbl_GroceryList.setText(_translate("win_MealPlanner", "Grocery List:"))
        # self.lbl_Condiments.setText(_translate("win_MealPlanner", "Condiments:"))
        # self.lbl_Heading_2.setText(_translate("win_MealPlanner", "Meal List:"))
        self.btn_DeleteEdit.setText(_translate("win_MealPlanner", "  Delete Selected Meal"))
        self.btn_LoadEditTable.setText(_translate("win_MealPlanner", "  Get Meal List"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Edit), _translate("win_MealPlanner", "Edit Meal List"))
        self.actionNew.setText(_translate("win_MealPlanner", "New"))
        self.actionNew.setStatusTip(_translate("win_MealPlanner", "Create a new file"))
        self.actionNew.setShortcut(_translate("win_MealPlanner", "Ctrl+N"))
        self.actionSave.setText(_translate("win_MealPlanner", "Save"))
        self.actionSave.setStatusTip(_translate("win_MealPlanner", "Save the current file"))
        self.actionSave.setShortcut(_translate("win_MealPlanner", "Ctrl+S"))
        self.actionCopy.setText(_translate("win_MealPlanner", "Copy"))
        self.actionCopy.setStatusTip(_translate("win_MealPlanner", "Copy selected text"))
        self.actionCopy.setShortcut(_translate("win_MealPlanner", "Ctrl+C"))
        self.actionPaste.setText(_translate("win_MealPlanner", "Paste"))
        self.actionPaste.setStatusTip(_translate("win_MealPlanner", "Paste copied text"))
        self.actionPaste.setShortcut(_translate("win_MealPlanner", "Ctrl+V"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win_MealPlanner = QtWidgets.QMainWindow()
    ui = Ui_win_MealPlanner()
    ui.setupUi(win_MealPlanner)

    # win_MealPlanner.setFont(font)
    win_MealPlanner.show()
    win_MealPlanner.setFixedSize(1080, 810)
    sys.exit(app.exec_())
