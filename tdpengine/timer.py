import sys

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import *

class MainForm(QMainWindow):
    def __init___(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.timer = QtCore.QTimer(self)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.update())
        self.timer.start(1000)
        
    def update(self):
        self.setWindowTitle("MATTEO")

app = QApplication(sys.argv)

topLevel = MainForm()
topLevel.show()
app.exec_()



