from PyQt4 import QtGui, QtCore
import Giocatore

class GiocatoriInsert(QtCore.QAbstractTableModel):
    def __init__(self):
        QtCore.QAbstractTableModel.__init__(self)
        self.giocatori = []
        self.giocatori.append(Giocatore.Giocatore())

    def columnCount(self, index=QtCore.QModelIndex()):
        return 5

    def rowCount(self, index=QtCore.QModelIndex()):
        return len(self.giocatori)

    def flags(self, index=QtCore.QModelIndex()):
        if (not index.isValid()):
            return QtCore.Qt.ItemIsEnabled
        
        return QtCore.QAbstractItemModel.flags(self, index) | QtCore.Qt.ItemIsEditable

    def setData(self, index, value, role= QtCore.Qt.EditRole):
        if (index.isValid() and role == QtCore.Qt.EditRole):
            if (index.column() == 0):
                self.giocatori[index.row()].cognome = value.toString().toUpper()
            elif (index.column() == 1):
                self.giocatori[index.row()].nome = value.toString().toUpper()
            elif (index.column() == 3):
                self.giocatori[index.row()].squadra = value.toString().toUpper()
            elif (index.column() == 4):
                self.giocatori[index.row()].prezzo = value
            elif (index.column() == 2):
                self.giocatori[index.row()].ruolo = value
        
            self.emit(QtCore.SIGNAL(""), self.dataChanged)
            return True
        else:
            return False

    def data(self, index, role):
        # FIXME non si ricorda il valore immesso
        if (not index.isValid()):
            return QtCore.QVariant()

        if (index.row() >= len(self.giocatori)):
            return QtCore.QVariant()

        temp = self.giocatori[index.row()]
        if (role == QtCore.Qt.TextAlignmentRole):
            return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        if (role == QtCore.Qt.DisplayRole):
            if (index.column() == 0):
                return temp.cognome
            elif (index.column() == 1):
                return temp.nome
            elif (index.column() == 2):
                if (temp.ruolo == 0):
                    return QtCore.QString("Portiere")
                elif (temp.ruolo == 1):
                    return QtCore.QString("Difensore")
                elif (temp.ruolo== 2):
                    return QtCore.QString("Centrocampista")
                elif (temp.ruolo == 3):
                    return QtCore.QString("Attaccante")
                else:
                    return QtCore.QString("")
            elif (index.column() == 3):
                return temp.squadra
            elif (index.column() == 4):
                return temp.prezzo
            else:
                return QtCore.QVariant()
  
        return QtCore.QVariant()

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        legenda = QtCore.QStringList()
        legenda.append("Cognome")
        legenda.append("Nome")
        legenda.append("Ruolo")
        legenda.append("Squadra")
        legenda.append("Prezzo")

        if (role != QtCore.Qt.DisplayRole):
            return QtCore.QVariant()

        if (orientation == QtCore.Qt.Horizontal):
            return legenda[section]

        return QtCore.QVariant()

    def insertRows(self, position, rows, index=QtCore.QModelIndex()):
        self.beginInsertRows(index, position, position+rows-1)

        for row in xrange(rows):
            self.giocatori.append(Giocatore.Giocatore())
    
        self.endInsertRows()
        return True

    def removeRows(self, position, rows, index=QtCore.QModelIndex()):
        self.beginRemoveRows(index, position, position+rows-1)

        for i in xrange(position, len(self.giocatori)-1):
            self.giocatori[i] = self.giocatori[i+1]

        self.giocatori.remove(len(self.giocatori))

        self.endRemoveRows()
        return True
