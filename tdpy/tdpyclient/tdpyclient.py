#! /usr/bin/python

from PyQt4 import Qt, QtGui, QtCore, QtNetwork

import tdpyclient_widget
import contrada, giocatore, barbero, cavallo, fantino
import splash.splash, tratta.tratta
import sceltafantino.sceltafantino
import connection.serverconnection
import nuovoGioco.caricagioco
import tdpsocket
import os, sys

class tdpyClient(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = tdpyclient_widget. Ui_MainWindow()
        self.ui.setupUi(self)
        self.socket_number = -1;
        self.setWindowTitle("Tempo di Palio II")
        self.tcpSocket = tdpsocket.Socket()
        self.tcpSocket.userName = self.getUserName()
        self.connect(self.tcpSocket, QtCore.SIGNAL("connected()"), self.ready)
        self.connect(self.tcpSocket, QtCore.SIGNAL("readyRead()"), self.readMessage)
        self.connect(self.tcpSocket, QtCore.SIGNAL("disconnected()"), self.serverHasStopped)
        self.connect(self.tcpSocket, QtCore.SIGNAL("error(QAbstractSocket::SocketError)"), self.serverHasError)
        self.connect(self.tcpSocket, QtCore.SIGNAL("stateChanged (QAbstractSocket::SocketState)"), self.statoSocket)
    
        self.nome_giochi = []
        self.data_giochi = []

        self.textStatus = Qt.QTextEdit()
        self.textStatus.setReadOnly(True)
        self.ctrlM = Qt.QShortcut(Qt.QKeySequence("Ctrl+M"), self)
        self.esc = Qt.QShortcut(Qt.QKeySequence("Esc"), self)
        self.ui.chatEdit.ensureCursorVisible()
        self.connect(self.ctrlM, QtCore.SIGNAL("activated()"), self.apriChat)
        self.connect(self.esc, QtCore.SIGNAL("activated()"), self.chiudiChat)
        self.connect(self.ui.lineEdit_chat, QtCore.SIGNAL("returnPressed()"), self.scriviChat)
        self.chiudiChat()
        self.listaChat = []

        self.ui.statusbar.addPermanentWidget(self.textStatus, 1)
        self.ui.statusbar.setSizeGripEnabled(False);
         #ui.actionSpettatore->setEnabled(false);
        #ui.actionAvvia_gioco->setEnabled(false);
        #ui.actionScegli_Contrada->setEnabled(false);
        #self.connect(self.fase, SIGNAL("nuovaFase"), self.nuovaFase)
        #connect(ui.actionConnessione, SIGNAL(activated()), this, SLOT(openConnection()));
        #connect(ui.actionScegli_Contrada, SIGNAL(activated()), this, SLOT(chooseContrada()));
        #connect(ui.actionAvvia_gioco, SIGNAL(activated()), this, SLOT(startGame()));
        #connect(ui.actionSpettatore, SIGNAL(activated()), this, SLOT(becomeSpectator()));
        self.connect(self.ui.actionNew, QtCore.SIGNAL("activated()"), self.fileNew)
        self.ui.actionNew.setEnabled(False)    
        self.connect(self.ui.actionOpen, QtCore.SIGNAL("activated()"), self.joinGioco)
        self.ui.actionOpen.setEnabled(False)    
        #connect(ui.actionSave, SIGNAL(activated()), this, SLOT(fileSave()));
        #connect(ui.actionSave_As, SIGNAL(activated()), this, SLOT(fileSaveAs()));
        #connect(ui.actionPrint, SIGNAL(activated()), this, SLOT(filePrint()));
        #connect(ui.actionExit, SIGNAL(activated()), this, SLOT(close()));
        #connect(ui.actionInserisci_Giocatore, SIGNAL(activated()), this, SLOT(nuovoGiocatore()));
        #connect(ui.aiutoInformazioniAction, SIGNAL(activated()), this, SLOT(aiutoInformazioni()));
        #connect(ui.aiutoAiutoAction, SIGNAL(activated()), this, SLOT(help()));
        #connect(ui.actionEffetti_sonori, SIGNAL(toggled(bool)), this, SLOT(abilitaSuono(bool)));
        self.connect(self.ui.actionAvanti, QtCore.SIGNAL("activated()"), self.ready)
        #connect(ui.actionContrada, SIGNAL(activated()), this, SLOT(visualizzaStatusContrada()));
        #connect(ui.actionVittorie, SIGNAL(activated()), this, SLOT(visualizzaTabellaVittorie()));
        #connect(ui.actionCuffia, SIGNAL(activated()), this, SLOT(visualizzaTabellaCuffie()));
        #connect(ui.actionFantini, SIGNAL(activated()), this, SLOT(visualizzaTabellaFantini()));
        #connect(ui.actionCavalli, SIGNAL(activated()), this, SLOT(visualizzaTabellaCavalli()));

        #FIXME chat dialog
        self.ui.label_pngContrada.setText(Qt.QString(""))
        self.ui.label_nomeContrada.setText("")
        self.ui.label_carica.setText("Mandato: -")
        self.ui.label_gradimento.setText("Umore: --%")
        self.ui.label_fantino.setText("Fantino:")
        self.ui.label_fantinoCorsi.setText("Corsi: -")
        self.ui.label_fantinoVinti.setText("Vinti: -")
        self.ui.label_cavallo.setText("Cavallo:")
        self.ui.label_cavalloCorsi.setText("Corsi: -")
        self.ui.label_cavalloVinti.setText("Vinti: -")
        self.ui.progressBar_forma.setValue(0)
        self.ui.tableWidget_contrade.setRowCount(10)
        self.ui.tableWidget_contrade.setColumnCount(3)
        self.ui.tableWidget_contrade.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_contrade.setSelectionMode(Qt.QAbstractItemView.NoSelection)
        self.ui.tableWidget_contrade.verticalHeader().hide()
        self.ui.tableWidget_contrade.horizontalHeader().hide()
        self.ui.tableWidget_contrade.setRowHeight(0, 20)
        self.ui.tableWidget_contrade.setColumnWidth(0, 24)
        self.ui.tableWidget_contrade.resizeRowsToContents()
        #self.ui.tableWidget_contrade.setFocusPolicy(Qt.NoFocus)
  
        #if (QSound::isAvailable()):
        #    soundWanted  = true
        #else:
        #    QMessageBox::warning(this,"Errore impostazione suono.", "Spiacente, nessuna scheda sonora disponibile.");
    
        #    ui.actionEffetti_sonori->setChecked(false)
        #    ui.actionEffetti_sonori->setEnabled(false)
        #    soundWanted = false
  
        
        #myStreamer = new MyStreamer();
        #self.openConnection();

    def ready(self):
        self.sendMessage(["Ready",])

    def statoSocket(self):
        pass

    def estrazione(self, list_):
        posx = (140, 190, 240, 290, 340, 390, 440, 490, 550, 625, 190, 240, 290, 340, 390, 440, 490)
        posy = (440, 440, 440, 440, 440, 440, 440, 440, 440, 440, 220, 220, 220, 220, 220, 220, 215)
  
        self.ui.statusbar.showMessage("Estrazione delle Contrade")
        #self.ui.label.show()
  
        bandiere = [Qt.QGraphicsPixmapItem() for i in xrange(17)]
        scene = Qt.QGraphicsScene(self.ui.frame)

        palazzo = scene.addPixmap(Qt.QPixmap(Qt.QString(":/estrazione/pictures/palazzo_comunale.png")));
        palazzo.setPos(0,0)

        for i in xrange(17):
            s = Qt.QString(":/estrazione/pictures/" + list_[i] + "_1.gif")
            bandiere[i] = scene.addPixmap(Qt.QPixmap(s))
            bandiere[i].setPos(posx[i], posy[i])

        scene.setSceneRect(0, 0, 906, 616);
        #self.ui.graphicsView.setRenderHint(Qt.QPainter.Antialiasing)
        #self.ui.graphicsView.setCacheMode(Qt.QGraphicsView.CacheBackground)
        #self.ui.graphicsView.setDragMode(Qt.QGraphicsView.ScrollHandDrag)
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.scale(float(self.ui.graphicsView.width())/906., float(self.ui.graphicsView.height())/616.)
        self.ui.graphicsView.show()
  
        for i in xrange(7):
            bandiere[i].show()
  
        #if (self.soundWanted):
            #Qt.QSound.play("../tdpalioclient/sound/chiarine.wav")
            #FIXME
            #sleep(10)
  
        for i in xrange(7,10):
            bandiere[i].show()
            #sleep(3)

        self.aggiornaContradeTable(1, list_)
        # FIXME attiva tasto di avanzamento

    def assegnazione(self, ass, c, cav):
        posx = (130, 130, 130, 128, 128, 590, 590, 590, 590, 590)
        posy = (220, 258, 298, 337, 377, 218, 258, 296, 336, 376)
        posx_contrada = (170, 170, 170, 170, 170, 627, 627, 627, 627, 627)
        posy_contrada = (220, 260, 300, 340, 380, 218, 258, 298, 338, 378)

        self.ui.statusbar.showMessage("Assegnazione")
        #self.ui.label.show()

        scene = Qt.QGraphicsScene(self.ui.frame)
        tabellone = scene.addPixmap(Qt.QPixmap(Qt.QString("pictures/tabellone.jpg")));
        tabellone.setPos(0,0)
  
        coscia = [Qt.QGraphicsPixmapItem() for i in xrange(10)]
        contrade = [Qt.QGraphicsPixmapItem() for i in xrange(10)]

        for i in xrange(10):
            s = Qt.QString("pictures/tabellone_" +str(ass[i][1]) + ".png")
            pixmap = Qt.QPixmap(s)
            pixmap = pixmap.scaled(30,30)
            coscia[i] = scene.addPixmap(pixmap)
            coscia[i].setPos(posx[ass[i][0]], posy[ass[i][0]])
            s = Qt.QString("pictures/tabellone_" + c[ass[i][3]].toLower() + ".png")
            contrade[i] = scene.addPixmap(Qt.QPixmap(s))
            contrade[i].setPos(posx_contrada[ass[i][0]], posy_contrada[ass[i][0]])

        scene.setSceneRect(0, 0, 906, 616);
        #self.ui.graphicsView.setRenderHint(Qt.QPainter.Antialiasing)
        #self.ui.graphicsView.setCacheMode(Qt.QGraphicsView.CacheBackground)
        #self.ui.graphicsView.setDragMode(Qt.QGraphicsView.ScrollHandDrag)

        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.scale(float(self.ui.graphicsView.width())/906., float(self.ui.graphicsView.height())/616.)
        self.ui.graphicsView.show()
  
        for i in xrange(10):
            contrade[i].show()
  
        #if (self.soundWanted):
            #Qt.QSound.play("../tdpalioclient/sound/chiarine.wav")
            #FIXME
            #sleep(10)
  
        for i in xrange(10):
            coscia[i].show()

        self.aggiornaContradeTable(1, c)
        self.aggiornaContradeTable(2, cav)
        # FIXME attiva tasto di avanzamento
        
    def aggiornaContradeTable(self, type, list_):
        if (type == 1):
            for i in xrange(10):
                s = Qt.QString("pictures/barbero_"+list_[i].toLower()+"_small.png")
                item = Qt.QTableWidgetItem(Qt.QIcon(s), "")
                self.ui.tableWidget_contrade.setItem(i, 0, item)
        elif (type == 2):
            for i in xrange(10):
                item = Qt.QTableWidgetItem(list_[i])
                #item.setForeground(Qt.blue)
                self.ui.tableWidget_contrade.setItem(i, 1, item)
        elif (type == 3):
            for i in xrange(10):
                item = Qt.QTableWidgetItem(list_[i])
                #item.setForeground(Qt.blue)
                self.ui.tableWidget_contrade.setItem(i, 2, item)

    def aggiornaContradaPanel(self, c, g):
        s = Qt.QString("./pictures/barbero_"+c.nome.toLower()+"_big.png")
        self.ui.label_pngContrada.setPixmap(Qt.QPixmap(s))
        self.ui.label_nomeContrada.setText(c.nomeCompleto)
        s = Qt.QString("Mandato: %1").arg(g.tempo_in_carica)
        self.ui.label_carica.setText(s)
        s = Qt.QString("Umore: %1 %").arg(c.status[3])
        self.ui.label_gradimento.setText(s)

    def aggiornaCavalloPanel(self):
        self.ui.label_cavallo.setText("Cavallo: "+ self.cavallo.nome)
        s = Qt.QString("Corsi: %1").arg(self.cavallo.score[2])
        self.ui.label_cavalloCorsi.setText(s)
        s = Qt.QString("Vinti: %1").arg(self.cavallo.score[3])
        self.ui.label_cavalloVinti.setText(s); 
        self.ui.progressBar_forma.setValue(self.cavallo.forma*10)

    def sceltaCavalli(self, cavalli):
        t = tratta.tratta.tratta(cavalli)
        t.exec_()
        self.sendMessage(["SceltaCavalli", t.getSelection()])

    def sceltaFantino(self, fantini):
        f = sceltafantino.sceltafantino.sceltafantino(self.barbero.indice, fantini)
        o = []
        if (f.exec_() == Qt.QDialog.Accepted):
            o = f.offerte

        self.sendMessage(["SceltaFantini"], o)

    def decidiFantino(self, offerte):
        if (len(offerte) == 0):
            message = Qt.QString("Spiacente, ma nessuna delle tue offerte e` stata accettata.")
            print message
            Qt.QMessageBox.information (self, "TdPalio II", message)                
            self.sendMessage(["FantinoDeciso"], -1)
        else:
            d = sceltafantino.decisionefantino.decisionefantino(self, fantini, offerte)
            d.exec_()
            if (d.offerta != -1):
                self.sendMessage(["FantinoDeciso"], offerte[o].fantino)
            else:
                self.sendMessage(["FantinoDeciso"], -1)

    def battesimo(self):
        titolo = Qt.QString("")
        text = ["", False]
        while(not text[1] or text[0].isEmpty()):
            text = Qt.QInputDialog.getText(self, "Segnatura del Fantino", titolo + Qt.QString("\nNome di Battaglia:"), Qt.QLineEdit.Normal,       Qt.QDir.home().dirName())
            
            if (not text[1] or text[0].isEmpty()):
                Qt.QMessageBox.critical(self, "TDPalio Error", "Non puoi non specificare un nome !", Qt.QMessageBox.Ok)
            else:
                self.sendMessage(["Nome Al Fantino", text[0]])

    def apriChat(self):
        item = Qt.QInputDialog.getItem(self, "Chat", "Contrada",  self.listaChat, 0, False)
        list1 = Qt.QStringList(item[0].split(" -"))
        self.chatPeer = list1[0]
        if (item[1] and not item[0].isEmpty()):
            self.ui.lineEdit_chat.setEnabled(True)
            self.ui.chatEdit.setVisible(True)
            self.ui.lineEdit_chat.setVisible(True)  
            self.ui.lineEdit_chat.setFocus()
    
    def chiudiChat(self):
        self.ui.lineEdit_chat.setEnabled(False)
        self.ui.chatEdit.setVisible(False)
        self.ui.lineEdit_chat.setVisible(False)
        self.ui.lineEdit_chat.setText("")
        self.chatPeer = ""

    def scriviChat(self):
        real_text  = Qt.QString(giocatore.userName() + ": " + self.ui.lineEdit_chat.text() + "<br>")

        self.ui.chatEdit.setTextColor(Qt.blue)
        self.ui.chatEdit.insertHtml(real_text)
        self.ui.lineEdit_chat.setText("")
        # FIXME 
        #QString total_text = ui.lineEdit_chat->toHtml();
        #total_text = total_text("<a name=\"end\"", "");
        #ui.chatEdit->insertHtml(real_text);
        self.sendMessage(["ScriviChat",  self.chatPeer,  self.tcpSocket.userName,  real_text])
    
    def joinGioco(self):
        self.sendMessage(["Join Gioco Corrente"])
  
    def leggiChat(self,  s):
        self.ui.lineEdit_chat.setEnabled(True)
        self.ui.chatEdit.setVisible(True)
        self.ui.lineEdit_chat.setVisible(True)
        self.ui.lineEdit_chat.setFocus()
        self.ui.chatEdit.setTextColor(Qt.red)
        self.ui.chatEdit.insertHtml(s[1]+": "+s[2])
        self.chatPeer = s[1]

    def fileNew(self):
        cg = nuovoGioco.caricagioco.caricaGioco()
        cg.setVariables(self.nome_giochi, self.data_giochi)
        number_int = cg.exec_()
        if (number_int == 3):
            return
        elif (number_int == 2):
            text_string = cg.nomi[cg.getSelection()]
        else:
            dial = Qt.QInputDialog.getText(self, "Nuovo Gioco", "Nome")
            if (not dial[1] or dial[0].isEmpty()):
                text_string = "----"
            else:
                text_string = dial[0]
        self.sendMessage(["Gioco Scelto",  text_string])

    def openConnection(self):
        while (1):
            # FIXME
            sc = connection.serverconnection.serverConnection()
            if(sc.exec_() == Qt.QDialog.Accepted):
                if (sc.local == 1):
                    pass
                    # FIXME in qualche modo va settato il path
                    # FIXME controlla se localmente c'e` gia` un server che gira
                    #QString arg1 = "tdpalioserver &";
                    #system(arg1.toLatin1());
                self.tcpSocket.connectToHost(sc.host_, sc.port_)
            
                if (self.tcpSocket.state() != QtNetwork.QAbstractSocket.UnconnectedState):
                    #self.connect(self.tcpSocket, QtCore.SIGNAL("readyRead()"), self.readMessage())
                    #self.connect(self.tcpSocket, QtCore.SIGNAL("error(QAbstractSocket::SocketError)"), self.displayError());                    
                    break
                else:
                    sys.exit(1000)

    def getUserName(self):    
        if (not os.path.isdir(os.path.expanduser("~")+"/.tdpyrc")):
            text = QtGui.QInputDialog.getText(self, "Benvenuto a Tempo di Palio II online", "User name:", Qt.QLineEdit.Normal)

            if (text[1]):
                userName = text[0]
                os.makedirs(os.path.expanduser("~")+"/.tdpyrc")
                file = open(os.path.expanduser("~")+"/.tdpyrc/userData", "w")
                file.write(userName)
                file.close()
                return userName
        else:
            file = open(os.path.expanduser("~")+"/.tdpyrc/userData")
            userName = file.readline()
            file.close()
            return userName

    def sendMessage(self, message):
        request = Qt.QByteArray()
        stream = Qt.QDataStream(request, Qt.QIODevice.WriteOnly)
        stream.setVersion(Qt.QDataStream.Qt_4_2)
        stream << Qt.QString(message[0])
        if (message[0] == "SceltaCavalli"):
            stream.writeInt16(len(message[1]))
            for i in message[1]:
                stream.writeInt16(i)
        
        elif (message[0] == "Ready"):
            pass
        
        elif (message[0] == "Join Gioco Corrente"): 
            pass

        elif (message[0] == "Not Join Gioco Corrente"):
            pass

        elif (message[0] == "Gioco Scelto"):
            stream << Qt.QString(message[1])
    
        elif (message[0] == "Contrada Scelta"):
            stream << Qt.QString(message[1])
            
        elif (message[0] == "UserName"):
            stream << Qt.QString(self.tcpSocket.userName)

        elif (message[0] == "SceltaFantino"):
            stream.writeInt16(len(message[1]))
            for i in message[1]:
                i.outStreamer(stream)
    
        elif (message[0] == "FantinoDeciso"):
            stream.writeInt16(message[1])
     
        elif (message[0] == "StrategiaProva"):
            self.barbero.outStreamer(stream)
      
        elif (message[0] == "Partiti"):
            stream.writeInt16(len(message[1]))
            for i in message[1]:
                i.outStreamer(stream)
	
        elif (message[0] == "DecisionePartiti"):
            self.barbero.outStreamer(stream)
    
        self.tcpSocket.write(request)
    
    def readMessage(self):
        while (self.tcpSocket.bytesAvailable() > 0):
            stream = Qt.QDataStream(self.tcpSocket)
            stream.setVersion(Qt.QDataStream.Qt_4_2)
            codice = Qt.QString()
            stream >> codice
            print codice

            if (codice == "SceltaCavalli"):
                cavalli = list()
                for i in xrange(21):
                    c = cavallo.Cavallo()
                    c.inStreamer(stream)
                    cavalli.append(c)
                self.sceltaCavalli(cavalli)
            
            elif (codice == "AggiornaTutto"):
                temp = []
                s = Qt.QString()
                for i in xrange(10):
                    stream >> s
                    temp.append(s)
                self.aggiornaContradeTable(1, temp)
                temp = []
                for i in xrange(10):
                    stream >> s
                    temp.append(s)
                self.aggiornaContradeTable(1, temp)
                temp = []
                for i in xrange(10):
                    stream >> s
                    temp.append(s)
                self.aggiornaContradeTable(1, temp)

            elif (codice == "Assegnazione"):
                ass = []
                barberi = []
                cav = []
                for i in xrange(10):
                    ass.append([stream.readInt16(),stream.readInt16(),stream.readInt16(),stream.readInt16()])
                for i in xrange(10):
                    nome = Qt.QString()
                    stream >> nome
                    barberi.append(nome)
                for i in xrange(10):
                    nome = Qt.QString()
                    stream >> nome
                    cav.append(nome)
                self.assegnazione(ass, barberi, cav)

            elif (codice == "Conferma Contrada"):
                c = contrada.Contrada()
                c.inStreamer(stream)
                g = giocatore.Giocatore()
                g.inStreamer(stream)
                self.aggiornaContradaPanel(c, g)
            
            elif (codice == "Message Box"):
                message = Qt.QString()
                print message
                stream >> message
                Qt.QMessageBox.information (self, "TdPalio II", message)
                
            elif (codice == "Message Chat"):
                message = Qt.QString()
                stream >> message
                self.leggiChat(["Server:",  message])
            
            elif (codice == "Gioco Attivo"):
                stato = stream.readInt16()
                #print "Il server e` nel seguente stato: ", stato
                if (stato == 0): # NESSUN GIOCO ATTIVO
                    self.ui.actionNew.setEnabled(True)    
                    giochi = stream.readInt16()
                    for i in xrange(giochi):
                        nome = Qt.QString()
                        data = Qt.QString()
                        stream >> nome 
                        self.nome_giochi.append(str(nome))
                        stream >> data
                        self.data_giochi.append(str(data))
                elif (stato == 2):
                    stream >> nome
                    self.ui.actionOpen.setEnabled(True)    
                    Qt.QMessageBox.information (self, "TdPalio II", "Il gioco " + nome + " e` attivo")
                elif (stato == 1):
                    Qt.QMessageBox.information (self, "TdPalio II", "Un altro giocatore sta scegliendo il gioco")
                    
            elif (codice == "UserName"):
                self.sendMessage(["UserName",])
            
            elif (codice == "Lista Contrade"):
                nLista = stream.readInt16()
                lista = []
                for i in xrange(nLista):
                    l = Qt.QString()
                    stream >> l
                    lista.append(l)
                # FIXME SCELTA CASUALE DELLA CONTRADA
                item = Qt.QInputDialog.getItem(self, "Lista Contrade", "Contrada",  lista, 0, False)
                if (item[1] and not item[0].isEmpty()):
                    self.sendMessage(["Contrada Scelta",  item[0]])
                
            elif (codice == "Join Gioco"):
                nome = Qt.QString()
                stream >> nome
                accept = Qt.QMessageBox.question(self, "TdPalio II", "Il gioco " + nome + " e` attivo. Vuoi partecipare ?", Qt.QMessageBox.Yes|Qt.QMessageBox.No)
                if (accept == Qt.QMessageBox.Yes):
                    self.sendMessage(["Join Gioco Corrente",])
                else:
                    self.sendMessage(["Not Join Gioco Corrente",])

            elif (codice == "Estrazione"):
                lista = []
                for i in xrange(17):
                    s = Qt.QString()
                    stream >> s
                    lista.append(s)
                self.estrazione(lista)

            elif (codice == "SceltaFantino"):
                nFantini = stream.readInt16()
                fantini = list()
                for i in xrange(nFantini):
                    f = fantino.Fantino()
                    f.inStreamer(stream)
                    fantini.append(f)
                self.sceltaFantino(fantini)
            
            elif (codice == "RispostaFantinoSi"):
                offerte = stream.readInt16()
                off = []
                for i in xrange(offerte):
                    o = fantino.offerta()
                    o.inStream(stream)
                    off.append(o)
                self.decidiFantino(off)

            elif (codice == "AggiornaBarbero"):
                b = barbero.Barbero()
                b.inStreamer(stream)
                self.barbero = b

            elif (codice == "AggiornaContrada"):
                c = contrada.Contrada()
                c.inStreamer(stream)
                self.contrada = c

            elif (codice == "AggiornaFantino"):
                f = fantino.Fantino()
                f.inStreamer(stream)
                self.fantino = f

            elif (codice == "AggiornaCavallo"):
                c = cavallo.Cavallo()
                c.inStreamer(stream)
                self.cavallo = c
                self.aggiornaCavalloPanel()
	
            elif (codice == "StrategiaProva"):
                nProva = stream.readInt16()
                self.strategiaProva(nProva)

            elif (codice == "Partiti"):
                self.partiti()
      
            elif (codice == "RispostePartiti"):
                self.barbero.inStream(stream)
                self.decidiPartito()
      
            elif (codice == "NotificaPartiti"):
                # FIXME leggi partito e spurga la lista dei partiti richiesti
                self.notificaPartiti()
	
    def serverHasStopped(self):
        self.tcpSocket.close()
        sys.exit(0)
						
    def serverHasError(self, error):
        print Qt.QString("Error: %1").arg(self.tcpSocket.errorString())
        self.tcpSocket.close()
        sys.exit(0)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    client = tdpyClient()
    #splash.splash.splash(client)
    client.openConnection()
    client.show()
    sys.exit(app.exec_())

    
    
