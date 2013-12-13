from PyQt4 import Qt, QtCore, QtGui

class DragTableView(Qt.QTableView):
    
    def __init__(self, parent=None):
        Qt.QTableView.__init__(self, parent)
        self.setAcceptDrops(True);

    def dragEnterEvent(self, event):
        if (event.mimeData().hasFormat("text/plain")):
            if (event.source() == self):
                event.ignore()
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
        if (event.mimeData().hasFormat("text/plain")):
            itemData = Qt.QByteArray(event.mimeData().data("text/plain"))
            dataStream = Qt.QDataStream(itemData, Qt.QIODevice.ReadOnly)
            # FIXME
            #pixmap = Qt.QPixmap()
            #offset = Qt.QPoint()
            val = Qt.QString()
            dataStream >> val# >> offset

            # Aggiungere un elemento alla tabella
            self.model().insertRow(self.model().rowCount())
            for i in xrange(5):
                index = self.model().index(self.model().rowCount()-1, i)
                if (i == 0):
                    self.model().setData(index, Qt.QVariant())
                if (i == 1):
                    self.model().setData(index, val.toInt()[0])
                if (i == 2):
                    self.model().setData(index, "Vai Piano !")
                if (i == 3):
                    self.model().setData(index, "")
                if (i == 4):
                    self.model().setData(index, 10)

            if (event.source() == self):
                event.ignore()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()
