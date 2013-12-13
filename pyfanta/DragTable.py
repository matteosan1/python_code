from PyQt4 import QtCore, QtGui, Qt

class DragTable(QtGui.QTableWidget):
    def __init__(self, parent = None):
        super(DragTable, self).__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.setDragDropMode(Qt.QAbstractItemView.DragDrop)
        self.setDragDropOverwriteMode(False)
        self.rosa = True

    def startDrag(self, dropActions):
        item = self.selectedItems()[0]
        r = -1            
        if ((item.foreground().color().red() == 50) or (item.foreground().color().blue() == 50)):
            r = 0
        elif ((item.foreground().color().red() == 100) or (item.foreground().color().blue() == 100)):
            r = 1
        elif ((item.foreground().color().red() == 150) or (item.foreground().color().blue() == 150)):
            r = 2 
        elif ((item.foreground().color().red() == 200) or (item.foreground().color().blue() == 200)):
            r = 3
              
        mimeData = QtCore.QMimeData()
        mimeData.setText(item.text()+"@"+str(r))
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        if (drag.start(QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction):
            self.removeRow(self.row(item))

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/plain"):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("text/plain"):
            if (self.rosa):
                event.setDropAction(QtCore.Qt.MoveAction)
            else:
                event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):        
        if (event.mimeData().hasFormat("text/plain")):
            text = event.mimeData().text().split("@")
            item = (QtGui.QTableWidgetItem(text[0]))
            r = int(text[1])
            if (r==0):
                item.setForeground(QtGui.QColor(0,0,50))
            elif (r==1):
                item.setForeground(QtGui.QColor(0,0,100))
            elif (r==2):
                item.setForeground(QtGui.QColor(0,0,150))
            elif (r==3):
                item.setForeground(QtGui.QColor(0,0,200))
            elif (r==10):
                item.setForeground(QtGui.QColor(50,0,0))
            elif (r==11):
                item.setForeground(QtGui.QColor(100,0,0))
            elif (r==12):
                item.setForeground(QtGui.QColor(150,0,0))
            elif (r==13):
                item.setForeground(QtGui.QColor(200,0,0))
              
            if (not self.rosa):
                if (not self.itemAt(event.pos()) is None):
                    row = self.itemAt(event.pos()).row()
                    self.setItem(row, 0, item);    
            else:
                self.setRowCount(self.rowCount()+1)
                self.setItem(self.rowCount()-1, 0, item);
            self.resizeColumnsToContents()

            if (self.rosa):
                event.setDropAction(QtCore.Qt.MoveAction)
            else:
                event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
