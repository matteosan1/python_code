import random
from PyQt4.QtCore import *

class Fase(QObject):
  def __init__(self):
    super(Fase, self).__init__()
    self.nomeFasi = ("Inizio", "Estrazione", "SceltaCavalli", "SceltaFantino", \
    "Partiti", "StrategiaProva", "CorsaProva", "AggiornaFantino", "Segnatura", \
    "Mossa", "PartitiMossa", "Palio", "PostPalio")
    self.votazioni = 0
    self.fase = 0
    self.anno = 2009
    self.mese = 0
    self.nprova = 0
    self.nomeProve = ["Prima Prova", "Seconda Prova", "Terza Prova", "Quarta Prova", \
    "Prova Generale", "Provaccia"]
    self.prove = []
    self.luglio = []
    self.agosto = []
    self.straordinario = []
    
  def nuovaFase(self):
    self.fase += 1
    if (self.fase == 8):
      self.nprova += 1
      self.fase = 4
      if (self.nprova == 6):
	self.nprova = 0
	self.fase = 9
      
    self.emit(SIGNAL("nuovaFase"), self.nomeFasi[self.fase])
    
  def chi_corre(self):
    if (self.mese == 0):
      return self.luglio[0:10]
    elif (self.mese == 1):
      return self.agosto[0:10]
    else:
      return self.straordinario[0:10]
      
  def chi_non_corre(self):
    if (self.mese == 0):
      return self.luglio[10:]
    elif (self.mese == 1):
      return self.agosto[10:]
    else:
      return self.straordinario[10:]   
      
  def estrazione(self, c):
      # inizializzazione contrade 
      if (c == -1):
          random.seed(1)
          self.luglio = random.sample(xrange(0, 17), 17)
          self.agosto = random.sample(xrange(0, 17), 17)
          self.straordinario = random.sample(xrange(0, 17), 17)
          
      # estrazione palio straordinario
      if (c == 2):
          self.straordinario = random.sample(xrange(0, 17), 17)
    
      # estrazione normale
      if (c == 1):
          self.prove = []
          if (self.mese == 1):
              self.mese == 0
              self.luglio = self.luglio[10:17] + random.sample(self.luglio[0:10], 10)
              self.prove.append([self.luglio[0:10]])
              self.prove.append([self.agosto[10:0]]) 
              return
          if (self.mese == 0):
              self.mese == 1	
              self.agosto = self.agosto[10:17] + random.sample(self.agosto[0:10], 10)
              self.prove.append([self.agosto[0:10]]) 
              self.prove.append([self.agosto[10:0]]) 
              
  def numeri_di_coscia(self):
    return random.sample(xrange(0, 20), 20)
  
  def mossa(self):
    return random.sample(xrange(0, 10), 10)
    
  def assegnazione(self):
    result = []
    orecchio = random.sample(xrange(0, 10), 10)
    contrada = random.sample(xrange(0, 10), 10)
    # ordina le contrade secondo il numero di orecchio capitato
    # FIXME torna ????
    self.prove.append([orecchio[0:10]]) 
    self.prove.append([orecchio[10:0]]) 
    self.prove.append([contrada[0:10]]) 
    self.prove.append([contrada[10:0]]) 
    
    for i in xrange(0, 10):
      result.append([orecchio[i], contrada[i]])
    
    return result
    
  
     
    
	
	  
