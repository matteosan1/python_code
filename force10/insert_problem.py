from PyQt4 import QtGui, QtCore 
from force_10_insert_problem import Ui_Dialog

class InsertProblem(QtGui.QDialog):
    def __init__(self, combo1, combo2):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Insert Problem")
        self.ui.dateEdit.setDisplayFormat("yyyy-MM-dd") 
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
        for self.i in combo1:
            self.ui.comboBox.addItem(self.i[1])

        for self.i in combo2:
            self.ui.comboBox_2.addItem(self.i[1])

    def text(self):
        return (self.ui.comboBox.currentIndex(),
                self.ui.comboBox_2.currentIndex(),
                self.ui.dateEdit.date().toString("yyyy-MM-dd"),
                self.ui.lineEdit.text())
