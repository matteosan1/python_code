# -*- coding: utf-8 -*-
from PyQt4.QtCore import QString
import nomi

class Offerta:
  def __init__(self, c1=-1, c2=-1, c3=-1, c4=-1):
    self.chi = c1
    self.strategia = c2
    self.fantino = c3
    self.soldi = c4
    
  def __str__(self):
    s = "Chi: " + str(self.chi) + " - fantino: " + str(self.fantino)
    return s
  
  def inTextStreamer(self, stream):
    t = QString()
    stream >> t
    self.chi = int(t)
    stream >> t
    self.strategia = int(t)
    stream >> t
    self.fantino = int(t)
    stream >> t
    self.soldi = int(t)

  def outTextStreamer(self, stream):
    stream << self.chi << " "
    stream << self.strategia << " "
    stream << self.fantino << " "
    stream << self.soldi << " " 
    stream << "\n"
    
  def outStreamer(self, stream):
    stream.writeInt16(self.chi)
    stream.writeInt16(self.strategia)
    stream.writeInt16(self.fantino)
    stream.writeInt16(self.soldi)
	  
  def inStreamer(self, stream):
    self.chi = stream.readInt16()
    self.strategia = stream.readInt16()
    self.fantino = stream.readInt16()  
    self.soldi = stream.readInt16()  
    
    
class Fantino:
  def __init__(self):
    self.indice = -1
    self.score = [0, 0, 0]    # anni, palii corsi, palii vinti
    self.nome = QString("-")
    self.nomeVero = QString(nomi.nome())
    self.caratteristiche = [0, 0, 0, 0] # prontezza, precisione sm, precisione ca, killer
    self.capacita = [0, 0, 0, 0] # prontezza, precisione sm, precisione ca, killer
    self.feeling = []
    for i in range(0, 17):
      self.feeling.append(6)
    self.contrada = -1
    self.infortunio = 0
    self.offerte = []

  def __str__(self):
    return str(self.nome)

  def creaFantino(self, a0, a, a1, b, c, d, e, f):
    index = a0;
    self.nome = a
    self.nomeVero = a1
    self.capacita = b
    self.score = c
    self.feeling = d
    self.contrada = e
    self.offerte = f
    
  def prezzo(self):
    # FIXME calcolare il vero prezzo
    return 100
    
  def media(self):
    # FIXME migliorarla
    media = float(0)
    for i in range(0,3):
      media = media + float(self.capacita[i])
    
    return media/3.
    
  def caricaDati(self, file):
    self.nome = file.readline().split("\r\n")[0]
    self.nomeVero = file.readline().split("\r\n")[0]
    line = file.readline().split(" ")
    self.feeling = [int(x) for x in line[-18:-1]]
    self.contrada = int(line[-1])
    self.infortunio = int(line[7])
    self.indice = int(line[0])
    self.capacita = [int(x) for x in line[1:5]]
    self.score = [int(x) for x in line[5:8]]

  def inTextStreamer(self, stream):
    t = QString()
    stream >> t
    self.indice = int(t) 
    self.nome = stream.readLine(75)
    self.nome = stream.readLine(75)
    self.nomeVero = stream.readLine(75)
    for i in xrange(len(self.score)):
      stream >> t
      self.score[i] = int(t)
    for i in xrange(len(self.caratteristiche)):
      stream >> t  
      self.caratteristiche[i] = int(t)
    for i in xrange(len(self.capacita)):
      stream >> t  
      self.capacita[i] = int(t)
    for i in xrange(17):
      stream >> t
      self.feeling[i] = int(t)
    stream >> t
    self.contrada = int(t)
    stream >> t
    self.infortunio = int(t)
    #stream << len(self.offerte) << "\n"
    #for i in self.offerte:
      #i.outTextStreamer(stream)

  def outTextStreamer(self, stream):
    stream << self.indice << "\n"
    stream << QString(self.nome) << "\n"
    stream << QString(self.nomeVero) << "\n"
    for i in xrange(len(self.score)):
      stream << self.score[i] << " "
    stream << "\n"
    for i in xrange(len(self.caratteristiche)):  
      stream << self.caratteristiche[i] << " "
    for i in xrange(len(self.capacita)):  
      stream << self.capacita[i] << " "
    stream << "\n"
    for i in xrange(17):
      stream << self.feeling[i] << " "
    stream << "\n"
    stream << self.contrada << "\n"
    stream << self.infortunio << "\n"
    #stream << len(self.offerte) << "\n"
    #for i in self.offerte:
      #i.outTextStreamer(stream)

  def outStreamer(self, stream):
    stream.writeInt16(self.indice)
    stream << QString(self.nome)
    stream << QString(self.nomeVero)
    for i in self.score:
      stream.writeInt16(i)
    for i in self.caratteristiche:  
      stream.writeInt16(i)
    for i in self.capacita:  
      stream.writeInt16(i)
    for i in xrange(17):
      stream.writeInt16(self.feeling[i])
    stream.writeInt16(self.contrada)
    stream.writeInt16(self.infortunio)
    #stream.writeInt16(len(self.offerte))
    #for i in self.offerte:
      #i.outStreamer(stream)
    
  def inStreamer(self, stream):
    self.indice = stream.readInt16()
    stream >> self.nome
    stream >> self.nomeVero
    for i in xrange(len(self.score)):
      self.score[i] = stream.readInt16()
    for i in xrange(len(self.caratteristiche)):
      self.caratteristiche[i] = stream.readInt16()
    for i in xrange(len(self.capacita)):
      self.capacita[i] = stream.readInt16()
    for i in xrange(17):
      self.feeling[i] = stream.readInt16()
    self.contrada = stream.readInt16()
    self.infortunio = stream.readInt16()
    
    #nofferte = stream.readInt16()
    #for i in xrange(nofferte):
      #o = Offerta()
      #self.offerte.append(o.inStreamer(stream))
      
