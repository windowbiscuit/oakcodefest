# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CFSGSSBCE.ui'
#
# Created: Sun Jan 20 06:15:37 2019
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(854, 721)
        self.lbl_mode = QtGui.QLabel(Dialog)
        self.lbl_mode.setGeometry(QtCore.QRect(10, 290, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.lbl_mode.setFont(font)
        self.lbl_mode.setObjectName(_fromUtf8("lbl_mode"))
        self.lbl_EID = QtGui.QLabel(Dialog)
        self.lbl_EID.setGeometry(QtCore.QRect(10, 90, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(18)
        self.lbl_EID.setFont(font)
        self.lbl_EID.setObjectName(_fromUtf8("lbl_EID"))
        self.lbl_day = QtGui.QLabel(Dialog)
        self.lbl_day.setGeometry(QtCore.QRect(10, 140, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(18)
        font.setItalic(True)
        self.lbl_day.setFont(font)
        self.lbl_day.setObjectName(_fromUtf8("lbl_day"))
        self.lne_TCF = QtGui.QLineEdit(Dialog)
        self.lne_TCF.setGeometry(QtCore.QRect(720, 340, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lne_TCF.setFont(font)
        self.lne_TCF.setObjectName(_fromUtf8("lne_TCF"))
        self.lne_month = QtGui.QLineEdit(Dialog)
        self.lne_month.setGeometry(QtCore.QRect(280, 190, 561, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lne_month.setFont(font)
        self.lne_month.setObjectName(_fromUtf8("lne_month"))
        self.lne_day = QtGui.QLineEdit(Dialog)
        self.lne_day.setGeometry(QtCore.QRect(280, 140, 561, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lne_day.setFont(font)
        self.lne_day.setObjectName(_fromUtf8("lne_day"))
        self.lne_year = QtGui.QLineEdit(Dialog)
        self.lne_year.setGeometry(QtCore.QRect(280, 240, 561, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lne_year.setFont(font)
        self.lne_year.setObjectName(_fromUtf8("lne_year"))
        self.lne_eID = QtGui.QLineEdit(Dialog)
        self.lne_eID.setGeometry(QtCore.QRect(280, 90, 561, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lne_eID.setFont(font)
        self.lne_eID.setText(_fromUtf8(""))
        self.lne_eID.setObjectName(_fromUtf8("lne_eID"))
        self.lbl_year = QtGui.QLabel(Dialog)
        self.lbl_year.setGeometry(QtCore.QRect(10, 240, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(18)
        font.setItalic(True)
        self.lbl_year.setFont(font)
        self.lbl_year.setObjectName(_fromUtf8("lbl_year"))
        self.lbl_month = QtGui.QLabel(Dialog)
        self.lbl_month.setGeometry(QtCore.QRect(10, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(18)
        font.setItalic(True)
        self.lbl_month.setFont(font)
        self.lbl_month.setObjectName(_fromUtf8("lbl_month"))
        self.btn_calc_cf = QtGui.QPushButton(Dialog)
        self.btn_calc_cf.setGeometry(QtCore.QRect(640, 350, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Pirate"))
        font.setPointSize(16)
        font.setItalic(True)
        self.btn_calc_cf.setFont(font)
        self.btn_calc_cf.setObjectName(_fromUtf8("btn_calc_cf"))
        self.lbl_TCF = QtGui.QLabel(Dialog)
        self.lbl_TCF.setGeometry(QtCore.QRect(300, 340, 321, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.lbl_TCF.setFont(font)
        self.lbl_TCF.setObjectName(_fromUtf8("lbl_TCF"))
        self.lbl_shallgivesalary = QtGui.QLabel(Dialog)
        self.lbl_shallgivesalary.setGeometry(QtCore.QRect(410, 10, 401, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_shallgivesalary.setFont(font)
        self.lbl_shallgivesalary.setObjectName(_fromUtf8("lbl_shallgivesalary"))
        self.lbl_carbonfootprint = QtGui.QLabel(Dialog)
        self.lbl_carbonfootprint.setGeometry(QtCore.QRect(10, 10, 401, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_carbonfootprint.setFont(font)
        self.lbl_carbonfootprint.setObjectName(_fromUtf8("lbl_carbonfootprint"))
        self.lne_tsalary = QtGui.QLineEdit(Dialog)
        self.lne_tsalary.setGeometry(QtCore.QRect(650, 660, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lne_tsalary.setFont(font)
        self.lne_tsalary.setObjectName(_fromUtf8("lne_tsalary"))
        self.lne_bonusmon = QtGui.QLineEdit(Dialog)
        self.lne_bonusmon.setGeometry(QtCore.QRect(280, 600, 561, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lne_bonusmon.setFont(font)
        self.lne_bonusmon.setObjectName(_fromUtf8("lne_bonusmon"))
        self.lbl_tsalary = QtGui.QLabel(Dialog)
        self.lbl_tsalary.setGeometry(QtCore.QRect(250, 660, 301, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.lbl_tsalary.setFont(font)
        self.lbl_tsalary.setObjectName(_fromUtf8("lbl_tsalary"))
        self.lne_bonuspc = QtGui.QLineEdit(Dialog)
        self.lne_bonuspc.setGeometry(QtCore.QRect(280, 540, 561, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lne_bonuspc.setFont(font)
        self.lne_bonuspc.setObjectName(_fromUtf8("lne_bonuspc"))
        self.lbl_bonus = QtGui.QLabel(Dialog)
        self.lbl_bonus.setGeometry(QtCore.QRect(10, 600, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.lbl_bonus.setFont(font)
        self.lbl_bonus.setObjectName(_fromUtf8("lbl_bonus"))
        self.lbl_bonuspc = QtGui.QLabel(Dialog)
        self.lbl_bonuspc.setGeometry(QtCore.QRect(10, 540, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.lbl_bonuspc.setFont(font)
        self.lbl_bonuspc.setObjectName(_fromUtf8("lbl_bonuspc"))
        self.btn_calc_sal = QtGui.QPushButton(Dialog)
        self.btn_calc_sal.setGeometry(QtCore.QRect(570, 670, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Pirate"))
        font.setPointSize(16)
        font.setItalic(True)
        self.btn_calc_sal.setFont(font)
        self.btn_calc_sal.setObjectName(_fromUtf8("btn_calc_sal"))
        self.lne_bonuspc_2 = QtGui.QLineEdit(Dialog)
        self.lne_bonuspc_2.setGeometry(QtCore.QRect(280, 440, 561, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lne_bonuspc_2.setFont(font)
        self.lne_bonuspc_2.setText(_fromUtf8(""))
        self.lne_bonuspc_2.setObjectName(_fromUtf8("lne_bonuspc_2"))
        self.lbl_bonuspc_2 = QtGui.QLabel(Dialog)
        self.lbl_bonuspc_2.setGeometry(QtCore.QRect(10, 440, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.lbl_bonuspc_2.setFont(font)
        self.lbl_bonuspc_2.setObjectName(_fromUtf8("lbl_bonuspc_2"))
        self.lbl_bonuspc_3 = QtGui.QLabel(Dialog)
        self.lbl_bonuspc_3.setGeometry(QtCore.QRect(10, 490, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.lbl_bonuspc_3.setFont(font)
        self.lbl_bonuspc_3.setObjectName(_fromUtf8("lbl_bonuspc_3"))
        self.lne_bonuspc_3 = QtGui.QLineEdit(Dialog)
        self.lne_bonuspc_3.setGeometry(QtCore.QRect(280, 490, 561, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lne_bonuspc_3.setFont(font)
        self.lne_bonuspc_3.setText(_fromUtf8(""))
        self.lne_bonuspc_3.setObjectName(_fromUtf8("lne_bonuspc_3"))
        self.cb_mode = QtGui.QComboBox(Dialog)
        self.cb_mode.setGeometry(QtCore.QRect(280, 290, 561, 41))
        self.cb_mode.setObjectName(_fromUtf8("cb_mode"))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.setItemText(0, _fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.lbl_bonuspc_4 = QtGui.QLabel(Dialog)
        self.lbl_bonuspc_4.setGeometry(QtCore.QRect(10, 390, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stephen"))
        font.setPointSize(20)
        self.lbl_bonuspc_4.setFont(font)
        self.lbl_bonuspc_4.setObjectName(_fromUtf8("lbl_bonuspc_4"))
        self.lne_bonuspc_4 = QtGui.QLineEdit(Dialog)
        self.lne_bonuspc_4.setGeometry(QtCore.QRect(280, 390, 561, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Poor Richard"))
        font.setPointSize(16)
        font.setItalic(True)
        self.lne_bonuspc_4.setFont(font)
        self.lne_bonuspc_4.setText(_fromUtf8(""))
        self.lne_bonuspc_4.setObjectName(_fromUtf8("lne_bonuspc_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lbl_mode.setText(_translate("Dialog", "Mode of transport :", None))
        self.lbl_EID.setText(_translate("Dialog", "Employee ID : ", None))
        self.lbl_day.setText(_translate("Dialog", "Day :", None))
        self.lbl_year.setText(_translate("Dialog", "Year :", None))
        self.lbl_month.setText(_translate("Dialog", "Month :", None))
        self.btn_calc_cf.setText(_translate("Dialog", "calc", None))
        self.lbl_TCF.setText(_translate("Dialog", "Total carbon footprints :", None))
        self.lbl_shallgivesalary.setText(_translate("Dialog", "Shall Give Salary", None))
        self.lbl_carbonfootprint.setText(_translate("Dialog", "Carbon Footprint", None))
        self.lbl_tsalary.setText(_translate("Dialog", "Total Salary (in Rs.) :", None))
        self.lbl_bonus.setText(_translate("Dialog", "Bonus (in Rs.) :", None))
        self.lbl_bonuspc.setText(_translate("Dialog", "Bonus percentage :", None))
        self.btn_calc_sal.setText(_translate("Dialog", "calc", None))
        self.lbl_bonuspc_2.setText(_translate("Dialog", "Month :", None))
        self.lbl_bonuspc_3.setText(_translate("Dialog", "Year :", None))
        self.cb_mode.setItemText(1, _translate("Dialog", "Bus", None))
        self.cb_mode.setItemText(2, _translate("Dialog", "Car", None))
        self.cb_mode.setItemText(3, _translate("Dialog", "Motorcycle", None))
        self.cb_mode.setItemText(4, _translate("Dialog", "Cycle", None))
        self.cb_mode.setItemText(5, _translate("Dialog", "Walking", None))
        self.cb_mode.setItemText(6, _translate("Dialog", "Metro", None))
        self.cb_mode.setItemText(7, _translate("Dialog", "Autorikshaw", None))
        self.lbl_bonuspc_4.setText(_translate("Dialog", "Employee ID:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

