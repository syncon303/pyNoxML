# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'noxML.ui'
#
# Created: Mon Apr 02 23:40:22 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(610, 454)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(610, 454))
        MainWindow.setMaximumSize(QtCore.QSize(610, 454))
        MainWindow.setAcceptDrops(True)
        MainWindow.setAnimated(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(610, 454))
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.grp_props = QtGui.QGroupBox(self.centralwidget)
        self.grp_props.setGeometry(QtCore.QRect(315, 70, 291, 296))
        self.grp_props.setObjectName(_fromUtf8("grp_props"))
        self.gridLayoutWidget = QtGui.QWidget(self.grp_props)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 55, 281, 191))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 4, 1, 1)
        self.e_loop_min = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_loop_min.setMaximumSize(QtCore.QSize(40, 30))
        self.e_loop_min.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.e_loop_min.setObjectName(_fromUtf8("e_loop_min"))
        self.gridLayout.addWidget(self.e_loop_min, 3, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.rd_loop_no = QtGui.QRadioButton(self.gridLayoutWidget)
        self.rd_loop_no.setChecked(True)
        self.rd_loop_no.setObjectName(_fromUtf8("rd_loop_no"))
        self.bgrp_macro_mode = QtGui.QButtonGroup(MainWindow)
        self.bgrp_macro_mode.setObjectName(_fromUtf8("bgrp_macro_mode"))
        self.bgrp_macro_mode.addButton(self.rd_loop_no)
        self.gridLayout.addWidget(self.rd_loop_no, 1, 0, 1, 1)
        self.rd_loop_till_stop = QtGui.QRadioButton(self.gridLayoutWidget)
        self.rd_loop_till_stop.setObjectName(_fromUtf8("rd_loop_till_stop"))
        self.bgrp_macro_mode.addButton(self.rd_loop_till_stop)
        self.gridLayout.addWidget(self.rd_loop_till_stop, 2, 0, 1, 7)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 4, 1, 1)
        self.rd_loop_time = QtGui.QRadioButton(self.gridLayoutWidget)
        self.rd_loop_time.setMaximumSize(QtCore.QSize(50, 16777215))
        self.rd_loop_time.setObjectName(_fromUtf8("rd_loop_time"))
        self.bgrp_macro_mode.addButton(self.rd_loop_time)
        self.gridLayout.addWidget(self.rd_loop_time, 3, 0, 1, 1)
        self.e_loop_sec = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_loop_sec.setMaximumSize(QtCore.QSize(40, 30))
        self.e_loop_sec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.e_loop_sec.setObjectName(_fromUtf8("e_loop_sec"))
        self.gridLayout.addWidget(self.e_loop_sec, 3, 5, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 6, 1, 1)
        self.e_loop_count = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_loop_count.setMaximumSize(QtCore.QSize(40, 16777215))
        self.e_loop_count.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.e_loop_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.e_loop_count.setObjectName(_fromUtf8("e_loop_count"))
        self.gridLayout.addWidget(self.e_loop_count, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.e_macro_name = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_macro_name.setPlaceholderText(_fromUtf8(""))
        self.e_macro_name.setObjectName(_fromUtf8("e_macro_name"))
        self.gridLayout.addWidget(self.e_macro_name, 0, 1, 1, 6)
        self.e_loop_hr = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_loop_hr.setMaximumSize(QtCore.QSize(40, 30))
        self.e_loop_hr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.e_loop_hr.setObjectName(_fromUtf8("e_loop_hr"))
        self.gridLayout.addWidget(self.e_loop_hr, 3, 1, 1, 1)
        self.e_loop_interval = QtGui.QLineEdit(self.gridLayoutWidget)
        self.e_loop_interval.setMaximumSize(QtCore.QSize(40, 16777215))
        self.e_loop_interval.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.e_loop_interval.setObjectName(_fromUtf8("e_loop_interval"))
        self.gridLayout.addWidget(self.e_loop_interval, 4, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 2)
        self.lbl_slider_value = QtGui.QLabel(self.gridLayoutWidget)
        self.lbl_slider_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_slider_value.setObjectName(_fromUtf8("lbl_slider_value"))
        self.gridLayout.addWidget(self.lbl_slider_value, 5, 2, 1, 1)
        self.hslid_accel = QtGui.QSlider(self.gridLayoutWidget)
        self.hslid_accel.setMaximumSize(QtCore.QSize(16777215, 22))
        self.hslid_accel.setMinimum(1)
        self.hslid_accel.setMaximum(8)
        self.hslid_accel.setOrientation(QtCore.Qt.Horizontal)
        self.hslid_accel.setTickPosition(QtGui.QSlider.TicksBelow)
        self.hslid_accel.setTickInterval(1)
        self.hslid_accel.setObjectName(_fromUtf8("hslid_accel"))
        self.gridLayout.addWidget(self.hslid_accel, 5, 3, 1, 4)
        self.horizontalLayoutWidget = QtGui.QWidget(self.grp_props)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 260, 281, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_prop_save = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_prop_save.setObjectName(_fromUtf8("btn_prop_save"))
        self.horizontalLayout.addWidget(self.btn_prop_save)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_prop_rst = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_prop_rst.setObjectName(_fromUtf8("btn_prop_rst"))
        self.horizontalLayout.addWidget(self.btn_prop_rst)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.grp_props)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(5, 20, 281, 31))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.btn_edit_macro = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_edit_macro.setMaximumSize(QtCore.QSize(75, 23))
        self.btn_edit_macro.setObjectName(_fromUtf8("btn_edit_macro"))
        self.horizontalLayout_4.addWidget(self.btn_edit_macro)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(89, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(4, 1)
        self.btn_edit_macro_2 = QtGui.QPushButton(self.grp_props)
        self.btn_edit_macro_2.setGeometry(QtCore.QRect(215, 180, 75, 23))
        self.btn_edit_macro_2.setObjectName(_fromUtf8("btn_edit_macro_2"))
        self.list_macros = TestListWidget(self.centralwidget)
        self.list_macros.setGeometry(QtCore.QRect(0, 0, 311, 451))
        self.list_macros.setMouseTracking(False)
        self.list_macros.setAcceptDrops(True)
        self.list_macros.setDragEnabled(True)
        self.list_macros.setDragDropOverwriteMode(True)
        self.list_macros.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.list_macros.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.list_macros.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.list_macros.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.list_macros.setObjectName(_fromUtf8("list_macros"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(320, 410, 281, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.chk_backup = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.chk_backup.setChecked(True)
        self.chk_backup.setObjectName(_fromUtf8("chk_backup"))
        self.horizontalLayout_2.addWidget(self.chk_backup)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.btn_nox_save = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_nox_save.setObjectName(_fromUtf8("btn_nox_save"))
        self.horizontalLayout_2.addWidget(self.btn_nox_save)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.group_new_item = QtGui.QGroupBox(self.centralwidget)
        self.group_new_item.setGeometry(QtCore.QRect(315, 0, 291, 66))
        self.group_new_item.setObjectName(_fromUtf8("group_new_item"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.group_new_item)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(5, 20, 281, 31))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.btn_new_macro = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_new_macro.setMaximumSize(QtCore.QSize(75, 23))
        self.btn_new_macro.setObjectName(_fromUtf8("btn_new_macro"))
        self.horizontalLayout_3.addWidget(self.btn_new_macro)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.btn_import_file = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_import_file.setMaximumSize(QtCore.QSize(89, 23))
        self.btn_import_file.setObjectName(_fromUtf8("btn_import_file"))
        self.horizontalLayout_3.addWidget(self.btn_import_file)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(4, 1)
        self.horizontalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(170, 705, 160, 80))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_7.setBuddy(self.e_loop_interval)
        self.label_3.setBuddy(self.e_loop_count)
        self.label_4.setBuddy(self.e_loop_min)
        self.label_5.setBuddy(self.e_loop_sec)
        self.label_6.setBuddy(self.e_loop_interval)
        self.label_2.setBuddy(self.e_loop_hr)
        self.label_8.setBuddy(self.hslid_accel)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.e_loop_hr, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.rd_loop_time.click)
        QtCore.QObject.connect(self.e_loop_count, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.rd_loop_no.click)
        QtCore.QObject.connect(self.e_loop_min, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.rd_loop_time.click)
        QtCore.QObject.connect(self.e_loop_sec, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.rd_loop_time.click)
        QtCore.QObject.connect(self.hslid_accel, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lbl_slider_value.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_nox_save, self.e_macro_name)
        MainWindow.setTabOrder(self.e_macro_name, self.rd_loop_no)
        MainWindow.setTabOrder(self.rd_loop_no, self.e_loop_count)
        MainWindow.setTabOrder(self.e_loop_count, self.rd_loop_till_stop)
        MainWindow.setTabOrder(self.rd_loop_till_stop, self.rd_loop_time)
        MainWindow.setTabOrder(self.rd_loop_time, self.e_loop_hr)
        MainWindow.setTabOrder(self.e_loop_hr, self.e_loop_min)
        MainWindow.setTabOrder(self.e_loop_min, self.e_loop_sec)
        MainWindow.setTabOrder(self.e_loop_sec, self.e_loop_interval)
        MainWindow.setTabOrder(self.e_loop_interval, self.btn_prop_save)
        MainWindow.setTabOrder(self.btn_prop_save, self.btn_prop_rst)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Nox macro librarian", None))
        self.grp_props.setTitle(_translate("MainWindow", "Macro properties", None))
        self.label_7.setText(_translate("MainWindow", "sec", None))
        self.e_loop_min.setText(_translate("MainWindow", "0", None))
        self.label_3.setText(_translate("MainWindow", "times", None))
        self.rd_loop_no.setText(_translate("MainWindow", "Loop", None))
        self.rd_loop_till_stop.setText(_translate("MainWindow", "Loop until stop button is pressed", None))
        self.label_4.setText(_translate("MainWindow", "min", None))
        self.rd_loop_time.setText(_translate("MainWindow", "Loop", None))
        self.e_loop_sec.setText(_translate("MainWindow", "0", None))
        self.label_5.setText(_translate("MainWindow", "sec", None))
        self.e_loop_count.setText(_translate("MainWindow", "0", None))
        self.label.setText(_translate("MainWindow", "Name", None))
        self.e_loop_hr.setText(_translate("MainWindow", "0", None))
        self.e_loop_interval.setText(_translate("MainWindow", "0", None))
        self.label_6.setText(_translate("MainWindow", "Loop interval", None))
        self.label_2.setText(_translate("MainWindow", "hr", None))
        self.label_8.setText(_translate("MainWindow", "Acceleration", None))
        self.lbl_slider_value.setText(_translate("MainWindow", "1", None))
        self.btn_prop_save.setToolTip(_translate("MainWindow", "<html><head/><body><p>Save macro properties</p></body></html>", None))
        self.btn_prop_save.setText(_translate("MainWindow", "Save", None))
        self.btn_prop_rst.setToolTip(_translate("MainWindow", "<html><head/><body><p>Reset macro properties to inital ones</p></body></html>", None))
        self.btn_prop_rst.setText(_translate("MainWindow", "Reset", None))
        self.btn_edit_macro.setToolTip(_translate("MainWindow", "<html><head/><body><p>Edit macro content</p></body></html>", None))
        self.btn_edit_macro.setText(_translate("MainWindow", "Edit macro", None))
        self.btn_edit_macro_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Edit macro content</p></body></html>", None))
        self.btn_edit_macro_2.setText(_translate("MainWindow", "Edit macro", None))
        self.chk_backup.setToolTip(_translate("MainWindow", "<html><head/><body><p>Backs up existing records file </p></body></html>", None))
        self.chk_backup.setText(_translate("MainWindow", "Backup old file", None))
        self.btn_nox_save.setToolTip(_translate("MainWindow", "<html><head/><body><p>Creates a new records file. </p><p>To use it you need to reopen macro window in Nox</p></body></html>", None))
        self.btn_nox_save.setText(_translate("MainWindow", "Save to Nox", None))
        self.group_new_item.setTitle(_translate("MainWindow", "Add new macro", None))
        self.btn_new_macro.setToolTip(_translate("MainWindow", "<html><head/><body><p>Opens editor in which you can paste a macro content</p></body></html>", None))
        self.btn_new_macro.setText(_translate("MainWindow", "New macro", None))
        self.btn_import_file.setToolTip(_translate("MainWindow", "<html><head/><body><p>Import existing macro file</p></body></html>", None))
        self.btn_import_file.setText(_translate("MainWindow", "Import macro file", None))

from qt_custom import TestListWidget
