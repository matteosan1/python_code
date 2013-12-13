from PyQt4 import QtGui, QtCore, Qt
import Squadra, Giocatore, Punteggi
import IO
import parser_2011_12
import Lista
import ui_fanta
import insformazione
import insgiocatore
import aggiornaVoti
import Regole
import datetime, re

class Fantamania(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_fanta.Ui_fanta()
        self.ui.setupUi(self)
        self.fileName = ""
        self.username = ""
        self.password = ""
        self.model = 0
        self.isModified = False
        self.labelSq = QtGui.QLabel()
        self.squadra = Squadra.Squadra()
        
        self.ui.actionSave.setEnabled(False)
        self.ui.actionNuovo_giocatore.setEnabled(False)
        self.ui.actionElimina_Giocatore.setEnabled(False)
        self.ui.actionModifica_Giocatore.setEnabled(False)
        self.ui.actionAggiorna_Giocatore.setEnabled(False)
        self.ui.actionInserisci_Voti.setEnabled(False)
        self.ui.actionMedie_Giocatori.setEnabled(False)
        self.ui.actionProfilo_Squadra.setEnabled(False)
        self.ui.actionFormazione.setEnabled(False)
        self.ui.actionFormazione_tipo.setEnabled(False)
        self.ui.actionMedie_Giocatori.setCheckable(True)
        self.ui.actionMedie_Giocatori.setChecked(False)
        
        self.ui.statusbar.addWidget(self.labelSq, 1)
        
        QtCore.QObject.connect(self.ui.actionOpen, QtCore.SIGNAL("activated()"), self.fileOpen)
        QtCore.QObject.connect(self.ui.actionSave, QtCore.SIGNAL("activated()"), self.fileSave)
        QtCore.QObject.connect(self.ui.actionFormazione, QtCore.SIGNAL("activated()"), self.insFormazione)
        QtCore.QObject.connect(self.ui.actionChiudi, QtCore.SIGNAL("activated()"), self.close)
        QtCore.QObject.connect(self.ui.actionMedie_Giocatori, QtCore.SIGNAL("toggled(bool)"), self.changeView)
        QtCore.QObject.connect(self.ui.actionNuovo_giocatore, QtCore.SIGNAL("activated()"), self.addPlayer)
        QtCore.QObject.connect(self.ui.actionModifica_Giocatore, QtCore.SIGNAL("activated()"), self.modifyPlayer)
        QtCore.QObject.connect(self.ui.actionAggiorna_Giocatore, QtCore.SIGNAL("activated()"), self.updatePlayer)
        QtCore.QObject.connect(self.ui.actionElimina_Giocatore, QtCore.SIGNAL("activated()"), self.killPlayer)
        QtCore.QObject.connect(self.ui.actionNew, QtCore.SIGNAL("activated()"), self.nuovaSquadra)
        QtCore.QObject.connect(self.ui.actionFormazione_tipo, QtCore.SIGNAL("activated()"), self.tipo)
        QtCore.QObject.connect(self.ui.tableGiocatori, QtCore.SIGNAL("doubleClicked(const QModelIndex&)"), self.riassunto)

    def fileSaveAs(self):
        fileFilters = QtCore.QString("Fantamania files (*.fnm);; Tutti (*.*)")
        f = QtCore.QFileDialog.getSaveFileName(self, "Save file", "/home/sani/Documents/Fantamaniaco", fileFilters)

        if (f.isEmpty()):
            return
        
        if (QtCore.QFile.exists(f)):
            ret = QtGui.QMessageBox.warning(self, "Fantamania Avvertimento", "Il giuoco %s esiste gia`.\nVuoi sovrascrivere ?"%(f), QtGui.QMessageBox.Yes | QtGui.QMessageBox.Default, QtGui.QMessageBox.No | QtGui.QMessageBox.Escape)
        if (ret == QtGui.QMessageBox.No):
            return
  
        if (not f.isEmpty()):
            self.fileName = str(f)
            self.fileSave()

    def fileSave(self):
        if (self.fileName == ""):
            self.fileSaveAs()
        else:
            IO.saveSquadra(self.squadra, self.fileName)
            self.ui.actionSave.setEnabled(False)
            self.isModified = False

    def fileOpen(self):
        fileFilters = QtCore.QString("Fantamania files (*.fnm);; Tutti (*.*)")
        if (self.isModified):
            self.fileSave()
  
        f = QtGui.QFileDialog.getOpenFileName(self, "Open file", "/home/sani/Documents/Fantamaniaco", fileFilters)

        if (not f.isEmpty()):
            self.fileName = str(f)
            self.squadra = IO.loadSquadra(self.fileName)
            for i in self.squadra.giocatori:
                if (i.ruolo == -1):
                    i.ruolo = 0
            self.squadra.ordinaGiocatori()
            self.fillList(self.ui.actionMedie_Giocatori.isChecked())
            self.isModified = False
            self.ui.actionSave.setEnabled(False)
            self.ui.actionNuovo_giocatore.setEnabled(True)
            self.ui.actionElimina_Giocatore.setEnabled(True)
            self.ui.actionModifica_Giocatore.setEnabled(True)
            self.ui.actionAggiorna_Giocatore.setEnabled(True)
            self.ui.actionInserisci_Voti.setEnabled(True)
            self.ui.actionMedie_Giocatori.setEnabled(True)
            self.ui.actionProfilo_Squadra.setEnabled(True)
            self.ui.actionFormazione_tipo.setEnabled(True)
            self.ui.actionFormazione.setEnabled(True);
            self.setWindowTitle("Fantamanager ("+self.squadra.nome+")")

    def fillList(self, toggleState):
        self.model = Lista.Giocatori(self.squadra, toggleState)
        self.ui.tableGiocatori.setModel(self.model)
        self.ui.tableGiocatori.show()
        note = "Giornate: " + QtCore.QString("%1").arg(self.squadra.giornata) + ", Media: " + QtCore.QString("%1").arg(self.squadra.mediaTotale(), 0, 'f', 2)
        self.labelSq.setText(note)

    def closeEvent(self, event):
        if (self.isModified):
            ret = Qt.QMessageBox.warning(self, "Fantamania Avvertimento", "Vuoi salvare i cambiamenti ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.Default, QtGui.QMessageBox.No | QtGui.QMessageBox.Escape)
            if (ret == QtGui.QMessageBox.Yes):
                self.fileSave()
  
    def insFormazione(self):
        f = insformazione.Formazione(self.squadra)
        if (f.exec_() == QtGui.QDialog.Accepted):
            giornataDaScaricare = f.giornataSelezionata()
            if (giornataDaScaricare == 0):
                giornataDaScaricare = 1;

            # FIXME LA SECONDA VOLTA NON FUNZIONA
            if (self.username == ""):
                while(1):
                    username = QtGui.QInputDialog.getText(self, QtCore.QString("Collegamento Fantagazzetta"), QtCore.QString("User name: "), QtGui.QLineEdit.Normal, QtCore.QString(""))
    
                    if (username[1] and not username[0].isEmpty()):
                        password = QtGui.QInputDialog.getText(self, QtCore.QString("Collegamento Fantagazzetta"), QtCore.QString("Password: "), QtGui.QLineEdit.Password, QtCore.QString(""))
                        
                        if (password[1] and not password[0].isEmpty()):
                            self.username = str(username[0])
                            self.password = str(password[0])
                            break

            Qt.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            out = IO.scaricaPagina(self.username, self.password, giornataDaScaricare)
            if (out != (0,0)):
                QtGui.QMessageBox.critical(self, "Fantamania Errore", "Impossibile scaricare i voti !")
                return
            tags = parser_2011_12.votiPerGiocatore_2011_12(giornataDaScaricare)
            Qt.QApplication.restoreOverrideCursor()

            mappa = {}
            for i in self.squadra.giocatori:
                mappa[i.nomeCompleto()] = i.indice
            indici = [g.indice for g in self.squadra.giocatori]
                                
            formazione = []
            for g in f.readFormazione():
                if (g == "-"):
                    formazione.append(-1)
                else:
                    formazione.append(mappa[str(g)])

            #print "FORMAZIONE"
            #for i in formazione[0:11]:
            #    print self.squadra.giocatori[indici.index(i)].cognome
            #print "--------------"
            #for i in formazione[11:]:
            #    print self.squadra.giocatori[indici.index(i)].cognome

            self.squadra.addFormazione(formazione, giornataDaScaricare)
            self.squadra.calcoloPrestazione(tags, giornataDaScaricare)
            
            (formazione_finale, panchina, totale) = self.squadra.totale(giornataDaScaricare)

            a2 = "FORMAZIONE FINALE                \n\n"
            giocatoIn = 0
            for i in formazione_finale:
                #if (i[1] != 0):
                if (self.squadra.giocatori[i[0]].prestazioni[giornataDaScaricare][1][0] != 0):
                    giocatoIn += 1
                a2 = a2 + self.squadra.giocatori[i[0]].cognome+" "+str(i[1])+"\n"

            #print "TOTALE:", totale
                      
            a1 = "\nPunteggio Giornata: " + QtCore.QString("%1").arg(giornataDaScaricare)
            a2 = a2+ "Modulo schierato: " + f.modulo() + "\n"
            if (giocatoIn < 11):
                a2 = a2 + "Sfortunatamente hai giocato con soli " + str(giocatoIn) + " giocatori.\n"
            a2 = a2 + "Punteggio totale: " + str(totale)

            if (self.squadra.giornata <= giornataDaScaricare):
                self.squadra.giornata = giornataDaScaricare

            QtGui.QMessageBox.information(self, a1, a2);
            self.fillList(self.ui.actionMedie_Giocatori.isChecked())
            self.isModified = True;
            self.ui.actionSave.setEnabled(True)

    def changeView(self, toggleState):
        self.fillList(toggleState)

    def updatePlayer(self):
        nomi = QtCore.QStringList()
        for g in self.squadra.giocatori:
            if (g.ruolo < 4):
                nomi.append(g.nomeCompleto())
        
        item = QtGui.QInputDialog.getItem(self, "Giocatore da aggiornare", "Nome giocatore: ", nomi, 0, False)
  
        if (item[1] and not item[0].isEmpty()):
            for i,j in enumerate(nomi):
                if (j == str(item[0])):
                    k = i
                    break
    
        Qt.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        for giornata in xrange(1, self.squadra.giornata+1):
            out = IO.scaricaPagina("matteosan", "fisica", giornata, True)
            if (out != (0,0)):
                QtGui.QMessageBox.critical(self, "Fantamania Errore", "Impossibile scaricare i voti !")
                break
            else:    
                tags = parser_2011_12.votiPerGiocatore_2011_12(giornata)

                matches = []
                n = self.squadra.giocatori[k].cognome
                nome = self.squadra.giocatori[k].nome

                for iteration in xrange(1, len(nome.split(" "))+1):
                    matches = [string for string in tags.keys() if re.match("^"+n, string)]
                    if (len(matches) == 0 or len(matches) == 1):
                        break
                    n = n + " " + nome.split(" ")[iteration]

                if (len(matches) != 0):
                    self.squadra.giocatori[k].replacePrestazione(giornata, tags[matches[0]])
        
        self.squadra.ordinaGiocatori()

        Qt.QApplication.restoreOverrideCursor()

        self.fillList(self.ui.actionMedie_Giocatori.isChecked())
        self.isModified = True
        self.ui.actionSave.setEnabled(True)

    def addPlayer(self):
        i = insgiocatore.InsGiocatore(Giocatore.Giocatore())

        if (i.exec_() == QtGui.QDialog.Accepted):
            if (i.giocatore.nome == ""):
                i.giocatore.nome = "_"
            
            if (i.giocatore.squadra == ""):
                i.giocatore.squadra = "_"
                        
            i.giocatore.indice = len(self.squadra.giocatori)
            i.giocatore.nome = str(i.giocatore.nome)
            i.giocatore.cognome = str(i.giocatore.cognome)
            i.giocatore.squadra = str(i.giocatore.squadra)
            self.squadra.addGiocatore(i.giocatore)

            if (self.username == ""):
                while(1):
                    username = QtGui.QInputDialog.getText(self, QtCore.QString("Collegamento Fantagazzetta"), QtCore.QString("User name: "), QtGui.QLineEdit.Normal, QtCore.QString(""))
    
                    if (username[1] and not username[0].isEmpty()):
                        password = QtGui.QInputDialog.getText(self, QtCore.QString("Collegamento Fantagazzetta"), QtCore.QString("Password: "), QtGui.QLineEdit.Password, QtCore.QString(""))
                        
                        if (password[1] and not password[0].isEmpty()):
                            self.username = str(username[0])
                            self.password = str(password[0])
                            break

            Qt.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            for giornata in xrange(1, self.squadra.giornata+1):
                out = IO.scaricaPagina("matteosan", "fisica", giornata, True)
                if (out != (0,0)):
                    QtGui.QMessageBox.critical(self, "Fantamania Errore", "Impossibile scaricare i voti !")
                    break
                else:    
                    tags = parser_2011_12.votiPerGiocatore_2011_12(giornata)

                    matches = []
                    n = self.squadra.giocatori[-1].cognome
                    nome = self.squadra.giocatori[-1].nome

                    for iteration in xrange(1, len(nome.split(" "))+1):
                        matches = [string for string in tags.keys() if re.match("^"+n, string)]
                        if (len(matches) == 0 or len(matches) == 1):
                            break
                        n = n + " " + nome.split(" ")[iteration]

                    if (len(matches) != 0):
                        self.squadra.giocatori[-1].replacePrestazione(giornata, tags[matches[0]])
        
            self.squadra.ordinaGiocatori()

            Qt.QApplication.restoreOverrideCursor()

            self.fillList(self.ui.actionMedie_Giocatori.isChecked())
            self.isModified = True
            self.ui.actionSave.setEnabled(True)
  
    def modifyPlayer(self):
        nomi = QtCore.QStringList()
        for g in self.squadra.giocatori:
            nomi.append(g.nomeCompleto())
        item = QtGui.QInputDialog.getItem(self, "Modifica giocatore", "Nome giocatore: ", nomi, 0, False)

        if (item[1] and not item[0].isEmpty()):
            for i,j in enumerate(nomi):
                if (j == item[0]):
                    k = i;
                    break;

            j = insgiocatori.InsGiocatore(self.squadra.giocatori[k])

            if (j.exec_() == QtCore.Qt.Accepted):
                self.squadra.giocatori[k] = j.giocatore()
                self.squadra.ordinaGiocatori()
                self.fillList(self.ui.actionMedie_Giocatori.isChecked())
                self.isModified = True;
                self.ui.actionSave.setEnabled(True)

    def killPlayer(self):
        nomi = QtCore.QStringList()
        for g in self.squadra.giocatori:
            if (g.ruolo < 4):
                nomi.append(g.nomeCompleto())
        
        item = QtGui.QInputDialog.getItem(self, "Giocatore Fuori Rosa", "Nome giocatore: ", nomi, 0, False)
  
        if (item[1] and not item[0].isEmpty()):
            for i,j in enumerate(nomi):
                if (j == str(item[0])):
                    k = i
                    break
    
            ret = QtGui.QMessageBox.warning(self, "Fantamania Avvertimento", "Vuoi mettere il giocatore %s fuori rosa ?"%(self.squadra.giocatori[k].nomeCompleto()), QtGui.QMessageBox.Yes | QtGui.QMessageBox.Default, QtGui.QMessageBox.No | QtGui.QMessageBox.Escape)

            if (ret == QtGui.QMessageBox.Yes):
                self.squadra.giocatori[k].ruolo += 10
                self.squadra.ordinaGiocatori();
                self.fillList(self.ui.actionMedie_Giocatori.isChecked())
                self.isModified = True;
                self.ui.actionSave.setEnabled(True)

    def nuovaSquadra(self):
        if (self.isModified):
            ret = QtGui.QMessageBox.warning(self, "Fantamania Avvertimento", "Vuoi salvare i cambiamenti ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.Default, QtGui.QMessageBox.No | QtGui.QMessageBox.Escape)
            if (ret == QtGui.QMessageBox.Yes):
                self.fileSave()

  
        nome = QtGui.QInputDialog.getText(self, QtCore.QString("Nuova Squadra"), QtCore.QString("Nome della squadra: "), QtGui.QLineEdit.Normal, QtCore.QString(""))
  
        if (nome[1]):
            if (nome[0].isEmpty()):
                nome[0] = "SQUADRA"
    
            self.squadra = Squadra.Squadra()
            if (datetime.datetime.today().month < 8):
                self.squadra.anno = str(datetime.datetime.today().year-1)+"/"+str(datetime.datetime.today().year)
            else:
                self.squadra.anno = str(datetime.datetime.today().year)+"/"+str(datetime.datetime.today().year+1)

            r = Regole.Regole() 
            if (r.exec_() == QtGui.QDialog.Accepted):
                for j,i in enumerate(r.model.giocatori):
                    i.indice = j
                    self.squadra.addGiocatore(i)

                self.isModified = True
                self.squadra.giornata = 0
                self.squadra.nome = nome[0]
                self.squadra.ordinaGiocatori()
                self.fillList(self.ui.actionMedie_Giocatori.isChecked())
                self.ui.actionSave.setEnabled(False)
      
            else:
                QtGui.QMessageBox.critical(self, "Fantamania Errore", "Nessuna squadra e` stata salvata.")
                return
        else:
            QtGui.QMessageBox.critical(self, "Fantamania Errore", "Nessuna squadra e` stata salvata.")
            return
  
  
        self.ui.actionNuovo_giocatore.setEnabled(True)
        self.ui.actionElimina_Giocatore.setEnabled(True)
        self.ui.actionModifica_Giocatore.setEnabled(True)
        self.ui.actionAggiorna_Giocatore.setEnabled(True)
        self.ui.actionInserisci_Voti.setEnabled(True)
        self.ui.actionMedie_Giocatori.setEnabled(True)
        self.ui.actionProfilo_Squadra.setEnabled(True)
        self.ui.actionFormazione_tipo.setEnabled(True)
        self.ui.actionFormazione.setEnabled(True)
        self.setWindowTitle("Fantamania ("+self.squadra.nome+")")
        
    def tipo(self):
        pass
    #    t = FormTipo(giocatori, self, punt)
    #    if (t.exec__() == Qt.QDialog.Accepted):
    #        return
  
    def riassunto(self, index):
        if (not self.model.toggle):
            giornata = index.column()+1
            g = self.squadra.giocatori[index.row()]

            a = aggiornaVoti.AggiornaVoti(g, giornata)
            if (a.exec_() == Qt.QDialog.Accepted):
                self.squadra.giocatori[index.row()].prestazioni[giornata] = a.getPrestazione()
                self.fillList(self.ui.actionMedie_Giocatori.isChecked())
                self.isModified = True
                self.ui.actionSave.setEnabled(True)
  

# TODO controllare il fuoco delle varie finestre
# TODO mettere squadra consigliata
