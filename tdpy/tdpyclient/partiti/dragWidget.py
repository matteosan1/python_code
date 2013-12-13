from PyQt4 import Qt, QtCore, QtGui

class DragWidget(Qt.QFrame):
    
    def __init__(self, parent=None):
        Qt.QFrame.__init__(self, parent)
        self.setFrameStyle(Qt.QFrame.Sunken | Qt.QFrame.StyledPanel)
        self.setAcceptDrops(True);

    def dragEnterEvent(self, event):
        if (event.mimeData().hasFormat("text/plain")):
            if (event.source() == self):
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if (event.mimeData().hasFormat("text/plain")):
            if (event.source() == self):
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        event.ignore()
     
    def mousePressEvent(self, event):
        if (self.childAt(event.pos()) == None):
            return
        #child = Qt.QLabel(self.childAt(event.pos()))
        index = self.childAt(event.pos()).objectName()
        #pixmap = Qt.QPixmap(child.pixmap())

        itemData = Qt.QByteArray()
        dataStream = Qt.QDataStream(itemData, Qt.QIODevice.WriteOnly)
        dataStream << index #pixmap << Qt.QPoint(event.pos() - child.pos())
        
        mimeData = Qt.QMimeData()
        mimeData.setData("text/plain", itemData)
        
        drag = Qt.QDrag(self)
        drag.setMimeData(mimeData)
        # FIXME migliora
        #drag.setPixmap(pixmap)
        #drag.setHotSpot(event.pos() - child.pos())
        
        #temp = Qt.QPixmap(pixmap)
        #painter = Qt.QPainter()
        #painter.begin(temp)
        #painter.fillRect(pixmap.rect(), Qt.QColor(127, 127, 127, 127));
        #painter.end()
        
        #child.setPixmap(temp)
        drag.exec_()
        #if (drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction, QtCore.Qt.CopyAction) == QtCore.Qt.MoveAction):
        #    child.close()
        #else:
        #    child.show()
        #    child.setPixmap(pixmap)
