from PyQt4 import Qt, QtCore
import strategiaprove_widget


class strategiaprove(Qt.QDialog):
    def __init__(self):
        Qt.QDialog.__init__(self)
        self.ui = strategiaprove_widget.Ui_
        self.ui.setupUi()
        
        self.connect(self.okButton, QtCore.SIGNAL("clicked()"), self.accept)
        self.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.reject)
        self.connect(self.scelta1Check, QtCore.SIGNAL("stateChanged(int)"), self.enableCombo1)
        self.connect(self.scelta2Check, QtCore.SIGNAL("stateChanged(int)"), self.enableCombo2)
        self.connect(self.scelta3Check, QtCore.SIGNAL("stateChanged(int)"), self.enableCombo3)


    def FillCombo(self, fantini, contrade, contrada, status):
        self.ui.contrada1Combo.addItems(contrade)
        self.ui.contrada2Combo.addItems(contrade)
        self.ui.contrada3Combo.addItems(contrade)

        for j,i in enumerate(fantini):
            if (status[j] == 1):
                self.ui.scelta1Combo.addItem(Qt.QPixmap(":/icons/pictures/filenew.png"), i)
                self.ui.scelta2Combo.addItem(Qt.QPixmap(":/icons/pictures/filenew.png"), i)
                self.ui.scelta3Combo.addItem(Qt.QPixmap(":/icons/pictures/filenew.png"), i)
            else:
                self.ui.scelta1Combo.addItem(i)
                self.ui.scelta2Combo.addItem(i)
                self.ui.scelta3Combo.addItem(i)
        
        self.ui.contradaLabel.setText(contrada.getContrada().nomeCompleto())
        monta = Qt.QString()
        if (contrada.getFantino() != 0):
            monta = contrada.getFantino().nome()
        else:
            monta = "nessun fantino scelto."

        self.ui.montaLabel.setText("Monta attuale: "+monta)
        self.ui.cavalloLabel.setText(contrada.getCavallo().nome())
        self.ui.formaBar.setTextVisible(True)
        # FIXME ci vorra` anche il range ?????
        #self.ui.formaBar.setRange(0, 100)
        self.ui.formaBar.setValue(contrada.forma())

        strategia = Qt.QStringList()
        strategia << "Mossa" << "Spunto" << "Curve"

        #for i in contrade:
        #    strategia.append("Ostacola " + i.nome)
        self.ui.primaCombo.addItems(strategia)
        self.ui.secondaCombo.addItems(strategia)
        self.ui.terzaCombo.addItems(strategia)
        self.ui.quartaCombo.addItems(strategia)
        self.ui.generaleCombo.addItems(strategia)
        self.ui.acciaCombo.addItems(strategia)

    def enableCombo1(self, state):
        self.ui.contrada1Combo.setEnabled(state)

    def enableCombo2(self, state):
        self.ui.contrada2Combo.setEnabled(state)

    def enableCombo3(self, state):
        self.ui.contrada3Combo.setEnabled(state)


