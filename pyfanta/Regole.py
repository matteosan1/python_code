from PyQt4 import QtGui, QtCore
import Punteggi
import ui_regole
import ComboBoxDelegate
import GiocatoriInsert

class Regole(QtGui.QDialog):
    def __init__(self, p = Punteggi.Punteggi()):
        QtGui.QDialog.__init__(self)
        self.ui = ui_regole.Ui_RegolamentoDialog()
        self.ui.setupUi(self)

        self.punteggi = p
        self.model = GiocatoriInsert.GiocatoriInsert()

        self.ui.tableView.verticalHeader().hide()
        self.ui.tableView.setItemDelegateForColumn(2, ComboBoxDelegate.ComboBoxDelegate(self))
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.show()
        
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("pressed()"), self.insertRow)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("pressed()"), self.removeRow)
        
        QtCore.QObject.connect(self.ui.checkBox_13, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_2, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_3, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_4, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_5, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_6, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_7, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_8, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_10, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_11, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_10, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_11, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_9, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        QtCore.QObject.connect(self.ui.checkBox_12, QtCore.SIGNAL("stateChanged(int)"), self.changeCheck)
        
        QtCore.QObject.connect(self.ui.spinBox_7, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_8, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_9, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_10, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_11, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_12, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_20, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_21, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_22, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_6, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        
        QtCore.QObject.connect(self.ui.spinBox_19, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_13, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_14, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_15, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_16, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_17, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_18, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_23, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_24, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)
        QtCore.QObject.connect(self.ui.spinBox_5, QtCore.SIGNAL("valueChanged(int)"), self.changeSpin)

        self.changeSpin(0)
        self.changeCheck(0)

    def insertRow(self):
        self.ui.tableView.model().insertRows(0, 1)

    def removeRow(self):
        row = self.ui.tableView.currentIndex().row()
        self.ui.tableView.model().removeRows(row, 1)

    def changeCheck(self, a):
        #check numero portieri se non auto_portiere almeno 2 portieri in squadra
        if (self.ui.checkBox_13.checkState() == QtCore.Qt.Checked):
            self.punteggi.auto_portiere = 1
        else:
            self.punteggi.auto_portiere = 0

        if (self.ui.checkBox_9.checkState() == QtCore.Qt.Checked):
            self.punteggi.sei_politico = 1
        else:
            self.punteggi.sei_politico = 0

        if (self.ui.checkBox_12.checkState() == QtCore.Qt.Checked):
            self.punteggi.sv_portiere = 1
        else:
            self.punteggi.sv_portiere = 0

        if (self.ui.checkBox_10.checkState() == QtCore.Qt.Checked):
            self.punteggi.schemi[0] = 1
        else:
            self.punteggi.schemi[0] = 0

        if (self.ui.checkBox_2.checkState() == QtCore.Qt.Checked):
            self.punteggi.schemi[1] = 1
        else:
            self.punteggi.schemi[1] = 0

        if (self.ui.checkBox_3.checkState() == QtCore.Qt.Checked):
            self.punteggi.schemi[2] = 1
        else:
            self.punteggi.schemi[2] = 0

        if (self.ui.checkBox_4.checkState() == QtCore.Qt.Checked):
            self.punteggi.schemi[3] = 1
        else:
            self.punteggi.schemi[3] = 0

        if (self.ui.checkBox_5.checkState() == QtCore.Qt.Checked):
            self.punteggi.schemi[4] = 1
        else:
            self.punteggi.schemi[4] = 0

        if (self.ui.checkBox_6.checkState() == QtCore.Qt.Checked):
            self.punteggi.schemi[5] = 1
        else:
            self.punteggi.schemi[5] = 0

        if (self.ui.checkBox_7.checkState() == QtCore.Qt.Checked):
            self.punteggi.schemi[6] = 1
        else:
            self.punteggi.schemi[6] = 0

        if (self.ui.checkBox_11.checkState() == QtCore.Qt.Checked):
            self.punteggi.schemi[7] = 1
        else:
            self.punteggi.schemi[7] = 0

        if (self.ui.checkBox_8.checkState() == QtCore.Qt.Checked):
            self.punteggi.schemi[8] = 1
        else:
            self.punteggi.schemi[8] = 0


    def changeSpin(self, a):
        self.punteggi.reti[0] = self.ui.spinBox_7.value()
        self.punteggi.reti[1] = self.ui.spinBox_8.value()
        self.punteggi.reti[2] = self.ui.spinBox_9.value()
        self.punteggi.reti[3] = self.ui.spinBox_10.value()
        self.punteggi.reti[4] = self.ui.spinBox_11.value()
        self.punteggi.reti[5] = self.ui.spinBox_12.value()
        self.punteggi.reti[6] = self.ui.spinBox_20.value()
        self.punteggi.reti[7] = self.ui.spinBox_21.value()
        self.punteggi.reti[8] = self.ui.spinBox_22.value()
        self.punteggi.reti[9] = self.ui.spinBox_6.value()
        
        self.punteggi.gsu = self.ui.spinBox_19.value()
        self.punteggi.rp = self.ui.spinBox_13.value()
        self.punteggi.rsb = self.ui.spinBox_14.value()
        self.punteggi.gse = self.ui.spinBox_15.value()
        self.punteggi.ass = self.ui.spinBox_16.value()
        self.punteggi.am = self.ui.spinBox_17.value()
        self.punteggi.es = self.ui.spinBox_18.value()
        self.punteggi.rse = self.ui.spinBox_23.value()
        self.punteggi.au = self.ui.spinBox_24.value()

