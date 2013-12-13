from PyQt4 import Qt, QtGui, QtCore

class ComboDelegate(QtGui.QItemDelegate):
    
    def __init__(self, items, parent=None):
        QtGui.QItemDelegate.__init__(self, parent)
        self.items = items

    def createEditor(self, parent, option, index):
        editor = QtGui.QComboBox(parent)
        for i in self.items:
            editor.addItem(i)

        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.DisplayRole).toInt()
        editor.setCurrentIndex(value[0])

    def setModelData(self, editor, model, index):
        value = editor.currentIndex()
        model.setData(index, editor.itemText(value))

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
    
