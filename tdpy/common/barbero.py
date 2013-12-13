# -*- coding: utf-8 -*-
from PyQt4.QtCore import QString

import cavallo
import fantino
import contrada

class Partito:
  def __init__(self, r=-1, s=-1, e =-1, t=0, sol=0, eseg = False):
    self.richiede = r
    self.subisce = s
    self.esegue =  e
    self.tipo = t
    self.soldi = sol
    self.eseguito = eseg
    
  def inTextStream(self, stream):
    t = QString()
    stream >> t
    self.richiede = int(t)
    stream >> t
    self.subisce = int(t)
    stream >> t
    self.esegue = int(t)
    stream >> t
    self.tipo = int(t)
    stream >> t
    self.soldi = int(t)
    stream >> t
    self.eseguito = int(t)

  def outTextStreamer(self, stream):
    stream << self.richiede << "\n"
    stream << self.subisce << "\n"
    stream << self.esegue << "\n"
    stream << self.tipo << "\n"
    stream << self.soldi << "\n"
    stream << int(self.eseguito) << "\n"

  def outStreamer(self, stream):
    stream.writeInt16(self.richiede)
    stream.writeInt16(self.subisce)
    stream.writeInt16(self.esegue)
    stream.writeInt16(self.tipo)
    stream.writeInt16(self.soldi)
    stream.writeBool(self.eseguito)
      
  def inStreamer(self, stream):
    self.richiede = stream.readInt16()
    self.subisce = stream.readInt16()
    self.esegue = stream.readInt16()
    self.tipo = stream.readInt16()
    self.soldi = stream.readInt16()
    self.eseguito = stream.readBool()
    
class Barbero:
  def __init__(self):
    self.indice = -1
    self.contrada = -1
    self.fantino = -1
    self.cavallo = -1
    self.strategiaProve = [-1,-1,-1,-1,-1,-1]
    self.strategia = -1
    self.avversaria = -1 # c'e` gia` in contrada
    self.partiti_richiesti = []
    self.partiti_da_fare = []
  
  def __str__(self):
    print self.contrada

  def outTextStreamer(self, stream): 
      stream << self.indice << " " << self.contrada << " " << self.fantino << " " << self.cavallo << "\n"
      for i in xrange(6):
          stream << self.strategiaProve[i] << " " 
      stream << self.strategia << "\n"

  def inTextStreamer(self, stream):
    t = QString()
    stream >> t
    self.indice = int(t)
    stream >> t
    self.contrada = int(t)
    stream >> t
    self.fantino = int(t)
    stream >> t
    self.cavallo = int(t)
    for i in xrange(6):
        stream >> t
        self.strategiaProve[i] = int(t)
    stream >> t
    self.strategia = int(t)
      
  def outStreamer(self, stream):
    stream.writeInt16(self.indice)
    stream.writeInt16(self.contrada)
    stream.writeInt16(self.fantino)
    stream.writeInt16(self.cavallo)
    for i in xrange(6):
      stream.writeInt16(self.strategiaProve[i])
    stream.writeInt16(self.strategia)
      
  def inStreamer(self, stream):
    self.indice = stream.readInt16()
    self.contrada = stream.readInt16()
    self.fantino = stream.readInt16()
    self.cavallo = stream.readInt16()
    for i in xrange(6):
      self.strategiaProve[i] = stream.readInt16()
    self.strategia = stream.readInt16()
      
