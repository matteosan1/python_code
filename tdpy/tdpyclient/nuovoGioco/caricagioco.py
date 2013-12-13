from PyQt4 import Qt,  QtCore
import caricagioco_widget

class caricaGioco(Qt.QDialog):
    def __init__(self):
        Qt.QDialog.__init__(self)
        self.ui = caricagioco_widget.Ui_CaricaGioco()
        self.ui.setupUi(self)
        
        self.nomi = []
        self.date = []

        self.connect(self.ui.tableFile, QtCore.SIGNAL("itemSelectionChanged()"), self.enableButton)
        self.connect(self.ui.caricaButton, QtCore.SIGNAL("clicked()"), self.load)
        self.connect(self.ui.cancellaButton, QtCore.SIGNAL("clicked()"), self.esci)
    
    def setVariables(self,  n,  d):
        self.nomi = n
        self.date = d
        self.headerLabels = Qt.QStringList()
        self.headerLabels << "Nome" << "Data Creazione"
        self.ui.tableFile.setHorizontalHeaderLabels(self.headerLabels)
        self.ui.tableFile.resizeColumnsToContents()
        self.ui.tableFile.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.ui.tableFile.setSelectionBehavior(Qt.QAbstractItemView.SelectRows)
        self.ui.tableFile.setSelectionMode(Qt.QAbstractItemView.SingleSelection)
        #self.ui.cavalliView.resize(500, 300)
        #self.ui.tableFile.show()
        self.ui.tableFile.setRowCount(len(self.nomi))
        self.ui.tableFile.setColumnCount(2)
        self.populateTable()

    def load(self):
        self.done(2)

    def esci(self):
        self.done(3)

    def populateTable(self):
        for i in xrange(len(self.nomi)):
            item0 = Qt.QTableWidgetItem(self.nomi[i])
            item1 = Qt.QTableWidgetItem(self.date[i])
            self.ui.tableFile.setItem(i, 0, item0);
            self.ui.tableFile.setItem(i, 1, item1);

    def enableButton(self):
        self.ui.caricaButton.setEnabled(True)

    def getSelection(self):
      return self.ui.tableFile.currentRow()
  
