# -*- coding: utf-8 -*-
import sys
import random
from PyQt4.QtNetwork import *
from PyQt4.QtCore import *
import cavallo, fantino, barbero, contrada
import tdpsocket

class TDPalioAiClient(QObject):
	      
  def __init__(self, parent=None):
    super(TDPalioAiClient, self).__init__(parent)
    self.socket = QTcpSocket()
    self.socket.connectToHost("localhost", 1974)
    self.barbero = barbero.Barbero()
    self.contrada = contrada.Contrada()
    self.fantino = fantino.Fantino()
    self.cavallo = cavallo.Cavallo()
    
    self.connect(self.socket, SIGNAL("connected()"), self.ready)
    self.connect(self.socket, SIGNAL("readyRead()"), self.readMessage)
    self.connect(self.socket, SIGNAL("disconnected()"), self.serverHasStopped)
    self.connect(self.socket, SIGNAL("error(QAbstractSocket::SocketError)"), self.serverHasError)
    self.connect(self.socket, SIGNAL("stateChanged (QAbstractSocket::SocketState)"), self.statoSocket)
    
  def statoSocket(self, stato):
    #print "STATO: ", stato
    stato = 0
    
  def ready(self):
    self.sendMessage(["Ready",""])
    
  def sendMessage(self, message):
    request = QByteArray()
    stream = QDataStream(request, QIODevice.WriteOnly)
    stream.setVersion(QDataStream.Qt_4_2)
    stream << QString(message[0])
    if (message[0] == "SceltaCavalli"):
      stream.writeInt16(len(message[1]))
      for i in message[1]:
	stream.writeInt16(i)
	
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
	
    self.socket.write(request)
    
    
  def readMessage(self):
    while (self.socket.bytesAvailable() > 0):
      stream = QDataStream(self.socket)
      stream.setVersion(QDataStream.Qt_4_2)
      codice = QString()
      stream >> codice

      if (codice == "SceltaCavalli"):
          cavalli = list()
          for i in xrange(20):
              c = cavallo.Cavallo()
              c.inStreamer(stream)
              cavalli.append(c)
          self.sceltaCavalli(cavalli)
      
      elif (codice == "SceltaFantino"):
          nFantini = stream.readInt16()
          fantini = list()
          for i in xrange(nFantini):
              f = fantino.Fantino()
              f.inStreamer(stream)
              fantini.append(f)
          self.sceltaFantino(fantini)

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
	
      elif (codice == "RispostaFantinoSi"):
          offerte = stream.readInt16()
          off = []
          if (offerte == 0):
              pass
          else:
              for i in xrange(limite):
                  o = fantino.offerta()
                  o.inStream(stream)
                  off.append(o)
          self.decidiFantino(off)

      elif (codice == "Partiti"):
          barberi = []
          for i in xrange(10):
              b = barbero.Barbero().inStream(stream)
              barberi.append(b)
          self.partiti(barberi)

      elif (codice == "RispostePartiti"):
	self.barbero.inStream(stream)
	self.decidiPartito()

      elif (codice == "StrategiaProva"):
	nProva = stream.readInt16()
	self.strategiaProva(nProva)
	
  def serverHasStopped(self):
    self.socket.close()
    sys.exit(0)
						
  def serverHasError(self, error):
    print QString("Error: %1").arg(self.socket.errorString())
    self.socket.close()
    sys.exit(0)
    
  def sceltaCavalli(self, cavalli):
    
    # FIXME prima n lo passavo variabile via argomento
    n = [3, 3, 4]
    
    # calcola quanti ne mancano
    media = [c.media() for c in cavalli]
    mediaECavalli = zip(media, cavalli)
    mediaECavalli.sort()
    media, cavalli = zip(*mediaECavalli)

    selezionati = 0
    boni = []
    outsiders = []
    brenne = []
#    for j, i in enumerate(cavalli):
#      if (i.selezione == 100):
#	selezionati += 1
#	if (j < 6):
#	  n[0] = n[0] -1
#	elif (j > 11):
#	  n[2] = n[2] -1
#	else:
#	  n[1] = n[1] -1
    
    for j, i in enumerate(cavalli):
#      if ((selezionati < 10 and i.selezione != 100) or \
#      (selezionati > 10 and i.selezione == 100)):
        if (j < 6):
            boni.append(i)
	elif (j > 11):
            brenne.append(i)
	else:
            outsiders.append(i)
	    
    # FIXME per il momento scelta indipendente dalla forma
    boni = random.sample(boni, abs(n[0]))
    outsiders = random.sample(outsiders, abs(n[1]))
    brenne = random.sample(brenne, abs(n[2]))
    #boni = boni[0: abs(n[0])]
    #outsiders = outsiders[0: abs(n[1])]
    #brenne = brenne[0: abs(n[2])]
      
    scelta = [10] + [i.indice for i in boni+outsiders+brenne] 
    self.sendMessage(["SceltaCavalli", scelta])    
    
  def sceltaFantino(self, fantini):
      media = []
      # FIXME fixare capacita` di killer qualunque cosa voglia dire
      # FIXME rendere piu` furba la classificazione
      if (self.barbero.strategia != 0):
          media = [f.media() for f in fantini]
      else:
          media = [f.capacita[3] for f in fantini]
      
      mediaEFantini = zip(media, fantini)
      mediaEFantini.sort()
      media, fantini = zip(*mediaEFantini)

      indici = []
      if (self.barbero.strategia == 0): # tira a vincere
          limiti = xrange(6)
      elif (self.barbero.strategia == 1): # outsider
          limiti = xrange(7, 16)
      else: # si vende
          limiti = range(6)
            
      offerte  = []
      for i in limiti:
          f = fantini[i]
      
          # controlla non sia gia` stato preso
          if (f.contrada != -1):
              continue

          # controlla amicizia del fantino
          if (f.feeling[self.barbero.contrada] < 4):
              continue

          # il fantino non puo` costare piu` di meta` del monte della contrada
          if (f.prezzo() > self.contrada.status[2]/2):
              continue
      
          # FIXME per il momento non definisco il prezzo
          prezzo = f.prezzo()+(10 - f.feeling[self.barbero.contrada])*(10 - f.feeling[self.barbero.contrada]) * random.uniform(-0.02, 0.02)
          if (self.barbero.strategia  == 0):
              prezzo += random.uniform(100, 200)
          offerte.append(fantino.Offerta(self.barbero.indice, self.barbero.strategia, f.indice, prezzo))
      
          if (len(offerte) > 2):
              break
	
      #for i in offerte:
	  #print i

      self.sendMessage(["SceltaFantino", offerte])
  
  def decidiFantino(self, off, fantini):
      # FIXME implica che se ha un offerta la sceglie sempre...
      temp = 0
      best_off = -1
      #print "offerte da scegliere: ",off
      for i in off:
       #print fantini[i].nome, fantini[i].media()
          if (fantini[i].media() > temp):
              temp = fantini[i].media()
              best_off = i
    
    self.sendMessage(["FantinoDeciso", best_off])
    
  def partiti(self, barberi, fantini, contrade):
    listaPartiti = []
    
    if (self.barbero.strategia == 2):
      self.sendMessage(["Partiti", []])
      return
    
    if (self.barbero.strategia == 1):
      # FIXME per il momento non fare niente 
      # poi aggiungere che puo`tentare di bloccare l'avversaria
      # cercando di aiutare una vincente
      self.sendMessage(["Partiti", []])
      return
      
    if (self.barbero.strategia == 0):
      # FIXME chi se ne frega dell'amicizia qui ???
      strat = [b.strategia for b in barberi]
      stratEBarberi = zip(strat, barberi)
      stratEBarberi.sort()
      strat, barberi = zip(*stratEBarberi)
      indice = barberi.index(self.barbero.index)
      strat.pop(indice)
      barberi.pop(indice)
      if (len(barberi) != 0):
	if (self.barbero.avversaria != -1):
	  indice_avv = barberi.index(self.barbero.avversaria)
	  strat.pop(indice_avv)
	  barberi.pop(indice_avv)
	da_fermare = barberi[0]
      
        # scegliere chi fermare e poi determinare il migliore antidoto...      
	killer = [b.strategia*fantini[b.fantino].capacita[4] + \
	10 - contrade[b.contrada].feeling[barberi[indice].contrada] + \
	contrade[b.contrada].feeling[self.barbero.indice.contrada] for b in barberi]
	killerEBarberi = zip(killer, barberi)
	killerEBarberi.sort()
	killer, barberi = zip(*killerEBarberi)
	if (len(barberi) != 0):	  
	  chi_ferma = barberi[0]
	  if (barberi[0].avversaria == da_fermare):
	    chi_ferma = barberi[1]
      
          # FIXME fai il check dei soldi (soldi definiti tramite una tabella)
	  spesa = 50
	  if (spesa < self.contrada.status[2]):
	    p = barbero.Partito(self.barbero.indice, da_fermare, chi_ferma, 1, spesa)
	    listaPartiti.append(p)
      if (len(listaPartiti) == 0):
	# controlla se ci sono outsider forti per farli andare piano
	strat = [b.strategia for b in barberi if b.strategia == 1]
	stratEBarberi = zip(strat, barberi)
	stratEBarberi.sort()
	strat, barberi = zip(*stratEBarberi)
	if (len(barberi) > 0):
	  if (barberi[0].strategia > 10):
	    spesa = 100
	    if (spesa < self.contrada.status[2]/2):
	      p = barbero.Partito(self.barbero.indice, -1, barbero[0].indice, 2, spesa)
	      listaPartiti.append(p)
	  
      # FIXME decidi se rompere le palle all'avversaria
      # FIXME in futuro aggiungere le salve e gli accordi per la mossa
      # FIXME aggiungere possibilita` di arrivare ai fantini direttamente
      # FIXME partiti di chi non corre
    
    self.sendMessage(["Partiti", listaPartiti])

  # FIXME muovi strategia contrada qui dal server
    
  def decidiPartito(self):
    if (len(partiti_da_fare) == 0):
      self.sendMessage(["DecisionePartiti",[]])
    
    partitiAccettati = [-1, -1]
    # FIXME il valore limite
    # piu` e` bassa la mia strategia e meno me ne frego dei parametri
    coeff1 = 0
    coeff2 = 0
    for j,i in enumerate(partiti_da_fare):
      
      f_da_fermare = self.contrada.feeling[barberi[i.subisce].contrada]
      f_richiedente = self.contrada.feeling[barberi[i.richiede].contrada]
      s_richiedente = barberi[i.richiede].strategia
      s = self.barbero.strategia
      
      if (i.tipo == 1):
	
	# TIPO 1
	temp = s_richiedente*0.6 - f_da_fermare*0.2 + f_richiedente*0.2
	
	if (temp > coeff1):
	  coeff1 = temp
	  partitiAccettati[0] = j
      
      elif (i.tipo == 2):
	
	# TIPO 2
	temp = (s_richiedente - s)/s

	if (temp > coeff2):
	  coeff2 = temp
	  partitiAccettati[1] = j

    # FIXME puo` fare 1 solo partito a fermare e 1 ad andare piano fermare l'avversaria ha la precedenza su tutto.
    self.barbero.partiti_da_fare = [] #[partiti_da_fare[x for x in partitiAccettati if x != -1]]
    self.sendMessage(["DecisionePartiti",[]])
    
  def strategiaProva(self, nProva):
      # FIXME probabilmente da cambiare tutto
      if (self.cavallo.forma > 80):
          self.barbero.strategiaProve[nProva] = 0
          self.sendMessage(["StrategiaProva", ])
    
      if (self.cavallo.forma > 30 and self.cavallo.forma < 80):
          if (self.fantino.capacita[0] > self.fantino.capacita[1]):
              self.barbero.strategiaProve[nProva] = 1  # prova partenza
          else:
              self.barbero.strategiaProve[nProva] = 2  # prova curve
    
      if (self.cavallo.forma < 30 and i.barbero.strategia == 0):
          self.barbero.strategiaProve[nProva] += 10  # aumenta intensita prova
    
      self.sendMessage(["StrategiaProva",])

        
#app = QCoreApplication(sys.argv)
#form = TDPalioAiClient()
#form.sendMessage("Speriamo funzioni")
#app.exec_()
