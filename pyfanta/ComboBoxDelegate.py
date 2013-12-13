from PyQt4 import QtGui, QtCore

class ComboBoxDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
        QtGui.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        lista = QtCore.QStringList()
        lista.append("Portiere")
        lista.append("Difensore")
        lista.append("Centrocampista")
        lista.append("Attaccante")

        editor = QtGui.QComboBox(parent)
        editor.insertItems(0, lista);
        
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.DisplayRole).toInt()
        editor.setCurrentIndex(value[0])

    def setModelData(self, editor, model, index):
        value = editor.currentIndex()
        model.setData(index, value)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

