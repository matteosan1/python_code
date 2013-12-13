from PyQt4 import Qt, QtGui, QtCore

class SpinBoxDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
        QtGui.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        editor = QtGui.QSpinBox(parent)
        editor.setMinimum(0)
        editor.setMaximum(1000)        
        return editor;
        
    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.DisplayRole).toInt()[0]
        editor.setValue(value)
    
    def setModelData(self, editor, model, index):
        value = editor.value()
        model.setData(index, value, QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
