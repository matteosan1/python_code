from PyQt4 import QtGui, QtCore
import Giocatore
import ui_aggiornaVoti

class AggiornaVoti(QtGui.QDialog):
    def __init__(self, g, gio):
        QtGui.QDialog.__init__(self)
        self.ui = ui_aggiornaVoti.Ui_AggiornaVoti()
        self.giocatore = g
        self.prestazione = g.prestazioni[gio]
        self.ui.setupUi(self)
        
        self.ui.labelGiornata.setText(QtCore.QString("%1").arg(gio))
        self.ui.labelGiocatore.setText(QtCore.QString("%1").arg(self.giocatore.cognome))
        
        if (self.giocatore.ammonito(gio)):
            self.ui.radioButton_2.setChecked(True)
        if (self.giocatore.espulso(gio)):
            self.ui.radioButton_3.setChecked(True)
            
        self.ui.doubleSpinBoxVoto.setValue(self.prestazione[1][0])
        if (self.giocatore.ruolo%10 != 0):
            self.ui.spinBoxGoal.setValue(self.prestazione[2])
            self.ui.spinBoxRigoriSe.setValue(self.prestazione[3])
            self.ui.spinBoxRigoriSb.setValue(self.prestazione[6])
            self.ui.spinBoxAutogoal.setValue(self.prestazione[7])
        else:
            self.ui.label_8.setText("Rigori Parati")
            self.ui.spinBoxGoal.setValue(self.prestazione[4])
            self.ui.spinBoxRigoriSb.setValue(self.prestazione[5])
            self.ui.spinBoxAutogoal.setValue(self.prestazione[7])

    def getPrestazione(self):
        if (self.ui.radioButton_2.isChecked()):
            self.prestazione[1][1] == 1
        if (self.ui.radioButton_3.isChecked()):
            self.prestazione[1][1] == 2
        self.prestazione[1][0] =  self.ui.doubleSpinBoxVoto.value();

        if (self.giocatore.ruolo%10 != 0):
            self.prestazione[2] = self.ui.spinBoxGoal.value()
            self.prestazione[3] = self.ui.spinBoxRigoriSe.value()
            self.prestazione[6] = self.ui.spinBoxRigoriSb.value()
            self.prestazione[7] = self.ui.spinBoxAutogoal.value()
        else:
            self.prestazione[4] = self.ui.spinBoxGoal.value()
            self.prestazione[5] = self.ui.spinBoxRigoriSb.value()
            self.prestazione[7] = self.ui.spinBoxAutogoal.value()

        return self.prestazione
