from PyQt4 import Qt, QtGui, QtCore

class PartitiModel(QtGui.QStandardItemModel):
    def __init__(self, rows, columns, contrade):
        QtGui.QStandardItemModel.__init__(self, rows, columns)
        self.contrade = contrade 

    def data(self, index, role):
        if (not index.isValid()):
            return QtCore.QVariant()

        value = QtGui.QStandardItemModel.data(self, index, role)
        
        if (role == QtCore.Qt.DecorationRole and index.column() == 0):
            i = index.sibling(index.row(), 1).data().toInt()[0];
            return Qt.QVariant(QtGui.QPixmap("../pictures/"+self.contrade[i]+".jpg").scaledToHeight(25))

        if (role == QtCore.Qt.TextAlignmentRole):
            return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        if (role == QtCore.Qt.DisplayRole and index.column() > 0):
            return value
            
