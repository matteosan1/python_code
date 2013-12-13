from PyQt4 import Qt, QtCore
import tratta_widget
import cavallo
from operator import attrgetter

class tratta(Qt.QDialog):

    def __init__(self, cavalli=[]):
        Qt.QDialog.__init__(self)
        self.ui = tratta_widget.Ui_Tratta()
        self.ui.setupUi(self)

        self.connect(self.ui.cavalliView, QtCore.SIGNAL("itemSelectionChanged()"), self.selection)
        
        self.ui.cavalliView.setRowCount(len(cavalli))
        self.ui.cavalliView.setColumnCount(4)
        
        self.ui.cavalliView.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.ui.cavalliView.setSelectionBehavior(Qt.QAbstractItemView.SelectRows)
        self.ui.cavalliView.setSelectionMode(Qt.QAbstractItemView.MultiSelection)
        
        headerLabels = Qt.QStringList()
        headerLabels << "Cavallo" << "Corsi" << "Vinti" << "Stato"
        self.ui.cavalliView.setHorizontalHeaderLabels(headerLabels)

        cavalli.sort(key=attrgetter('coscia'))

        self.populateTable(cavalli)
        self.ui.cavalliView.resizeColumnsToContents()
        self.ui.cavalliView.show()

    def selection(self):
        selections = (len(self.ui.cavalliView.selectedItems())/4.)
        self.cambiaCaption(Qt.QString("Seleziona: %1 cavalli").arg(10-selections))

        if (selections == 10):
            self.ui.okButton.setEnabled(True)
        else:
            self.ui.okButton.setEnabled(False)

    def populateTable(self, cavalli):
        for j in xrange(len(cavalli)):
            item0 = Qt.QTableWidgetItem(cavalli[j].nome)
            item1 = Qt.QTableWidgetItem(Qt.QString("%1").arg(cavalli[j].score[2]))
            item2 = Qt.QTableWidgetItem(Qt.QString("%1").arg(cavalli[j].score[3]))
            item3 = Qt.QTableWidgetItem()
            if (cavalli[j].media() > 6.0):
                item3 = Qt.QTableWidgetItem(Qt.QIcon(":/status/pictures/buono.bmp"), "")
            elif (cavalli[j].media() < 4.0):
                item3 = Qt.QTableWidgetItem(Qt.QIcon(":/status/pictures/scarso.bmp"), "")
            else:
                item3 = Qt.QTableWidgetItem(Qt.QIcon(":/status/pictures/suff.bmp"), "");
      
            self.ui.cavalliView.setItem(j, 0, item0)
            self.ui.cavalliView.setItem(j, 1, item1)
            self.ui.cavalliView.setItem(j, 2, item2)
            self.ui.cavalliView.setItem(j, 3, item3)
            self.ui.cavalliView.item(j, 0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.ui.cavalliView.item(j, 1).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.ui.cavalliView.item(j, 2).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.ui.cavalliView.item(j, 3).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            
        self.cambiaCaption(Qt.QString("Seleziona: %1 cavalli").arg(10))

    def cambiaCaption(self, s):
        cap = Qt.QString("Scelta Cavalli (" + s +")")
        self.setWindowTitle(cap)

    def getSelection(self):
        result = []
        for i in xrange(len(self.ui.cavalliView.selectedItems()), 4): #step di 4
            for j in xrange(len(cavalli)):
                if (cavalli[j].coscia == self.ui.cavalliView.selectedItems().at(i).row()):
                    result.append(cavalli[j].indice)

        return result
