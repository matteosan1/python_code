# -*- coding: utf-8 -*-
from PyQt4.QtCore import QString

class Cavallo:
  def __init__(self):
    self.indice = -1
    self.score = [0,0,0,0]       # eta, tratte, corsi, vinti
    self.nome = QString("")
    self.colore = 0
    self.caratteristiche = [0,0,0,0,0]      # scatto(ripresa), velocita max, resistenza, precisione sm, precisione casato
    self.capacita = [0,0,0,0,0]      # scatto(ripresa), velocita max, resistenza, precisione sm, precisione casato
    self.selezione = 9999
    self.coscia = -1
    self.infortunio = 0

  def __str__(self):
    s = str(self.nome) + " " + str(self.forma)
    return s
    
  def media(self):
    result = 0
    for i in self.capacita:
      result += i
    result = (float(result)/3.)
    return result
    
  def caricaDati(self, file):
    self.nome = QString(file.readline().split("\r\n")[0])
    line = file.readline().split(" ")
    self.indice = int(line[0])
    self.colore = int(line[1])
    self.capacita = [int(x) for x in line[2:5]]
    self.score = [int(x) for x in line[5:]] 

  def inTextStreamer(self, stream):
    t = QString()
    self.nome = stream.readLine()
    self.nome = stream.readLine()
    stream >> t
    self.colore = int(t)
    stream >> t
    self.indice = int(t)
    for i in xrange(len(self.score)):
      stream >> t
      self.score[i] = int(t)
    for i in xrange(len(self.caratteristiche)):  
      stream >> t
      self.caratteristiche[i] = int(t)
    for i in xrange(len(self.capacita)):  
      stream >> t
      self.capacita[i] = int(t)
    stream >> t
    self.selezione = int(t)
    stream >> t
    self.coscia = int(t)
    stream >> t
    self.infortunio = int(t)

  def outTextStreamer(self, stream):
    stream << self.nome << "\n"
    stream << self.colore << "\n"
    stream << self.indice << "\n"
    for i in self.score:
      stream << i << " " 
    stream  << "\n"
    for i in self.caratteristiche:  
      stream << i << " "
    for i in self.capacita:  
      stream << i << " "
    stream  << "\n"
    stream << self.selezione << "\n"
    stream << self.coscia << "\n"
    stream << self.infortunio << "\n"    

  def outStreamer(self, stream):
    stream << self.nome
    stream.writeInt16(self.indice)
    for i in self.score:
      stream.writeInt16(i)
    for i in self.caratteristiche:  
        stream.writeInt16(i)
    for i in self.capacita:  
      stream.writeInt16(i)
    stream.writeInt16(self.selezione)
    stream.writeInt16(self.coscia)
    
  def inStreamer(self, stream):
    stream >> self.nome
    self.indice = stream.readInt16()
    for i in xrange(len(self.score)):
       self.score.append(stream.readInt16())
    for i in xrange(len(self.caratteristiche)):
      self.caratteristiche.append(stream.readInt16())
    for i in xrange(len(self.capacita)):
      self.capacita.append(stream.readInt16())
    self.selezione = stream.readInt16()
    self.coscia = stream.readInt16()
