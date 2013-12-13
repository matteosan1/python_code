from PyQt4 import QtCore, QtGui

class Giocatori(QtCore.QAbstractTableModel):
  def __init__(self, s, b = False):
    QtCore.QAbstractTableModel.__init__(self)
    self.stringList = QtCore.QStringList()
    self.squadra = s
    self.toggle = b

  def columnCount(self, parent):
    if (not self.toggle):
        return self.squadra.giornata
    else:
        return 8;

  def rowCount(self, parent):
    if (not self.toggle):
      rows = len(self.squadra.giocatori) + 2
      return rows;
    else:
      return len(self.squadra.giocatori)

  def data(self, index, role):
    if (not index.isValid()):
      return QtCore.QVariant()

    if (role == QtCore.Qt.TextAlignmentRole):
      return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    if (index.row() < len(self.squadra.giocatori)):
      temp = self.squadra.giocatori[index.row()]

      if (role == QtCore.Qt.FontRole):
        if self.toggle:
          return QtGui.QFont("Sans Serif", 10)
        else:
          if (self.squadra.haGiocato(index.column()+1, index.row()) != 1):
            return QtGui.QFont("Sans Serif", 8)
          else:
            return QtGui.QFont("Sans Serif", 12, QtGui.QFont.Bold)
        
      if (not self.toggle):
        if (role == QtCore.Qt.ForegroundRole):
          if (temp.haSegnato(index.column()+1)):
            return QtGui.QColor(QtCore.Qt.darkRed)
          
        if (role == QtCore.Qt.BackgroundRole):
          if (temp.ammonito(index.column()+1)):
            return QtGui.QColor(QtCore.Qt.yellow)
          if (temp.espulso(index.column()+1)):
            return QtGui.QColor(QtCore.Qt.red)
              
    if (role == QtCore.Qt.DisplayRole):
      if (index.row() < len(self.squadra.giocatori)):
        temp = self.squadra.giocatori[index.row()]

        if (not self.toggle):
          voto = temp.voto(index.column()+1, self.squadra.punteggi)
          if (temp.prestazioni[index.column()+1][1][0] != 0):
            return QtCore.QString("%1").arg(voto)
          else:
            return QtCore.QString("")
        else:
          if (index.column() == 0):
            # FIXME metti colori se < 6, se > 6 se > 8
            if (temp.media(self.squadra.punteggi) != 0):
              return QtCore.QString("%1").arg(temp.media(self.squadra.punteggi), 0, 'f', 2)
            else:
              return QtCore.QString("-")
          elif (index.column() == 1):
            return QtCore.QString("%1").arg(temp.giocate())
          elif (index.column() == 2):
            return QtCore.QString("%1").arg(self.squadra.presenze(index.row()))
          elif (index.column() == 3):
            if temp.ammonizioni() != 0:
              return QtCore.QString("%1").arg(temp.ammonizioni())
          elif (index.column() == 4):
            if temp.espulsioni() != 0:
              return QtCore.QString("%1").arg(temp.espulsioni())
          elif (index.column() == 5):
            if temp.goal() != 0:
              return QtCore.QString("%1").arg(temp.goal())
          elif (index.column() == 6):
            if temp.autogoal() != 0:
              return QtCore.QString("%1").arg(temp.autogoal())
          elif (index.column() == 7):
            return QtCore.QString("%1").arg(temp.rigori())
          else:
            return QtCore.QVariant()
        
      if (index.row() == len(self.squadra.giocatori)):
          return QtCore.QString("%1").arg(self.squadra.schemaPerGiornata(index.column()+1))

      if (index.row() == len(self.squadra.giocatori)+1):
          return QtCore.QString("%1").arg(self.squadra.totale(index.column()+1)[-1], 0, 'f', 1)
     
    return QtCore.QVariant()


  def headerData(self, section, orientation, role):
    items = ["Media" , "Giocate" , "Presenze" , "Ammonizioni" , "Espulsioni" , "Goal" , "Autogoal" , "Rigori"]
    legenda = QtCore.QStringList()
    for i in items:
      legenda.append(i)

    if (section < len(self.squadra.giocatori)):
      temp = self.squadra.giocatori[section]
      if (role == QtCore.Qt.BackgroundRole and orientation == QtCore.Qt.Vertical):
        if (temp.ruolo == 0):
          return QtGui.QColor(QtCore.Qt.green)
        if (temp.ruolo == 1):
          return QtGui.QColor(QtCore.Qt.cyan)
        if (temp.ruolo == 2):
          return QtGui.QColor(QtCore.Qt.gray)
        if (temp.ruolo == 3):
          return QtGui.QColor(QtCore.Qt.blue)
        if (temp.ruolo > 4):
          return QtGui.QColor(QtCore.Qt.magenta)

    if (role != QtCore.Qt.DisplayRole):
      return QtCore.QVariant()

    if (orientation == QtCore.Qt.Horizontal):
      if (not self.toggle):
        return QtCore.QString("Giornata %1").arg(section+1)
      else:
        return legenda[section]
    else:
      if (not self.toggle):
        if (section == len(self.squadra.giocatori)):
          return QtCore.QString("SCHEMA")

        if (section == len(self.squadra.giocatori)+1):
          return QtCore.QString("PUNTEGGI")
        
      if (section < len(self.squadra.giocatori)):
        temp = self.squadra.giocatori[section];
        return temp.nomeCompleto()
        
    return QtCore.QVariant()


