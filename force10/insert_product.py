from PyQt4 import QtGui, QtCore 
from force_10_insert import Ui_Dialog

class InsertProduct(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Insert Product")
        self.ui.comboBox.setVisible(False)
        self.ui.dateEdit.setVisible(False)
        self.ui.label_3.setVisible(False)
        self.ui.label_4.setVisible(False)

    def text(self):
        return (self.ui.productName.text(), 
                self.ui.productDescription.text())
