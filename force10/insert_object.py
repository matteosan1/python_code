from PyQt4 import QtGui, QtCore 
from force_10_insert import Ui_Dialog

class InsertObject(QtGui.QDialog):
    def __init__(self, combos):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Insert Object")
        self.ui.label.setText("Serial Number:")
        self.ui.label_2.setText("Revision:")
        self.ui.label_4.setText("Shipment:")
        self.ui.label_3.setText("Type:")
        self.ui.dateEdit.setDisplayFormat("yyyy-MM-dd") 
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
        for self.i in combos:
            self.ui.comboBox.addItem(self.i[1])

    def text(self):
        return (self.ui.comboBox.currentIndex(),
                self.ui.dateEdit.date().toString("yyyy-MM-dd") ,
                self.ui.productName.text(), 
                self.ui.productDescription.text())
