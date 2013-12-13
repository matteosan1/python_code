#! /usr/bin/python

import sys, time, random, os
from PyQt4.QtNetwork import *
from PyQt4.QtCore import *
from tdpyaiclient import aiclient
from tdpsocket import *
import contrada, fantino, cavallo, barbero, giocatore
import fase
    
class TDPalioServer(QTcpServer):
  
    def __init__(self, parent=None):
        super(TDPalioServer, self).__init__(parent)
        self.sockets = []
        self.contrade = []
        self.fantini = []
        self.cavalli = []
        self.barberi = []
        self.giocatori = []
        self.avviamentoGioco = -1
        self.giocoAttivo = False
        self.fileName = QString("")
        self.fase = fase.Fase()
        self.connect(self.fase, SIGNAL("nuovaFase"), self.nuovaFase)

        self.ai = []
        # avvia 17 client ai
        for i in xrange(17):
            time.sleep(.3)
            self.ai.append(aiclient.TDPalioAiClient())

        # carica le condizioni iniziali
        self.inizializza()

    def removePlayer(self, e):
        for i, s in enumerate(self.sockets):
            if (s.error() > -1):
                self.salvaFile()
                print QString("Error from socket %1").arg(i)
                sys.exit(0)

    def inizializza(self):  
        # FIXME condizioni iniziali casuali ????
        file = open("data/setup.dat", "r")
        for i in xrange(17):
            c = contrada.Contrada()
            c.caricaDati(file)
            self.contrade.append(c)
      
        for i in xrange(16):
            f = fantino.Fantino()
            f.caricaDati(file)
            self.fantini.append(f)

        for i in xrange(21):
            c = cavallo.Cavallo()
            c.caricaDati(file)
            self.cavalli.append(c)
    
        self.fase.estrazione(-1)

    def salvaFile(self):
        file = QFile("giochi/" + self.fileName + ".tdp")
        if (not file.open(QIODevice.WriteOnly)):
            print "NON POSSO SALVARE IL GIOCO..."
            sys.exit(1001)
 
        out = QTextStream(file)
        out << self.fase.anno << " "
        out << self.fase.mese << " "
        out << self.fase.fase << " "
        out << self.fase.nprova << "\n"
  
        #for(int i=0; i<17; i++)
        #  out << corrono[i] << " ";
        #out << "\n";

        for i in xrange(17):
            out << self.fase.luglio[i] << " "
        out << "\n"
  
        for i in xrange(17):
            out << self.fase.agosto[i] << " "
        out << "\n"
  
        for i in xrange(17):
            out << self.fase.straordinario[i] << " "
        out << "\n"
 
        out << len(self.giocatori) << "\n"
        for i in xrange(len(self.giocatori)):
            self.giocatori[i].outTextStreamer(out)

        for i in xrange(17):
            self.contrade[i].outTextStreamer(out)
  
        for i in xrange(21):
            self.cavalli[i].outTextStreamer(out)
  
        out << len(self.fantini) << "\n"
        for i in xrange(len(self.fantini)):
            self.fantini[i].outTextStreamer(out)

        out << len(self.barberi) << "\n"
        for i in xrange(len(self.barberi)):
            self.barberi[i].outTextStreamer(out)
        
        file.close();

    def caricaFile(self):
        self.cavalli = []
        self.fantini = []
        path = "giochi/" + self.fileName + ".tdp"
        file = QFile(path)
        if (not file.open(QIODevice.ReadOnly)):
            print "NON POSSO CARICARE QUESTO GIOCO (Error Code " + file.error()+")"
            # FIXME manda un popup a chi ha cercato di caricare il gioco
            # QString mex("NON POSSO CARICARE QUESTO GIOCO...");
            #      myStreamerOut->stringStream[0] = mex;
            #      for(int i=0; i<sockets.size(); ++i) {
            #        sendMessage(PopupMessage, sockets[i]);
            #        return false;
            sys.exit(8003)
        inf = QTextStream(file)
        t = QString()
        inf >> t
        self.fase.anno = int(t)
        inf >> t
        self.fase.mese = int(t)
        inf >> t
        self.fase.fase = int(t)
        inf >> t
        self.fase.nprova  = int(t)

        #for i in xrange(17):
        #    inf >> self.corrono[i] # ???????

        for  i in xrange(17):
            inf >> t
            self.fase.luglio[i] = int(t)
    
        for  i in xrange(17):
            inf >> t
            self.fase.agosto[i] = int(t)
  
        for  i in xrange(17):
            inf >> t
            self.fase.straordinario[i] = int(t)
        
        inf >> t
        nGiocatori = int(t)
        for i in xrange(nGiocatori):
            g = giocatore.Giocatore()
            g.inTextStreamer(inf)
            self.giocatori.append(g)
  
        for i in xrange(17):
            c = contrada.Contrada()
            c.inTextStreamer(inf)
            self.contrade[i] = c
            
        for i in xrange(21):
            c = cavallo.Cavallo()
            c.inTextStreamer(inf)
            self.cavalli.append(c)

        inf >> t
        nFantini = int(t)   
        for i in xrange(nFantini):
            f = fantino.Fantino()
            f.inTextStreamer(inf)
            self.fantini.append(f)
 
        inf >> t
        nBarberi = int(t)        
        for  i in xrange(nBarberi):
            b = barbero.Barbero()
            b.inTextStreamer(inf)
            self.barberi.append(b)

        file.close()
        return 1

    def nSocketContrada(self, index):
        for j, s in enumerate(self.sockets):
            if (s.tipo == index):
                return j
        else:
            print "Errore, nessun socket ha la contrada: ", index            

    def socketContrada(self, index):
        for s in self.sockets:
            if (s.tipo == index):
                return s
        else:
            print "Errore, nessun socket ha la contrada: ", index
        
    def azzeraSockets(self):
        for i in self.fase.chi_corre():
            self.socketContrada(i).stato = "Not Ready"
        for i in self.fase.chi_non_corre():
            self.socketContrada(i).stato = "Spectator"

    def controllaNSocketsPerStato(self, n, stato):
        tot = 0
        for i in self.sockets:
            if (i.tipo >= 0 and i.stato == stato):
                tot += 1
        if (tot == n):
            return True
        else:
            return False

    def controllaSocketsPerStato(self, stato):
        tot = 0
        for i in self.sockets:
            if (i.tipo >= 0 and i.stato == stato):
                tot += 1
        if (tot != 0):
            return False
        else:
            return True

    def controllaNSocketsUmaniPerStato(self, n, stato):
        tot = 0
        for i in self.sockets:
            if (i.userName != "AI" and i.stato == stato):
                tot += 1
        if (tot == n):
            return True
        else:
            return False

    def controllaNSocketsUmani(self, n):
        tot = 0
        for i in self.sockets:
            if (i.userName != "AI"):
                tot += 1
        if (tot >= n):
            return True
        else:
            return False
    
    def contradeDisponibili(self, n_socket):
        lista = [] 
        userContradaMap = [[k.username, k.contrada] for k in self.giocatori]
        # controlla se il giocatore giocava gia`
        for i,j in enumerate(userContradaMap):
            if (self.sockets[n_socket].userName == j[0]):
                self.sceltaContrada(n_socket, j[1],  -i)
                return

        lista_contrade_che_giocavano = [k[1] for k in userContradaMap]
        # fa la lista delle contrade rimaste 
        for j,i in enumerate(self.contrade):
            if (self.socketContrada(j).userName == "AI" and j not in lista_contrade_che_giocavano):
                lista.append(i.nomeCompleto)
        
        # se la lista e` vuota prende anche quelle del vecchio gioco non ancora riprese
        if (len(lista) == 0):
            for j,i in enumerate(self.contrade):
                if (self.socketContrada(j).userName == "AI"):
                    lista.append(i.nomeCompleto)

        self.sendMessage(n_socket, ["Lista Contrade", lista])
              
    def sceltaContrada(self, n_socket, n_contrada,  tipo):
        if (tipo <= 0):
            if (self.socketContrada(n_contrada).userName == "AI"):
                self.socketContrada(n_contrada).tipo = -1 #???????
                self.sockets[n_socket].tipo = n_contrada
                self.giocatori[-tipo].sta_giocando = True
                self.sendMessage(n_socket, ["Conferma Contrada", n_contrada, -tipo])
                self.sendMessage(n_socket, ["Message Box", QString("Sei stato riassegnato alla " + self.contrade[n_contrada].nomeCompleto)])
                # FIXME da controllare in varie situazioni
                if (self.controllaNSocketsUmaniPerStato(0, "Not Ready")): # and self.fase.fase == 0):
                    self.fase.nuovaFase()
            else:
                self.contradeDisponibili(n_socket)
        else:
            if (self.socketContrada(n_contrada).userName == "AI"):
                self.socketContrada(n_contrada).tipo = -1
                self.sockets[n_socket].tipo = n_contrada
                g = giocatore.Giocatore()
                g.nome = ""                           
                g.cognome = ""                                                   
                g.username = self.sockets[n_socket].userName
                g.contrada = n_contrada                                                       
                g.score = [0,0]                              
                g.sta_giocando = True
                self.giocatori.append(g)
                self.sendMessage(n_socket, ["Conferma Contrada", n_contrada, len(self.giocatori)-1])
                self.sendMessage(n_socket, ["Message Box", QString("Sei stato assegnato alla " + self.contrade[n_contrada].nomeCompleto)])

                if (self.controllaNSocketsUmaniPerStato(0, "Not Ready") and self.fase.fase == 0):
                    self.fase.nuovaFase()
            else:
                self.contradeDisponibili(n_socket)
            
    def incomingConnection(self, socketId):
        s = Socket()
        self.connect(s, SIGNAL("readyRead()"), self.readMessage)
        self.connect(s, SIGNAL("error(QAbstractSocket::SocketError)"), self.removePlayer)

        s.setSocketDescriptor(socketId)
        if (len(self.sockets) < 17):
            s.tipo = len(self.sockets)

        self.sockets.append(s)
        if (len(self.sockets) > 17):
            #if (self.controllaSocketsUmani(17)):
            #    self.sendMessage(len(self.sockets)-1, ["Messaggio", "Ci sono gia` 17 giocatori, riprova piu` tardi."])
            #    s.disconnectFromHost()
            #    return
            #s.tipo = 1
            self.sendMessage(len(self.sockets)-1, ["UserName",])
    
    def readMessage(self):
        for j, i in enumerate(self.sockets):
            if (i.bytesAvailable() > 0):
                stream = QDataStream(i)
                stream.setVersion(QDataStream.Qt_4_5)
                self.processMessage(j, stream)

    def processMessage(self, number, stream):
        codice = QString()
        stream >> codice
        print "SERVER: ", codice, number
        if (codice == "Ready"):
            self.sockets[number].stato = "Ready"
            if (self.controllaNSocketsUmani(1) and self.controllaNSocketsUmaniPerStato(0, "Not Ready")):
                self.fase.nuovaFase()
            if (self.controllaNSocketsPerStato(17, "Ready") and self.controllaNSocketsUmani(1)):
                self.fase.nuovaFase()
            #if (self.controllaNSocketsPerStato(10, "Ready") and self.controllaNSocketsPerStato(7, "Spectator")):
            #    self.fase.nuovaFase()
    
        elif (codice == "UserName"):
            nome = QString()
            stream >> nome
            print "Si e` registrato il giocatore: ", nome
            self.sockets[number].userName = str(nome)
            self.sendMessage(number, ["Gioco Attivo", self.giocoAttivo])

        #elif (codice == "Nuovo Gioco"):
         #   n_parametri = stream.readInt16()
         #   parametri = []
         #   for i in xrange(n_parametri):
         #       stream >> p
          #      parametri.append(p)      
          #  if (self.avviamentoGioco):
          #      self.sendMessage(number, ["Messaggio", "Un gioco e` gia` stato scelto"])
          #  else:
          #      self.avviamentoGioco = True
          #      self.giocoAttivo = True
          #      self.nomeFile = parametri[1]
           #     self.fase.anno = parametri[2]
          #  for i in xrange(17, len(self.sockets)):
          #      self.contradeDisponibili(i)
      
    #elif (codice == "Vecchio Gioco"):
     # if (self.avviamentoGioco):
      #  self.sendMessage(number, ["Messaggio", "Un gioco e` gia` stato scelto"])
     # else:
     #   self.avviamentoGioco = True
      #  self.sendMessage(number, ["Avvia Gioco",])
    
        elif (codice == "Gioco Scelto"):
            if (self.avviamentoGioco != -1 and self.avviamentoGioco != number):
                return
            self.avviamentoGioco = number
            self.giocoAttivo = True
            stream >> self.fileName 
            if (self.fileName == "----"):
                self.giocoAttivo = False
                self.avviamentoGioco = -1
                print "Nessun gioco scelto"
                return
            if (os.path.isfile("giochi/"+ self.fileName+".tdp")):
                result = self.caricaFile()
                if (not result):
                    for k,i in enumerate(self.sockets):
                        if (i.userName != "AI"):
                            self.sendMessage(k, ["Message Box", "Problema irreversibile: non posso caricare il gioco."])
                            sys.exit(1002)
                for i in xrange(len(self.sockets)):
                    if (i == self.avviamentoGioco):
                       self.sockets[number].stato = "Ready"
                       self.contradeDisponibili(number)
                    else:
                        self.sendMessage(i, ["Join Gioco",])
            else:
                self.salvaFile() 
                for i in xrange(len(self.sockets)):
                    if (i == self.avviamentoGioco):
                        self.sockets[number].stato = "Ready"
                        self.contradeDisponibili(number)
                    else:
                        self.sendMessage(i, ["Join Gioco",])
    
        elif (codice == "Join Gioco Corrente"):
            self.sockets[number].stato = "Ready"
            self.contradeDisponibili(number)
    
        elif (codice == "Not Join Gioco Corrente"):
            self.sockets[number].stato = "Spectator"

        elif (codice == "Contrada Scelta"):
            c = QString()
            stream >> c
            lista = [i.nomeCompleto for i in self.contrade]
            index = lista.index(c)
            self.sceltaContrada(number, index, 1)
    
        elif (codice == "SceltaCavalli"):
            self.sockets[number].stato = "Ready"
            nScelti =  stream.readInt16()
            scelta = []
            for i in xrange(nScelti):
                scelta.append(stream.readInt16())
            self.sceltaCavalliRead(scelta)
        
        elif (codice == "SceltaFantino"):
            offerte = []
            nOfferte = stream.readInt16()
            for i in xrange(nOfferte):
                o = fantino.Offerta()
                o.inStreamer(stream)
                offerte.append(o)
            self.sceltaFantinoRead(number, offerte)

        elif (codice == "RispostaFantinoSi"):
            offerte = []
                
        elif (codice == "FantinoDeciso"):
            f = stream.readInt16()
            self.decisioneFantino(number, f)

        elif (codice == "Partiti"):
            nPartiti = stream.readInt16()
            listaPartiti = []
            for i in xrange(nPartiti):
                p = barbero.Partito()
                p.inStreamer(stream)
                listaPartiti.append(p)
            self.sockets[number].stato = "Ready"
            self.raccogliPartiti(listaPartiti)
  
        elif (codice == "DecisionePartiti"):
            self.sockets[number].stato = "Ready"
            b = barbero.Barbero()
            b.inStreamer(stream)
            self.barberi[b.indice] = b
            if (self.controllaSockets(10, "Ready")):
                self.notificaPartiti()

        elif (codice == "StrategiaProva"):
            b = barbero.Barbero()
            b.inStreamer(stream)
            self.barberi[b.indice] = b
            self.sockets[number].stato = "Ready"
            if (self.controllaSockets(10, "Ready")):
                self.fase.nuovaFase()
      
        elif (codice == "RispostaSegnatura"):
            self.sockets[number].stato = "Ready"
            f = fantino.Fantino()
            f.inStreamer(stream)
            self.fantini[f.indice] = f
            # FIXME comunica a tutti il nuovo nome...
            if (self.controllaSockets(10, "Ready")):
                self.fase.nuovaFase()
                
    def sendMessage(self, socket_n, message):
        reply = QByteArray()
        stream = QDataStream(reply, QIODevice.WriteOnly)
        stream.setVersion(QDataStream.Qt_4_5)
        stream << QString(message[0])

        if (message[0] == "Segnatura"):
            message[1].outStreamer(stream)
            stream.writeInt16(int(message[2]))

        if (message[0] == "SceltaCavalli"):
            for i in self.cavalli:
                i.outStreamer(stream)
        
        elif (message[0] == "Assegnazione"):
            for i in message[1]:
                stream.writeInt16(i[0])
                stream.writeInt16(i[1])
                stream.writeInt16(i[2])
                stream.writeInt16(i[3])
            for b in message[2]:
                stream << QString(self.contrade[b.contrada].nome)

            for b in message[2]:
                stream << QString(self.cavalli[b.cavallo].nome)

        elif (message[0] == "Estrazione"):
            for i in self.fase.chi_corre():
                stream << QString(self.contrade[i].nome)
            for i in self.fase.chi_non_corre():
                stream << QString(self.contrade[i].nome)
    
        elif (message[0] == "Conferma Contrada"):
            self.contrade[message[1]].outStreamer(stream)
            self.giocatori[message[2]].outStreamer(stream)
        
        elif (message[0] == "UserName"):
            pass
        
        elif (message[0] == "Message Box"):
            stream << QString(message[1])

        elif (message[0] == "Join Gioco"):
            stream << QString(self.fileName)

        elif (message[0] == "Gioco Attivo"):
            if (self.avviamentoGioco == -1):
                self.avviamentoGioco = socket_n
            else:
                stream.writeInt16(1)
            
            if (not self.giocoAttivo):
                stream.writeInt16(0)
                giochi = os.popen("ls -l giochi/*.tdp").readlines()
                stream.writeInt16(len(giochi))
                for i in giochi:
                    stream << QString(i.split(" ")[7].split(".tdp")[0].split("giochi/")[1])
                    stream << QString(i.split(" ")[5]+" "+i.split(" ")[6])
            else:
                stream.writeInt16(2)
                stream << self.fileName
            
        elif (message[0] == "Lista Contrade"):
            stream.writeInt16(len(message[1]))
            for i in message[1]:
                stream << QString(i)

        elif (message[0] == "SceltaFantino"):
            stream.writeInt16(len(self.fantini))
            for i in self.fantini:
                i.outStreamer(stream)
        
        elif (message[0] == "AggiornaTutto"):
            for i in xrange(10):
                stream << QString(message[1][i])
            for i in xrange(10):
                stream << QString(message[2][i])
            for i in xrange(10):
                stream << QString(message[3][i])

        elif (message[0] == "AggiornaBarbero"):
            self.barberi[message[1]].outStreamer(stream)
    
        elif (message[0] == "AggiornaContrada"):
            self.contrade[message[1]].outStreamer(stream)

        elif (message[0] == "AggiornaFantino"):
            self.fantini[message[1]].outStreamer(stream)

        elif (message[0] == "AggiornaCavallo"):
            self.cavalli[message[1]].outStreamer(stream)
    
        elif (message[0] == "RispostaFantinoSi"):
            stream.writeInt16(len(message[1]))
            for i in message[1]:
                i.outStreamer(stream)

        elif (message[0] == "Partiti"): 
            for b in self.barberi:
                b.outStreamer(stream)
        
        elif (message[0] == "RispostePartiti"):
            self.barberi[message[1]].outStreamer(stream)
        
        elif (message[0] == "StrategiaProva"):
            stream.writeInt16(self.fase.nProva)

        self.sockets[socket_n].write(reply)
        return
    
    def nuovaFase(self, fase):
        print "FASE ",fase
        #for s in self.sockets:
        #    self.sendMessage(s, ["AggiornaTutto", ])
        if (fase == "Estrazione"):
            self.fase.estrazione(1)
            for j,i in enumerate(self.sockets):
                if (i.userName != "AI"):
                    i.stato = "Not Ready"
                    self.sendMessage(j, ["Estrazione",])

            for j,i in enumerate(self.fase.chi_corre()):
                b = barbero.Barbero()
                b.indice = j;
                b.contrada = i
                if (self.contrade[j].status[0] in self.fase.chi_corre()):
                    b.avversaria = self.fase.chi_corre().index(self.contrade[j].status[0])
                self.barberi.append(b)
            for j, i in enumerate(self.fase.chi_corre()):
                self.sendMessage(self.nSocketContrada(i), ["AggiornaBarbero", j])
                self.sendMessage(self.nSocketContrada(i), ["AggiornaContrada", i])
	
            # forma e coscia dei cavalli alla tratta
            self.provincia()	
      
        elif (fase == "SceltaCavalli"):
            self.azzeraSockets()
            for i in self.fase.chi_corre():
                self.sendMessage(self.nSocketContrada(i), ["SceltaCavalli",])
      
        elif (fase == "SceltaFantino"):
            self.azzeraSockets()
            for i in self.fase.chi_corre():
                self.sendMessage(self.nSocketContrada(i), ["SceltaFantino",])
            #for i in self.barberi:
            #    if (i.fantino == -1):
            #        self.sendMessage(i.contrada, ["SceltaFantino",])
            #    else:
            #        self.sockets[i.contrada].stato = "Ready"
        elif (fase == "Partiti"):
            self.azzeraSockets()
            for i in self.barberi:
                self.sendMessage(i.contrada, ["Partiti",])
	
        elif (fase == "StrategiaProva"):
            self.azzeraSockets()
            for i in self.barberi:
                self.sendMessage(i.contrada, ["StrategiaProva",])
	
        elif (fase == "CorsaProva"):
            self.corsaProva()
    
        elif (fase == "AggiornaFantino"):
            self.aggiornaFantino()
        
        elif (fase == "Segnatura"):
            self.segnatura()

        elif (fase == "Mossa"):
            self.mossa()
            
        elif (fase == "PartitiMossa"):
            self.partitiMossa()
            
        elif (fase == "Palio"):
            self.palio()
        
        elif (fase == "PostPalio"):
            self.postPalio()
    
    def provincia(self):
        # FIXME
        # assegna forma e numero di coscia a tutti i cavalli
        c = random.sample(xrange(1,22), 21)
        for n, i in enumerate(self.cavalli):
            i.coscia = c[n]
            forma = int(random.gauss(60, 20))
            if (forma > 100):
                forma = 100
            elif(forma < 20):
                forma = 20
            i.forma = forma
     
    def sceltaCavalliRead(self, scelta):
        # FIXME azzera il conteggio per i cavalli da qualche parte
        for i in scelta:
            self.cavalli[i].selezione += 1
        
        if (self.controllaNSocketsPerStato(10, "Ready")):
            self.azzeraSockets()
            # FIXME aggiungere peso maggiore se pochi giocatori
            c = self.cavalli
            for i in xrange(len(c)):
                for j in xrange(len(c)):
                    if (c[i].indice == c[j].indice):
                        continue
                    if ((c[i].selezione < c[j].selezione) or ((c[i].selezione == c[j].selezione) and (c[i].coscia < c[j].coscia))):
                        temp = c[i]
                        c[i] = c[j]
                        c[j] = temp

            cavalli_scelti = []
            for i in c[0:10]:
                cavalli_scelti.append(i.indice) 
            self.assegnazione(cavalli_scelti)
    
    def assegnazione(self, cavalli_scelti):
        # ordina i cavalli scelti per numero di coscia
        coscia = [self.cavalli[i].coscia for i in cavalli_scelti]
        cosciaECavalli = zip(coscia, cavalli_scelti)
        cosciaECavalli.sort()

        # fai l'assegnazione
        ass_temp = self.fase.assegnazione()
        ass = []
        for i in ass_temp:
            ass.append([i[0], cosciaECavalli[i[0]][0], cosciaECavalli[i[0]][1], i[1]])
        
        for i in ass:
            self.barberi[i[3]].cavallo = i[2]
            self.barberi[i[3]].strategia = self.strategia(i[3], True)

        for j,i in enumerate(self.sockets):
            if (i.userName != "AI"):
                i.stato = "Not Ready"
                self.sendMessage(j, ["Assegnazione", ass, self.barberi])

        for j, i in enumerate(self.fase.chi_corre()):
            self.sendMessage(i, ["AggiornaBarbero", j])
            self.sendMessage(i, ["AggiornaCavallo", self.barberi[j].cavallo])
      
    def sceltaFantinoRead(self, socket_number, offerte):
        self.sockets[socket_number].stato = "Ready"
        for i in offerte:
            self.fantini[i.fantino].offerte.append(i)
    
        if (self.controllaNSocketsPerStato(10, "Ready")):
            print "SOMMARIO OFFERTE"
            for i in self.fantini:
                for j in i.offerte:
                    print j
            self.rispostaFantino()
	  
    def rispostaFantino(self):
        mappaOfferte = []
        for f in self.fantini:
            # skippa se e` gia` impegnato o se non ha offerte
            if (f.contrada != -1):
                continue

            if (len(f.offerte) == 0):
                continue
      
            best_rate = -1
            best_offerta = -1
            for i, o in enumerate(f.offerte):
                # assegna un rate alle offerte 
                if (strategia == 0):
                    rate = 5
                    for i,b in enumerate(self.barberi):
                        if (i == richiedente):
                            rate += 1
                        elif (i == avversaria):
                            rate += 0
                        else:
                            if (b.strategia == 0):
                                rate += 0
                            elif (b.strategia == 1):
                                rate += self.contrade[b.contrada].feeling(self.barberi[richiedente].contrada)/2.
                            elif (b.strategia == 2):
                                rate += self.contrade[b.contrada].feeling(self.barberi[richiedente].contrada)*2.          
                            elif (b.strategia == 3):
                                rate += self.contrade[b.contrada].feeling(self.barberi[richiedente].contrada)
                    # FIXME valori negati e protezione per offerte umane esagerate
                    prezzo_base = f.prezzo()+100.
                    rate += float(prezzo-prezzo_base)/float(prezzo_base)

                elif (strategia == 1):
                    pass
                elif (strategia == 2):
                    pass
                else:
                    pass
                
                if (rate > best_rate):
                    best_offerta = i
                    best_rate = rate

            # FIXME aggiungi dubbio se le prime due offerte sono vicine
            mappaOfferte.append(f.offerte[best_offerta])
        
        # comunica le decisioni
        for b in self.barberi:
            risposte = []
            for i in mappaOfferte:
                for o in enumerate(i[2]):
                    if (b.indice == o.richiedente):
                        risposte.append(o)
            
            self.sendMessage(b.contrada, ["RispostaFantinoSi", risposte])
              
    def decisioneFantino(self, c, f):
        self.sockets[c].stato = "Ready"
        if (f != -1):
            #print self.fase.chi_corre()
            for i in self.fantini:
                to_remove = []
                if (i.indice == f):
                    for j, k in enumerate(i.offerte):
                        if (self.barberi[k.chi].contrada != c):
                            to_remove.append(j)
                else:
                    for j, k in enumerate(i.offerte):
                        if (self.barberi[k.chi].contrada == c):
                            to_remove.append(j)
        
            if (len(to_remove) != 0):
                to_remove.sort(reverse=True)
                for j in to_remove:
                    i.offerte.pop(j)

            for b in self.barberi:
                if (b.contrada == c):
                    self.fantini[f].contrada = c
                    b.fantino = f
                    self.contrade[c].status[2] -= self.fantini[f].prezzo()
                    self.sendMessage(c, ["AggiornaBarbero", b.indice])
                    self.sendMessage(c, ["AggiornaContrada", c])
                    self.sendMessage(c, ["AggiornaFantino", f])
                    break

        if (self.controllaNSocketsPerStato(10, "Ready")):
            for b in self.barberi:
	        #print i.fantino, i.indice
                if (b.fantino == -1):
                    f = fantino.Fantino()
                    self.fantini.append(f)
                    self.sendMessage(b.contrada, ["Message Box", "Per il momento hai coraggiosamente deciso di affidarti al giovane " + f.nomeVero + "."])
                    b.fantino = len(self.fantini) - 1
                    self.fantini[f].contrada = b.contrada
                    self.contrade[c].status[2] -= 10
                    self.sendMessage(b.contrada, ["AggiornaBarbero", b.indice])
                    self.sendMessage(b.contrada, ["AggiornaContrada", c])
                    self.sendMessage(b.contrada, ["AggiornaFantino", f])

            for s in self.sockets:
                if (s.userName != "AI"):
                    t0 = [self.contrade[i].nome for i in b.contrada]
                    t1 = [self.cavalli[i].nome for i in b.cavallo]
                    t2 = []
                    for i in b.fantini:
                        if (self.fantini[i].nome != "-") :
                            t2.append(self.fantini[i].nome)
                        else:
                            t2.append(self.fantini[i].nomeVero)
                    self.sendMessage(s, ["AggiornaTutto", t0, t1, t2])
            #self.saveFile()
            self.fase.nuovaFase()

    def raccogliPartiti(self, listaPartiti):
        for p in listaPartiti:
            self.barberi[p.esegue].partiti_da_fare.append(p)
      
        if (controllaSockets(10, "Ready")):
            for b in self.barberi:
                self.sendMessage(b.contrada, ["RispostePartiti", b.indice])

    def notificaPartiti(self):
        listaPartiti = []
        for b in self.barberi:
            for p in b.partiti_da_fare:
                listaPartiti.append([p.richiede, p])
    
        listaPartiti.sort()
        for p in listaPartiti:
            self.sendMessage(self.barberi[p[0]].contrada, ["NotificaPartiti", p[1]])
        self.fase.nuovaFase()

    def corsaProva(self):
        result = Qt.QString()
        nProva = self.fase.nProva
        print "PROVA: ", nProva
        mossa = self.fase.prove[nProva]
        
        mossaDifficile = False
        # FIXME me codice strategia
        if (self.barberi[mossa[9]].strategiaProve[nProva] == 10):
            mossaDifficile = True
            for b in self.barberi:
                if (b.indice == self.barberi[mossa[9]].indice):
                    continue
                if (b.cavallo.score[2] < 3):

                    b.cavallo.capacita[0] -= 0.3
        if (mossaDifficile): 
            result += "Mossa: difficile con la " + self.barberi[mossa[9]].contrada.nome + " che temporeggia per innervosire i cavalli dentro al canape.\n"
        else:
            result += "Mossa: veloce senza particolari problemi.\n"
        # FIXME aggiungere testo tensione al canape...
        for i in xrange(9):
            if (self.barberi[mossa[i]].strategiaProve[nProva] == 10):
                # FIXME codice strategia
                self.barberi[mossa[i]].strategiaProve[nProva] -= 10
                self.barberi[mossa[i]].cavallo.forma -= 5
                riesce = ramdom.random.uniform(0, 1)
                if ((i == 0) and (self.barberi[mossa[i]].avversaria == self.barberi[mossa[i+1]].contrada)):
                    if (riesce > .5):
                        self.barberi[mossa[i]].cavallo.forma -= 10
                        if (b.cavallo.score[2] < 3):
                            b.cavallo.capacita[0] -= 0.3

                elif ((i == 8) and (self.barberi[mossa[i]].avversaria == self.barberi[mossa[i-1]].contrada)):
                    if (riesce > .5):
                        self.barberi[mossa[i]].cavallo.forma -= 10
                        if (b.cavallo.score[2] < 3):
                            b.cavallo.capacita[0] -= 0.3

                elif ((i < 8 and i > 0) and ((self.barberi[mossa[i]].avversaria == self.barberi[mossa[i-1]].contrada))):
                    if (riesce > .5):
                        self.barberi[mossa[i]].cavallo.forma -= 10
                        if (b.cavallo.score[2] < 3):
                            b.cavallo.capacita[0] -= 0.3

                elif ((i < 8 and i > 0) and ((self.barberi[mossa[i]].avversaria == self.barberi[mossa[i+1]].contrada))):
                    if (riesce > .5):
                        self.barberi[mossa[i]].cavallo.forma -= 10
                        if (b.cavallo.score[2] < 3):
                            b.cavallo.capacita[0] -= 0.3
        

        # controlla ostacoli fra rivali
        for i in xrange(9):
            

        for m in mossa:
            b = self.barberi[m]
            # prova partenza se non ostacolato
            if (b.strategiaProve[nProva] == 1):
            # prova curva
            elif (b.strategiaProve[nProva] == 1):
            # se mossa faticosa cambia "paura" del cavallo
            elif (b.strategiaProve[nProva] == 1):
            elif (b.strategiaProve[nProva] == 1):
            elif (b.strategiaProve[nProva] == 1):
        
        # looppa su tutti i barberi e prova la strategia
        # aggiorna i parametri da aggiornare
        # manda un report sulla prova ad ogni contrada
        # esci e aspetta un ready da tutti
  
    def strategia(self, indice, avversaria):
        # FIXME aggiungere umore della contrada
        avversaria = self.barberi[indice].avversaria
        contrada = self.barberi[indice].contrada
        cuffia = self.contrade[contrada].vittorie[3]
        soldi = self.contrade[contrada].status[2]
        media = self.cavalli[self.barberi[indice].cavallo].media()
        
        strategia = -1

        if (media >= 6):
            if((cuffia <= 5) and (cuffia >= 0)):
                strategia = 1
            elif ((cuffia <= 10) and (cuffia > 5)):
                strategia = 0
            elif ((cuffia <= 15) and (cuffia > 10)):
                strategia = 0
            elif (cuffia > 15):
                strategia = 0
        elif (media <=4):
            if((cuffia <= 5) and (cuffia >= 0)):
                strategia = 1
            elif ((cuffia <= 10) and (cuffia > 5)):
                strategia = 1
            elif ((cuffia <= 15) and (cuffia > 10)):
                strategia = 0
            elif (cuffia > 15):
                strategia = 0
        else:
            if((cuffia <= 5) and (cuffia >= 0)):
                strategia = 2
            elif ((cuffia <= 10) and (cuffia > 5)):
                strategia = 2
            elif ((cuffia <= 15) and (cuffia > 10)):
                strategia = 1
            elif (cuffia > 15):
                strategia = 1

        # FIXME soglia dei soldi da valutare
        if (soldi < 200 and strategia < 2):
            strategia += 1

        # cambio strategia per avversaria forte
        if (avversaria != -1):
            if ((self.barberi[avversaria].strategia == 0) and (strategia != 0)):
                strategia = 3

        return strategia
        
    def aggiornaFantino(self):
    # FIXME manda un messaggio a tutti i giocatori che possono provare
    # a scambiare un fantino di una contrada diversa o prenderne uno disponibile
        pass
    
    def segnatura(self):
        eFatta = True
        for b in self.barberi:
            if (b.fantino.nome == ""):
                eFatta = False
                if (socketContrada(b.contrada).userName != "AI"):
                    socketContrada(b.contrada).stato = "Not Ready"
                    # FIXME secondo me non torna l'indice della contrada
                    self.sendMessage(self.barberi[p[0]].contrada, ["Segnatura", b.fantino, True])                    
                else:
                    temp = []
                    for i, s in enumerate(self.sockets):
                        if (s.userName != "AI"):
                            temp.append(i)
                    indice = random.sample(1, temp)
                    socketContrada(indice).stato = "Not Ready"
                    self.sendMessage(indice, ["Segnatura", b.fantino, False])
                    
        if (eFatta):
            self.fase.nuovaFase()
    
#FIXME DA FARE:
# partiti alla mossa: posto tra i vicini e farsi dare la mossa

# corsa

# aggiornare parametri nel dopo-corsa: vittorie, partiti, cavalli, fantini, infortuni...
# numero unico, commenti giocatori
# salvare tutto in un db sqllite

# ricomiciare da capo


if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    port = 1974
    if (len(sys.argv) > 1):
        port = int(sys.argv[1])

    server = TDPalioServer()
    if (not server.listen(QHostAddress("127.0.0.1"), port) or not server.isListening()):
        print QString("Failed to start server: %1").arg(server.errorString())
    
    sys.exit(app.exec_())
