# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caricagioco.ui'
#
# Created: Tue Jun 15 15:14:31 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CaricaGioco(object):
    def setupUi(self, CaricaGioco):
        CaricaGioco.setObjectName("CaricaGioco")
        CaricaGioco.resize(400, 300)
        self.hboxlayout = QtGui.QHBoxLayout(CaricaGioco)
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.tableFile = QtGui.QTableWidget(CaricaGioco)
        self.tableFile.setObjectName("tableFile")
        self.tableFile.setColumnCount(0)
        self.tableFile.setRowCount(0)
        self.vboxlayout.addWidget(self.tableFile)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.newButton = QtGui.QPushButton(CaricaGioco)
        self.newButton.setObjectName("newButton")
        self.hboxlayout1.addWidget(self.newButton)
        self.caricaButton = QtGui.QPushButton(CaricaGioco)
        self.caricaButton.setEnabled(False)
        self.caricaButton.setObjectName("caricaButton")
        self.hboxlayout1.addWidget(self.caricaButton)
        self.cancellaButton = QtGui.QPushButton(CaricaGioco)
        self.cancellaButton.setObjectName("cancellaButton")
        self.hboxlayout1.addWidget(self.cancellaButton)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.retranslateUi(CaricaGioco)
        QtCore.QObject.connect(self.cancellaButton, QtCore.SIGNAL("clicked()"), CaricaGioco.reject)
        QtCore.QObject.connect(self.newButton, QtCore.SIGNAL("clicked()"), CaricaGioco.accept)
        QtCore.QMetaObject.connectSlotsByName(CaricaGioco)

    def retranslateUi(self, CaricaGioco):
        CaricaGioco.setWindowTitle(QtGui.QApplication.translate("CaricaGioco", "Carica Gioco", None, QtGui.QApplication.UnicodeUTF8))
        self.newButton.setText(QtGui.QApplication.translate("CaricaGioco", "Nuovo...", None, QtGui.QApplication.UnicodeUTF8))
        self.caricaButton.setText(QtGui.QApplication.translate("CaricaGioco", "Carica...", None, QtGui.QApplication.UnicodeUTF8))
        self.cancellaButton.setText(QtGui.QApplication.translate("CaricaGioco", "Cancella", None, QtGui.QApplication.UnicodeUTF8))

