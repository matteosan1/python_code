# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decisionefantino.ui'
#
# Created: Fri Jul 29 17:43:29 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DecisioneFantino(object):
    def setupUi(self, DecisioneFantino):
        DecisioneFantino.setObjectName(_fromUtf8("DecisioneFantino"))
        DecisioneFantino.resize(628, 241)
        self.verticalLayout = QtGui.QVBoxLayout(DecisioneFantino)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidgetDecisioneFantino = QtGui.QTableWidget(DecisioneFantino)
        self.tableWidgetDecisioneFantino.setObjectName(_fromUtf8("tableWidgetDecisioneFantino"))
        self.tableWidgetDecisioneFantino.setColumnCount(0)
        self.tableWidgetDecisioneFantino.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidgetDecisioneFantino)
        self.buttonBox = QtGui.QDialogButtonBox(DecisioneFantino)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DecisioneFantino)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DecisioneFantino.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DecisioneFantino.reject)
        QtCore.QMetaObject.connectSlotsByName(DecisioneFantino)

    def retranslateUi(self, DecisioneFantino):
        DecisioneFantino.setWindowTitle(QtGui.QApplication.translate("DecisioneFantino", "Fantini Disponibili", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
