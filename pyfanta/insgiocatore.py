from PyQt4 import QtGui, QtCore
import ui_aggiungigiocatore
import Giocatore

class InsGiocatore(QtGui.QDialog):
    def __init__(self, g = Giocatore.Giocatore()):
        QtGui.QDialog.__init__(self)
        self.ui = ui_aggiungigiocatore.Ui_NewPlayer()
        self.giocatore = g
        self.ui.setupUi(self)
        self.ui.radioButton.setChecked(True)

        #TODO bloccare le lettere nel campo prezzo
        #TODO bloccare ok se il cognome e` vuoto
        QtCore.QObject.connect(self.ui.lineEdit, QtCore.SIGNAL("textChanged(const QString&)"), self.changeCognome)
        QtCore.QObject.connect(self.ui.lineEdit_2, QtCore.SIGNAL("textChanged(const QString&)"), self.changeNome)
        QtCore.QObject.connect(self.ui.lineEdit_3, QtCore.SIGNAL("textChanged(const QString&)"), self.changePrezzo)
        QtCore.QObject.connect(self.ui.lineEdit_4, QtCore.SIGNAL("textChanged(const QString&)"), self.changeSquadra)
        QtCore.QObject.connect(self.ui.radioButton, QtCore.SIGNAL("toggled(bool)"), self.changeRadio)
        QtCore.QObject.connect(self.ui.radioButton_2, QtCore.SIGNAL("toggled(bool)"), self.changeRadio)
        QtCore.QObject.connect(self.ui.radioButton_3, QtCore.SIGNAL("toggled(bool)"), self.changeRadio)
        QtCore.QObject.connect(self.ui.radioButton_4, QtCore.SIGNAL("toggled(bool)"), self.changeRadio)
        
        if (self.giocatore.indice != -1):
            self.fillField()

    def fillField(self):
        if (self.giocatore.ruolo == 0):
            self.ui.radioButton.setChecked(True)
        if (self.giocatore.ruolo == 1):
            self.ui.radioButton_2.setChecked(True)
        if (self.giocatore.ruolo == 2):
            self.ui.radioButton_3.setChecked(True)
        if (self.giocatore.ruolo == 3):
            self.ui.radioButton_4.setChecked(True)

        self.ui.lineEdit.setText(self.giocatore.cognome)
        self.ui.lineEdit_2.setText(self.giocatore.nome)
        self.ui.lineEdit_3.setText(QtCore.QString("%1").arg(str(self.giocatore.prezzo)))
        self.ui.lineEdit_4.setText(self.giocatore.squadra)


    def changeRadio(self, a):
        ruolo = int()
        if (self.ui.radioButton.isChecked()):
            ruolo = 0
        if (self.ui.radioButton_2.isChecked()):
            ruolo = 1
        if (self.ui.radioButton_3.isChecked()):
            ruolo = 2
        if (self.ui.radioButton_4.isChecked()):
            ruolo = 3

        self.giocatore.ruolo = ruolo

    def changeNome(self, s):
        #s.replace(" ", "_")
        self.giocatore.nome = s.toUpper()

    def changeCognome(self, s):
        #s.replace(" ", "_")
        self.giocatore.cognome = s.toUpper()

    def changePrezzo(self, s):
        self.giocatore.prezzo = s.toInt()

    def changeSquadra(self, s):
        #s.replace(" ", "_")
        self.giocatore.squadra = s.toUpper()
