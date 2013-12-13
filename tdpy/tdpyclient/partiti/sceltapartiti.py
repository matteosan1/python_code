from PyQt4 import Qt, QtCore, QtGui
import sceltapartiti_widget
import partitiModel, spinDelegate, comboDelegate
import sys

class sceltaPartiti(Qt.QDialog):
    def __init__(self): 
        Qt.QDialog.__init__(self)
        self.ui = sceltapartiti_widget.Ui_SceltaPartito()
        self.ui.setupUi(self)

        lista = ["aquila", "bruco", "chiocciola", "civetta", "drago", "giraffa", "istrice", "leocorno", "lupa", "nicchio"]

        self.ui.label1.setPixmap(Qt.QPixmap("../pictures/" + lista[0] + ".jpg").scaledToHeight(50))
        self.ui.label1.setObjectName("0")
        self.ui.label2.setPixmap(Qt.QPixmap("../pictures/" + lista[1] + ".jpg").scaledToHeight(50))
        self.ui.label2.setObjectName("1")
        self.ui.label3.setPixmap(Qt.QPixmap("../pictures/" + lista[2] + ".jpg").scaledToHeight(50))
        self.ui.label3.setObjectName("2")
        self.ui.label4.setPixmap(Qt.QPixmap("../pictures/" + lista[3] + ".jpg").scaledToHeight(50))
        self.ui.label4.setObjectName("3")
        self.ui.label5.setPixmap(Qt.QPixmap("../pictures/" + lista[4] + ".jpg").scaledToHeight(50))
        self.ui.label5.setObjectName("4")
        self.ui.label6.setPixmap(Qt.QPixmap("../pictures/" + lista[5] + ".jpg").scaledToHeight(50))
        self.ui.label6.setObjectName("5")
        self.ui.label7.setPixmap(Qt.QPixmap("../pictures/" + lista[6] + ".jpg").scaledToHeight(50))
        self.ui.label7.setObjectName("6")
        self.ui.label8.setPixmap(Qt.QPixmap("../pictures/" + lista[7] + ".jpg").scaledToHeight(50))
        self.ui.label8.setObjectName("7")
        self.ui.label9.setPixmap(Qt.QPixmap("../pictures/" + lista[8] + ".jpg").scaledToHeight(50))
        self.ui.label9.setObjectName("8")
        self.ui.label10.setPixmap(Qt.QPixmap("../pictures/" + lista[9] + ".jpg").scaledToHeight(50))
        self.ui.label10.setObjectName("9")

        self.model = partitiModel.PartitiModel(0, 5, lista)
        headers = Qt.QStringList() << "Contrada" << " " << "Azione" << "Dettaglio" << "Offerta"
        for i in xrange(5):
            self.model.setHeaderData(i, QtCore.Qt.Horizontal, headers[i])

        self.ui.tableViewPartiti.setModel(self.model) 
        self.ui.tableViewPartiti.setColumnHidden(1, True)

        self.ui.tableViewPartiti.setEditTriggers(Qt.QAbstractItemView.AllEditTriggers)
        self.ui.tableViewPartiti.setItemDelegateForColumn(4, spinDelegate.SpinBoxDelegate(self))     
        self.ui.tableViewPartiti.setItemDelegateForColumn(3, comboDelegate.ComboDelegate([""]+lista, self))
        lista = ["Vai Piano !", "Ferma: "];
        self.ui.tableViewPartiti.setItemDelegateForColumn(2, comboDelegate.ComboDelegate(lista, self))
        
        self.ui.tableViewPartiti.verticalHeader().setVisible(False)
        
        self.setWindowTitle("Partiti")
        self.ui.tableViewPartiti.resizeColumnsToContents()       
        self.ui.tableViewPartiti.show()  
        
    def populateTable(self):
        for row in xrange(0):
            for column in xrange(4):
                index = self.model.index(row, column)
                f = self.fantini[row]
                if (column == 0):
                    self.model.setData(index, f.nome)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    client = sceltaPartiti()
    client.show()
    sys.exit(app.exec_())

