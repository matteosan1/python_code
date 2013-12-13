class Cavallo:
  scatto = 5
  vel_max = 50
  resistenza = 10
  
class Fantino:
  prontezza = 0
  
class Barbero:
  
  fantino = Fantino()
  cavallo = Cavallo()
  d = 0
  x = 0
  dec = 5
  acc = cavallo.scatto
  vel = 0
  vel_max = cavallo.vel_max
  giro = 0
  rischio = [10, 10, 10]
  andatura = [0, 0, 0]
    
  def mossa(self):
    
    
  def fatigue(self):
    if (self.vel > self.vel_max*0.75):
      self.vel_max = self.vel_max - 0.1*(11-self.cavallo.resistenza)
    if (self.vel_max < 30):
	self.vel_max = 30
  
  def decelerate(self):
    self.vel = self.vel - self.dec
    if (self.vel < 0):
      self.vel = 0

  def accelerate(self, giro):
    vel_eff = self.vel_max
    if (self.andatura[giro] == 0):
      vel_eff = vel_eff * 0.75
    self.vel = self.vel + self.acc
    if (self.vel > vel_eff):
      self.vel = vel_eff
      
  def move(self):
    self.d = self.d + self.vel
    
   
