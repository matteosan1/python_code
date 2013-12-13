# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formazione.ui'
#
# Created: Sun Jan 16 00:37:06 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import DragTable

class Ui_Formazione(object):
    def setupUi(self, Formazione):
        Formazione.setObjectName("Formazione")
        Formazione.resize(565, 457)
        self.buttonBox = QtGui.QDialogButtonBox(Formazione)
        self.buttonBox.setEnabled(False)
        self.buttonBox.setGeometry(QtCore.QRect(430, 370, 81, 63))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.labelStato = QtGui.QLabel(Formazione)
        self.labelStato.setGeometry(QtCore.QRect(400, 310, 151, 41))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelStato.setFont(font)
        self.labelStato.setObjectName("labelStato")
        self.labelStato.setText(QtGui.QApplication.translate("Formazione", "Formazione vuota", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPo = QtGui.QLabel(Formazione)
        self.labelPo.setGeometry(QtCore.QRect(230, 10, 91, 18))
        self.labelPo.setObjectName("labelPo")
        self.layoutWidget = QtGui.QWidget(Formazione)
        self.layoutWidget.setGeometry(QtCore.QRect(410, 30, 115, 53))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vboxlayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.vboxlayout.addWidget(self.label_5)
        self.giornataCombo = QtGui.QComboBox(self.layoutWidget)
        self.giornataCombo.setEnabled(False)
        self.giornataCombo.setObjectName("giornataCombo")
        self.vboxlayout.addWidget(self.giornataCombo)
        self.tableFormazione = DragTable.DragTable(Formazione)
        self.tableFormazione.rosa = False
        #self.tableFormazione.setDragDropOverwriteMode(True)
        self.tableFormazione.setGeometry(QtCore.QRect(10, 70, 191, 330))
        self.tableFormazione.setDragEnabled(True)
        self.tableFormazione.setAcceptDrops(True)
        self.tableFormazione.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.tableFormazione.setShowGrid(False)
        self.tableFormazione.setObjectName("tableFormazione")
        self.tableFormazione.setColumnCount(1)
        self.tableFormazione.setRowCount(17)
        self.tableFormazione.horizontalHeader().setVisible(False)
        self.tableFormazione.verticalHeader().setVisible(True)
        self.tableRosa = DragTable.DragTable(Formazione)
        self.tableRosa.setGeometry(QtCore.QRect(220, 30, 171, 401))
        self.tableRosa.setDragEnabled(True)
        self.tableRosa.setAcceptDrops(False)
        #self.tableRosa.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.tableRosa.setShowGrid(False)
        self.tableRosa.setObjectName("tableRosa")
        self.tableRosa.setColumnCount(0)
        self.tableRosa.setRowCount(0)
        self.tableRosa.horizontalHeader().setVisible(False)
        self.tableRosa.verticalHeader().setVisible(False)
        self.labelPo_2 = QtGui.QLabel(Formazione)
        self.labelPo_2.setGeometry(QtCore.QRect(20, 50, 91, 18))
        self.labelPo_2.setObjectName("labelPo_2")

        self.retranslateUi(Formazione)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Formazione.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Formazione.reject)
        QtCore.QMetaObject.connectSlotsByName(Formazione)

    def retranslateUi(self, Formazione):
        Formazione.setWindowTitle(QtGui.QApplication.translate("Formazione", "Inserisci formazione", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPo.setText(QtGui.QApplication.translate("Formazione", "Rosa", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Formazione", "Scegli giornata:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPo_2.setText(QtGui.QApplication.translate("Formazione", "Formazione", None, QtGui.QApplication.UnicodeUTF8))

