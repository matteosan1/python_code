# -*- coding: utf-8 -*-

class Contrada:
  
  def __init__(self):
    self.nome = ""
    self.nomeCompleto = ""
    self.indice = int()          # 1 Aquila, 2 Bruco, 3 Chiocciola...
    self.status = [0, 0, 0, 0]   # avversaria, popolo, denaro, umore
    self.vittorie = [0, 0 ,0 ,0] # luglio, agosto, settembre, cuffia
    self.giocatore = -1          # -1 niente altrimenti indice del vettore di giocatori
    self.fantino = -1            # eventuale indice del fantino di contrada  
    self.feeling = []
    for i in range(0, 17):
      self.feeling.append(6)     # rapporto con le altre contrade

  def setContrada(self, j, a, d, b, c):
    self.nome = a;
    self.nomeCompleto = d;
    self.indice = j;
    for i in range(0, 3):
      self.status[i] = b[i]	  
    for i in range(0, 17):
      self.feeling[i] = c[i]
   
  def caricaDati(self, file):
    self.nome = file.readline().split("\r\n")[0]
    self.nomeCompleto = file.readline().split("\r\n")[0]    
    self.indice = int(file.readline())
    self.status = [int(x) for x in file.readline().split(" ")]
    self.vittorie = [int(x) for x in file.readline().split(" ")]
    self.giocatore, self.fantino = [int(x) for x in file.readline().split(" ")]
    self.feeling = [int(x) for x in file.readline().split(" ")]

  def inTextStreamer(self, stream):
    t = ""
    self.nome = stream.readLine(75)
    self.nome = stream.readLine(75)
    self.nomeCompleto = stream.readLine(75)
    stream >> t
    self.indice = int(t)
    for i in xrange(4):
      stream >> t
      self.status[i] = int(t)
    for i in xrange(4):
      stream >> t
      self.vittorie[i] = int(t)
    stream >> t
    self.giocatore = int(t)
    stream >> t
    self.fantino = int(t)
    for i in xrange(17):  
      stream >> t
      self.feeling[i] = int(t)

  def outTextStreamer(self, stream):
    stream << self.nome << "\n"
    stream << self.nomeCompleto << "\n"
    stream << self.indice << "\n"
    for i in xrange(4):
      stream << self.status[i] << " " 
    stream << "\n"
    for i in xrange(4):
      stream << self.vittorie[i] << " "
    stream << "\n"
    stream << self.giocatore << "\n"
    stream << self.fantino << "\n"
    for i in xrange(17):  
      stream << self.feeling[i] << " "
    stream << "\n"

  def outStreamer(self, stream):
    stream << self.nome
    stream << self.nomeCompleto
    stream.writeInt16(self.indice)
    for i in xrange(4):
      stream.writeInt16(self.status[i])
    for i in xrange(4):
      stream.writeInt16(self.vittorie[i])
    stream.writeInt16(self.giocatore)
    stream.writeInt16(self.fantino)
    for i in xrange(17):  
      stream.writeInt16(self.feeling[i])
      
  def inStreamer(self, stream):
    stream >> self.nome
    stream >> self.nomeCompleto
    self.indice = stream.readInt16()
    for i in xrange(4):
      self.status[i] = stream.readInt16()
    for i in xrange(4):
      self.vittorie[i] = stream.readInt16()
    self.giocatore = stream.readInt16()
    self.fantino = stream.readInt16()
    for i in xrange(17):  
      self.feeling[i] = stream.readInt16()
