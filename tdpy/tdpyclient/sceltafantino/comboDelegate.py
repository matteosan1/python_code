from PyQt4 import Qt, QtGui, QtCore

class ComboDelegate(QtGui.QItemDelegate):
    
    def __init__(self, parent=None):
        QtGui.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        editor = QtGui.QComboBox(parent)
        editor.addItem("---------")
        editor.addItem("A Vincere")
        editor.addItem("A Correre")
        editor.addItem("A Vendere")
        editor.addItem("Killer...")
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.DisplayRole).toInt()
        editor.setCurrentIndex(value[0])

    def setModelData(self, editor, model, index):
        value = editor.currentIndex()
        model.setData(index, editor.itemText(value))

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
    
