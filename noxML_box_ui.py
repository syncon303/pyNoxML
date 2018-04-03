# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'noxML_editbox.ui'
#
# Created: Sat Mar 24 18:16:05 2018
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

class Ui_form_edit_macro(object):
    def setupUi(self, form_edit_macro):
        form_edit_macro.setObjectName(_fromUtf8("form_edit_macro"))
        form_edit_macro.resize(487, 737)
        self.edit_macro = QtGui.QTextEdit(form_edit_macro)
        self.edit_macro.setGeometry(QtCore.QRect(0, 0, 486, 691))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(9)
        self.edit_macro.setFont(font)
        self.edit_macro.setObjectName(_fromUtf8("edit_macro"))
        self.btn_box = QtGui.QDialogButtonBox(form_edit_macro)
        self.btn_box.setGeometry(QtCore.QRect(160, 705, 156, 26))
        self.btn_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.btn_box.setCenterButtons(False)
        self.btn_box.setObjectName(_fromUtf8("btn_box"))

        self.retranslateUi(form_edit_macro)
        QtCore.QMetaObject.connectSlotsByName(form_edit_macro)

    def retranslateUi(self, form_edit_macro):
        form_edit_macro.setWindowTitle(_translate("form_edit_macro", "Edit macro", None))

