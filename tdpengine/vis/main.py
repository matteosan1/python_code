# -*- coding: utf-8 -*-
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from palio import *



class PalioMainWindow(QtGui.QMainWindow):
  
  def __init__(self):
    QtGui.QMainWindow.__init__(self)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.graphicScene = QtGui.QGraphicsScene()
    self.ui.graphicsView.setScene(self.graphicScene) # = QtGui.QGraphicsView(self.graphicScene, self)
    #self.graphicsView.setGeometry(QtCore.QRect(10, 10, 1200, 1000))
    #self.graphicsView.setObjectName("graphicsView")    
    self.ui.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    self.ui.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    self.drappellone()
    
  def drappellone(self):
    self.graphicScene.clear()
    nomefile = QString("/home/sani/tdpengine/piazza_colorata.png")
    
    pixMap = QtGui.QPixmap(nomefile)
    
    self.graphicScene.addPixmap(pixMap)
    self.ui.graphicsView.show()
    #self.ui.graphicsView.setSceneRect(100, 100, 10, 10)
    self.ui.graphicsView.scale(1.5, 1.5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = PalioMainWindow()
    main_window.show()
    sys.exit(app.exec_())

