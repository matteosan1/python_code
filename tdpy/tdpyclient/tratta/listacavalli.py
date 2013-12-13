from PyQt4 import Qt, QtCore, QtGui
import listacavalli_widget
import sys

class listaCavalli(Qt.QDialog):
    
    def __init__(self, cavalli=[], parent=None):
        Qt.QDialog.__init__(self)
        self.ui = listacavalli_widget.Ui_ListaCavalli()
        self.ui.setupUi(self)
        self.cavalli = cavalli

        self.setWindowTitle("Cavalli Ammessi alla Tratta")
        self.writeEdit()

    def writeEdit(self):
        s = Qt.QString("<html><img src=\"../pictures/logo_comune.png\"><br><br>")
        # FIXME scrivici la data giusta
        s += "<div align=\"right\">Siena, XX Luglio 2008</div><br><br>"
        s += "<div align=\"center\">ELENCO CAVALLI AMMESSI ALLE BATTERIE DI SELEZIONE</div><br><br><br><br><div align\"right\">"
        
        for i, c in enumerate(self.cavalli):
            #s += Qt.QString("%1." + c.nome.toUpper()+"<br>").arg(i);
            s += Qt.QString("%1." + Qt.QString(c).toUpper()+"<br>").arg(i);
        s += "</div></html>"
  
        self.ui.textEdit.setHtml(s)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    fantini = ["Pippo", "Pluto", "Paperino", "Minni", "Gastone"]
    client = listaCavalli(fantini)
    client.show()
    sys.exit(app.exec_())


