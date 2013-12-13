# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tratta.ui'
#
# Created: Fri Jul 15 15:00:12 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Tratta(object):
    def setupUi(self, Tratta):
        Tratta.setObjectName(_fromUtf8("Tratta"))
        Tratta.resize(463, 481)
        self.vboxlayout = QtGui.QVBoxLayout(Tratta)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.cavalliView = QtGui.QTableWidget(Tratta)
        self.cavalliView.setDragDropOverwriteMode(False)
        self.cavalliView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.cavalliView.setObjectName(_fromUtf8("cavalliView"))
        self.cavalliView.setColumnCount(0)
        self.cavalliView.setRowCount(0)
        self.vboxlayout.addWidget(self.cavalliView)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.okButton = QtGui.QPushButton(Tratta)
        self.okButton.setEnabled(False)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.hboxlayout.addWidget(self.okButton)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(Tratta)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Tratta.accept)
        QtCore.QMetaObject.connectSlotsByName(Tratta)

    def retranslateUi(self, Tratta):
        Tratta.setWindowTitle(QtGui.QApplication.translate("Tratta", "Scelta Cavalli", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("Tratta", "OK", None, QtGui.QApplication.UnicodeUTF8))

