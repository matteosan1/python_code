from PyQt4 import Qt, QtGui, QtCore

class ReadOnlyDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
        QtGui.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        return None;
        
