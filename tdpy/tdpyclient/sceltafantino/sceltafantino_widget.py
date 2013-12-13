# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sceltafantino.ui'
#
# Created: Thu Jul 28 22:39:00 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SceltaFantino(object):
    def setupUi(self, SceltaFantino):
        SceltaFantino.setObjectName(_fromUtf8("SceltaFantino"))
        SceltaFantino.resize(550, 605)
        self.verticalLayout = QtGui.QVBoxLayout(SceltaFantino)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidgetSceltaFantino = QtGui.QTableView(SceltaFantino)
        self.tableWidgetSceltaFantino.setObjectName(_fromUtf8("tableWidgetSceltaFantino"))
        self.verticalLayout.addWidget(self.tableWidgetSceltaFantino)
        self.buttonBox = QtGui.QDialogButtonBox(SceltaFantino)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SceltaFantino)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SceltaFantino.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SceltaFantino.reject)
        QtCore.QMetaObject.connectSlotsByName(SceltaFantino)

    def retranslateUi(self, SceltaFantino):
        SceltaFantino.setWindowTitle(QtGui.QApplication.translate("SceltaFantino", "Fantini Disponibili", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
