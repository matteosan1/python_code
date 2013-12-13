# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listacavalli.ui'
#
# Created: Fri Jul 29 23:24:02 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ListaCavalli(object):
    def setupUi(self, ListaCavalli):
        ListaCavalli.setObjectName(_fromUtf8("ListaCavalli"))
        ListaCavalli.resize(413, 463)
        self.horizontalLayout = QtGui.QHBoxLayout(ListaCavalli)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QTextEdit(ListaCavalli)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.buttonBox = QtGui.QDialogButtonBox(ListaCavalli)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(ListaCavalli)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ListaCavalli.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ListaCavalli.reject)
        QtCore.QMetaObject.connectSlotsByName(ListaCavalli)

    def retranslateUi(self, ListaCavalli):
        ListaCavalli.setWindowTitle(QtGui.QApplication.translate("ListaCavalli", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

