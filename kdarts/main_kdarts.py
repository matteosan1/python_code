from PyQt4 import QtGui, QtCore 
from ui_main_kdarts import Ui_MainKdarts

class MainDialog(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainKdarts()
        self.ui.setupUi(self)
        self.players = ("Matteo")
        self.ui.label.setPixmap(QtGui.QPixmap("./bersaglio.png"))
        #self.ui.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);
        #self.ui.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers);

#        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.populate_table)

