from PyQt4 import QtGui, QtCore 
from force_10_show import Ui_Dialog

class ShowProblems(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # specificare componente nel titolo
        self.setWindowTitle("Problem List")
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(3)
        headerLabels = ("Date", "Problem", "Installed in:")
        self.ui.tableWidget.setHorizontalHeaderLabels(headerLabels);
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.show()

    def populate_table(self, results):
        self.ui.tableWidget.setRowCount(len(results))
        self.i = 0
        for self.r in results:
            self.item0 = QtGui.QTableWidgetItem(str(self.r[0]))
            self.item1 = QtGui.QTableWidgetItem(str(self.r[1]))
            self.item2 = QtGui.QTableWidgetItem(str(self.r[2]))

            self.ui.tableWidget.setItem(self.i, 0, self.item0);
            self.ui.tableWidget.setItem(self.i, 1, self.item1);
            self.ui.tableWidget.setItem(self.i, 2, self.item2);
            self.i += 1

        self.ui.tableWidget.resizeColumnsToContents()

