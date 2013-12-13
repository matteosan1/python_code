from PyQt4 import QtGui, QtCore
import ui_formazione

class Formazione(QtGui.QDialog):
    def __init__(self, s):
        QtGui.QDialog.__init__(self)
        self.ui = ui_formazione.Ui_Formazione()
        self.ui.setupUi(self)
        self.squadra = s
        self.moduloCorrente = [0,0,0,0]
        self.fillTables()
        self.setWindowTitle("Formazione")
        QtCore.QObject.connect(self.ui.tableFormazione, QtCore.SIGNAL("itemChanged(QTableWidgetItem*)"), self.checkFormazione) 
        QtCore.QObject.connect(self.ui.giornataCombo, QtCore.SIGNAL("currentIndexChanged(int)"), self.setGiornata) 

    def giornataSelezionata(self):
        return self.ui.giornataCombo.currentIndex()+1

    def fillTables(self):
        for i in xrange(17):
            item = (QtGui.QTableWidgetItem("-"))
            self.ui.tableFormazione.setItem(i, 0, item);
        self.ui.tableFormazione.resizeColumnsToContents()

        self.ui.tableRosa.setRowCount(len(self.squadra.giocatori))
        self.ui.tableRosa.setColumnCount(1)
        self.ui.tableRosa.resizeColumnsToContents()

        for i,j in enumerate(self.squadra.giocatori):
            # FIXME per quelli fuori rosa
            r = j.ruolo
            item = (QtGui.QTableWidgetItem(str(j.nomeCompleto())))
            if (r==0):
                item.setForeground(QtGui.QColor(0,0,50))
            elif (r==1):
                item.setForeground(QtGui.QColor(0,0,100))
            elif (r==2):
                item.setForeground(QtGui.QColor(0,0,150))
            elif (r==3):
                item.setForeground(QtGui.QColor(0,0,200))
            elif (r==10):
                item.setForeground(QtGui.QColor(50,0,0))
            elif (r==11):
                item.setForeground(QtGui.QColor(100,0,0))
            elif (r==12):
                item.setForeground(QtGui.QColor(150,0,0))
            elif (r==13):
                item.setForeground(QtGui.QColor(200,0,0))

            self.ui.tableRosa.setItem(i, 0, item);

        self.ui.tableRosa.resizeColumnsToContents()

        if (self.squadra.giornata > 0):
            lista = QtCore.QStringList()
            for i in xrange(1, self.squadra.giornata+2):
                lista.append("%d"%i)
            self.ui.giornataCombo.insertItems(0, lista)
            self.ui.giornataCombo.setEnabled(True)
            self.ui.giornataCombo.setCurrentIndex(self.squadra.giornata)


    def checkFormazione(self, item):
        # controlla modulo
        formazione = [0,0,0,0]
        for i in xrange(11):
            item = self.ui.tableFormazione.item(i, 0)
            if (item and item.text() != "-"):
                if ((item.foreground().color().red() == 50) or (item.foreground().color().blue() == 50)):
                    formazione[0] += 1
                elif ((item.foreground().color().red() == 100) or (item.foreground().color().blue() == 100)):
                    formazione[1] += 1
                elif ((item.foreground().color().red() == 150) or (item.foreground().color().blue() == 150)):
                    formazione[2] += 1
                elif ((item.foreground().color().red() == 200) or (item.foreground().color().blue() == 200)):
                    formazione[3] += 1

        if (formazione[0] != 1):
            self.ui.labelStato.setText("Devi schierare un\nsolo portiere")
            self.ui.buttonBox.setEnabled(False)
            return
        
        modulo = "".join(str(i) for i in formazione[1:])
        if (modulo not in self.squadra.punteggi.schemi):
            self.ui.buttonBox.setEnabled(False)
            self.ui.labelStato.setText("Modulo non\npermesso")
            return                                 

        # controlla formazione
        for i in xrange(self.ui.tableFormazione.rowCount()-1):
            item = self.ui.tableFormazione.item(i, 0).text()
            if (item == "-"):
                continue
            for j in xrange(i+1, self.ui.tableFormazione.rowCount()):
                item2 = self.ui.tableFormazione.item(j, 0).text()
                if (item == item2):
                    self.ui.labelStato.setText("Hai schierato un\ngiocatore piu` volte")
                    self.ui.buttonBox.setEnabled(False)
                    return

        self.ui.labelStato.setText("")
        self.ui.buttonBox.setEnabled(True)

    def modulo(self):
        formazione = [0,0,0,0]
        for i in xrange(11):
            item = self.ui.tableFormazione.item(i, 0)
            if (item and item.text() != "-"):                
                if ((item.foreground().color().red() == 50) or (item.foreground().color().blue() == 50)):
                    formazione[0] += 1
                elif ((item.foreground().color().red() == 100) or (item.foreground().color().blue() == 100)):
                    formazione[1] += 1
                elif ((item.foreground().color().red() == 150) or (item.foreground().color().blue() == 150)):
                    formazione[2] += 1
                elif ((item.foreground().color().red() == 200) or (item.foreground().color().blue() == 200)):
                    formazione[3] += 1
        
        modulo = "".join(str(i) for i in formazione[1:])
        return modulo

    def setGiornata(self, a):
        if self.squadra.giornata < a+1:
            for i in xrange(18):
                item = (QtGui.QTableWidgetItem("-"))
                item.setForeground(QtCore.Qt.black)
                self.ui.tableFormazione.setItem(i, 0, item)
            self.ui.tableFormazione.resizeColumnsToContents()
            return
        for i,j in enumerate(self.squadra.formazioni[a+1]):
            if (j != -1):
                for g in self.squadra.giocatori:
                    if (g.indice == j):
                        r = g.ruolo           
                        item = (QtGui.QTableWidgetItem(g.nomeCompleto()))
                        if (r==0):
                            item.setForeground(QtGui.QColor(0,0,50))
                        elif (r==1):
                            item.setForeground(QtGui.QColor(0,0,100))
                        elif (r==2):
                            item.setForeground(QtGui.QColor(0,0,150))
                        elif (r==3):
                            item.setForeground(QtGui.QColor(0,0,200))
                        elif (r==10):
                            item.setForeground(QtGui.QColor(50,0,0))
                        elif (r==11):
                            item.setForeground(QtGui.QColor(100,0,0))
                        elif (r==12):
                            item.setForeground(QtGui.QColor(150,0,0))
                        elif (r==13):
                            item.setForeground(QtGui.QColor(200,0,0))

                        self.ui.tableFormazione.setItem(i, 0, item)
                        break
                            
        self.ui.tableFormazione.resizeColumnsToContents()

    def readFormazione(self):
        formazione = []
        for i in xrange(self.ui.tableFormazione.rowCount()):
            formazione.append(self.ui.tableFormazione.item(i, 0).text())
        
        return formazione
