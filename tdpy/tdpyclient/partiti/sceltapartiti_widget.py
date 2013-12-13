# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sceltapartiti.ui'
#
# Created: Sat Jul 30 00:43:16 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import dragWidget
import dragTableView

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SceltaPartito(object):
    def setupUi(self, SceltaPartito):
        SceltaPartito.setObjectName(_fromUtf8("SceltaPartito"))
        SceltaPartito.resize(314, 449)
        self.tableViewPartiti = dragTableView.DragTableView(SceltaPartito)
        self.tableViewPartiti.setGeometry(QtCore.QRect(0, 0, 311, 271))
        self.tableViewPartiti.setObjectName(_fromUtf8("tableViewPartiti"))
        self.frame = dragWidget.DragWidget(SceltaPartito)
        self.frame.setGeometry(QtCore.QRect(0, 280, 311, 121))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label1 = QtGui.QLabel(self.frame)
        self.label1.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.label2 = QtGui.QLabel(self.frame)
        self.label2.setGeometry(QtCore.QRect(70, 10, 51, 51))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.label3 = QtGui.QLabel(self.frame)
        self.label3.setGeometry(QtCore.QRect(130, 10, 51, 51))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.label4 = QtGui.QLabel(self.frame)
        self.label4.setGeometry(QtCore.QRect(190, 10, 51, 51))
        self.label4.setObjectName(_fromUtf8("label4"))
        self.label5 = QtGui.QLabel(self.frame)
        self.label5.setGeometry(QtCore.QRect(250, 10, 51, 51))
        self.label5.setObjectName(_fromUtf8("label5"))
        self.label8 = QtGui.QLabel(self.frame)
        self.label8.setGeometry(QtCore.QRect(130, 60, 51, 51))
        self.label8.setObjectName(_fromUtf8("label8"))
        self.label10 = QtGui.QLabel(self.frame)
        self.label10.setGeometry(QtCore.QRect(250, 60, 51, 51))
        self.label10.setObjectName(_fromUtf8("label10"))
        self.label9 = QtGui.QLabel(self.frame)
        self.label9.setGeometry(QtCore.QRect(190, 60, 51, 51))
        self.label9.setObjectName(_fromUtf8("label9"))
        self.label7 = QtGui.QLabel(self.frame)
        self.label7.setGeometry(QtCore.QRect(70, 60, 51, 51))
        self.label7.setObjectName(_fromUtf8("label7"))
        self.label6 = QtGui.QLabel(self.frame)
        self.label6.setGeometry(QtCore.QRect(10, 60, 51, 51))
        self.label6.setObjectName(_fromUtf8("label6"))
        self.buttonBox = QtGui.QDialogButtonBox(SceltaPartito)
        self.buttonBox.setGeometry(QtCore.QRect(130, 410, 170, 26))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(SceltaPartito)
        QtCore.QMetaObject.connectSlotsByName(SceltaPartito)

    def retranslateUi(self, SceltaPartito):
        SceltaPartito.setWindowTitle(QtGui.QApplication.translate("SceltaPartito", "Partiti", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("SceltaPartito", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("SceltaPartito", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("SceltaPartito", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label4.setText(QtGui.QApplication.translate("SceltaPartito", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label5.setText(QtGui.QApplication.translate("SceltaPartito", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label8.setText(QtGui.QApplication.translate("SceltaPartito", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label10.setText(QtGui.QApplication.translate("SceltaPartito", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label9.setText(QtGui.QApplication.translate("SceltaPartito", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label7.setText(QtGui.QApplication.translate("SceltaPartito", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label6.setText(QtGui.QApplication.translate("SceltaPartito", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

