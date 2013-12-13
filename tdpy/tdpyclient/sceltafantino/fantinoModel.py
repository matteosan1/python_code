from PyQt4 import Qt, QtGui, QtCore
import resource_rc

class FantinoModel(QtGui.QStandardItemModel):
    def __init__(self, rows, columns):
        QtGui.QStandardItemModel.__init__(self, rows, columns)

    def data(self, index, role):
        if (not index.isValid()):
            return QtCore.QVariant()

        value = QtGui.QStandardItemModel.data(self, index, role)

        #FIXME
        #if (role == QtCore.Qt.TextAlignmentRole):
        #    return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        if (role == QtCore.Qt.BackgroundRole):
            temp = index.sibling(index.row(), 6).data(QtCore.Qt.DisplayRole)
            if (temp.toString() == "Killer..."):
                return QtGui.QColor(QtCore.Qt.darkRed)
            if (temp.toString() == "A Vincere"):
                return QtGui.QColor(QtCore.Qt.darkYellow)
            if (temp.toString() == "A Correre"):
                return QtGui.QColor(QtCore.Qt.lightGray)
            if (temp.toString() == "A Vendere"):
                return QtGui.QColor(QtCore.Qt.darkGreen)

        if (role == QtCore.Qt.DisplayRole and index.column() != 4):
                return value

        if (role == QtCore.Qt.DecorationRole and index.column() == 4):
            mix = value.toFloat()
            capacita = (mix[0]/100)%100
            media = mix[0] - capacita*100
            if (capacita > 0):
                return Qt.QVariant(QtGui.QIcon(":/status/pictures/killer.bmp"))
            else:
                if (media > 6.0):
                    return Qt.QVariant(QtGui.QIcon(":/status/pictures/buono.bmp"))
                elif (media < 4.0):
                    return Qt.QVariant(QtGui.QIcon(":/status/pictures/scarso.bmp"))                  
                else:
                    return Qt.QVariant(QtGui.QIcon(":/status/pictures/suff.bmp"))

