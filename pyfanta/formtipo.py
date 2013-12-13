from PyQt4 import QtGui, QtCore
import ui_formtipo

class FormTipo(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = ui_formtipo.Ui::Dialog()
        self.giocatori = g
        self.punteggi = p
        #QStringList list, nomi;
        #QGraphicsScene* scene;
        #QList<QPair<QString, float> > pairs[3];
        #int n[3];
        self.ui.setupUi(this);

        scene = QtGui.QGraphicsScene(parent)
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.show()
        self.setCampo()
        
        # FIXME ci sono in punteggi...
        lista = QtCore.QStringList()
        lista.append....<< "6-3-1" << "5-4-1" << "5-3-2" << "4-5-1"
            << "4-4-2" << "4-3-3" << "3-5-2" << "3-6-1" << "3-4-3";

            for(int i=0; i<9; ++i)
            if (punt->schemi[i] == 0)
            list.removeAt(i);

    self.fillCombo()
    self.ordina()
    QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeFormazione)


    def changeFormazione(self, a):
        l = self.lista[a].split("-")

        for(int j=0; j<3; ++j)
        n[j] = l[j].toInt();
        for(int i=0; i<n[j]; ++i)
            nomi << pairs[j][i].first;

    def ordina(self):
    QPair<QString, float> temp;

    for(int j=0; j<3; ++j) {
        for(unsigned int i=0; i<giocatori.size(); ++i)
            if (giocatori[i].GetRuolo() == j+1) {
                temp.first = giocatori[i].GetCognome();
                temp.second = giocatori[i].GetMedia(punt);
                pairs[j].push_back(temp);
            }
    }

    // cambiare ordinamento in base anche al numero di partite giocate
    for(int j=0; j<3; ++j) {
        for(int i=0; i<pairs[j].size()-1; ++i) {
            for(int y=i+1; y<pairs[j].size(); ++y) {
                if (pairs[j][i].second < pairs[j][y].second)
                    pairs[j].swap(i, y);
            }
        }
    }
}

def fillCombo(self):
self.ui.comboBox.insertItems(0, self.lista)


def setScene(self):
    scene->addText("Matteo");
    scene->addText("Matteo");
    //
    scene->addText("Matteo");
    //
    scene->addText("Matteo");
    //
    scene->addText("Matteo");
    //
    scene->addText("Matteo");
    //
    scene->addText("Matteo");
    //
    scene->addText("Matteo");
    //
    scene->addText("Matteo");

//    1
//  1 1 1  (2)
// 1 1 1 1 (2)
//   1 1   (1)

//   1 1   (1)
//  1 1 1  (2)
// 1 1 1 1 (2)

//   1   (1)
//  1 1  (2)
}

def setCampo(self):

    self.scene.setBackgroundBrush(QtGui.Qt.green)
    //scene->addLine();
    //scene->addCircle();
    //scene->addLine();
    //scene->addLine();
    //scene->addLine();

