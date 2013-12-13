import sys

from PyQt4 import Qt, QtCore, QtGui
import decisionefantino_widget
import fantino

class decisionefantino(Qt.QDialog):
    def __init__(self, fantini=[], offerte=[]):
        Qt.QDialog.__init__(self)
        self.ui = decisionefantino_widget.Ui_DecisioneFantino()
        self.ui.setupUi(self)
        self.fantini = fantini
        self.offerte = offerte
        self.offerta = -1
        self.strategia = Qt.QStringList() << "A Vincere" << "A Correre" << "A Vendere" << "Killer..."

        self.buttonGroup = Qt.QButtonGroup()
        headers = Qt.QStringList() << "Fantino" << "Prezzo" << "Corsa" << "Scelta"
        self.ui.tableWidgetDecisioneFantino.setRowCount(len(self.offerte))
        self.ui.tableWidgetDecisioneFantino.setColumnCount(4)
        self.ui.tableWidgetDecisioneFantino.setHorizontalHeaderLabels(headers)
               
        self.ui.tableWidgetDecisioneFantino.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.populateTable()
        
        self.setWindowTitle("Offerte Accettate !!!")

        QtCore.QObject.connect(self.ui.tableWidgetDecisioneFantino, QtCore.SIGNAL("itemClicked(QTableWidgetItem*)"), self.selezione)

        self.ui.tableWidgetDecisioneFantino.resizeColumnsToContents()
        self.ui.tableWidgetDecisioneFantino.resize(500, 300)
        self.ui.tableWidgetDecisioneFantino.show()  
        
    def populateTable(self):
        for i in xrange(len(self.offerte)):
            item0 = Qt.QTableWidgetItem(self.fantini[self.offerte[i].fantino].nome)
            item1 = Qt.QTableWidgetItem(Qt.QString("%1").arg(self.offerte[i].soldi))
            item2 = Qt.QTableWidgetItem(self.strategia[self.offerte[i].strategia])
            item3 = Qt.QTableWidgetItem()
            item3.setCheckState(QtCore.Qt.Unchecked)

            self.ui.tableWidgetDecisioneFantino.setItem(i, 0, item0)
            self.ui.tableWidgetDecisioneFantino.setItem(i, 1, item1)
            self.ui.tableWidgetDecisioneFantino.setItem(i, 2, item2)
            self.ui.tableWidgetDecisioneFantino.setItem(i, 3, item3)

    def selezione(self, item):
        if (item.column() == 3):
            row = item.row()
            if (item.checkState() == QtCore.Qt.Checked):
                self.offerta = row
                for i in xrange(self.ui.tableWidgetDecisioneFantino.rowCount()):
                    if (i == row):
                        continue
                    self.ui.tableWidgetDecisioneFantino.item(i, 3).setCheckState(QtCore.Qt.Unchecked)
            else:
                self.offerta = -1
            
    def accept(self):
        self.done(Qt.QDialog.Accepted)
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    fantini = []
    offerte = []
    for i in xrange(4):
        o = fantino.Offerta()
        offerte.append(o)

    for i in xrange(16):
        f = fantino.Fantino()
        fantini.append(f)

    client = decisionefantino(fantini, offerte)
    client.show()
    sys.exit(app.exec_())


