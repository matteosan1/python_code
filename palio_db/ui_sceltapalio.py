# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sceltapalio.ui'
#
# Created: Wed Jun 24 00:38:58 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SceltaPalio(object):
    def setupUi(self, SceltaPalio):
        SceltaPalio.setObjectName("SceltaPalio")
        SceltaPalio.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(SceltaPalio)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtGui.QLineEdit(SceltaPalio)
        self.lineEdit.setGeometry(QtCore.QRect(150, 70, 71, 29))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtGui.QLabel(SceltaPalio)
        self.label.setGeometry(QtCore.QRect(50, 80, 69, 19))
        self.label.setObjectName("label")
        self.comboBox = QtGui.QComboBox(SceltaPalio)
        self.comboBox.setGeometry(QtCore.QRect(140, 130, 131, 28))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(SceltaPalio)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SceltaPalio.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SceltaPalio.reject)
        QtCore.QMetaObject.connectSlotsByName(SceltaPalio)

    def retranslateUi(self, SceltaPalio):
        SceltaPalio.setWindowTitle(QtGui.QApplication.translate("SceltaPalio", "Scelta Palio", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setInputMask(QtGui.QApplication.translate("SceltaPalio", "9999;_", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SceltaPalio", "Anno", None, QtGui.QApplication.UnicodeUTF8))

