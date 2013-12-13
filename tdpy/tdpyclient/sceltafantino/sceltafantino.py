import sys

from PyQt4 import Qt, QtCore, QtGui
import sceltafantino_widget
import fantino
import spinDelegate, comboDelegate, readOnlyDelegate
import fantinoModel

class sceltafantino(Qt.QDialog):
    def __init__(self, indice, fantini=[]):
        Qt.QDialog.__init__(self)
        self.ui = sceltafantino_widget.Ui_SceltaFantino()
        self.ui.setupUi(self)
        self.indice = indice
        self.fantini = fantini
        self.offerte = []

        lista = Qt.QStringList() << "Fantino" << "Eta`" << "Corsi" << "Vinti" << "Forma" << "Offerta" << "Corsa"
        self.model = fantinoModel.FantinoModel(len(fantini), 7)
        for i in xrange(7):
            self.model.setHeaderData(i, QtCore.Qt.Horizontal, lista[i])
        self.ui.tableWidgetSceltaFantino.setModel(self.model) 
        
        self.ui.tableWidgetSceltaFantino.setEditTriggers(Qt.QAbstractItemView.AllEditTriggers)
        self.ui.tableWidgetSceltaFantino.setItemDelegateForColumn(0, readOnlyDelegate.ReadOnlyDelegate(self))     
        self.ui.tableWidgetSceltaFantino.setItemDelegateForColumn(1, readOnlyDelegate.ReadOnlyDelegate(self))
        self.ui.tableWidgetSceltaFantino.setItemDelegateForColumn(2, readOnlyDelegate.ReadOnlyDelegate(self))
        self.ui.tableWidgetSceltaFantino.setItemDelegateForColumn(3, readOnlyDelegate.ReadOnlyDelegate(self))
        self.ui.tableWidgetSceltaFantino.setItemDelegateForColumn(4, readOnlyDelegate.ReadOnlyDelegate(self))
        self.ui.tableWidgetSceltaFantino.setItemDelegateForColumn(5, spinDelegate.SpinBoxDelegate(self))
        self.ui.tableWidgetSceltaFantino.setItemDelegateForColumn(6, comboDelegate.ComboDelegate(self))
        self.ui.tableWidgetSceltaFantino.horizontalHeader().setStretchLastSection(True)
        self.populateTable()
        
        self.setWindowTitle("Fantini disponibili...")
        
        self.ui.tableWidgetSceltaFantino.resizeColumnsToContents()
        self.ui.tableWidgetSceltaFantino.resize(500, 300)
        self.ui.tableWidgetSceltaFantino.show()  
        
    def populateTable(self):
        for row in xrange(len(self.fantini)):
            for column in xrange(7):
                index = self.model.index(row, column)
                f = self.fantini[row]
                if (column == 0):
                    self.model.setData(index, f.nome)
                if (column == 1):
                    self.model.setData(index, f.score[0])
                if (column == 2):
                    self.model.setData(index, f.score[1])
                if (column == 3):
                    self.model.setData(index, f.score[2])
                if (column == 4):
                    self.model.setData(index, f.capacita[3]*100+f.media())
                if (column == 5):
                    self.model.setData(index, f.prezzo())
                if (column == 6):
                    self.model.setData(index, "---------")

    def accept(self):
        selezioni = 0
        for row in xrange(self.model.rowCount()):
            index = self.model.index(row, 6)
            # FIXME puo` essere semplificato immagino lavorando sulle ComboBox
            corsa = index.data(QtCore.Qt.DisplayRole).toString()
            if (corsa != "---------"):
                selezioni += 1
                strategia = 3
                if (corsa == "A Vincere"):
                    strategia = 0
                if (corsa == "A Correre"):
                    strategia = 1
                if (corsa == "A Vendere"):
                    strategia = 2

                index = self.model.index(row, 5)
                prezzo = index.data(QtCore.Qt.DisplayRole).toInt()[0]
                o = fantino.Offerta(self.indice, strategia, self.fantini[row].indice, prezzo)
                self.offerte.append(o)

        if (selezioni <= 3):
            self.done(Qt.QDialog.Accepted)
        else:
            self.offerte = []
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    fantini = []
    for i in xrange(16):
        f = fantino.Fantino()
        fantini.append(f)
    client = sceltafantino(fantini)
    client.show()
    sys.exit(app.exec_())


