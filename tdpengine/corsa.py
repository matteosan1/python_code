#! /usr/bin/python

from barbero import *

barberi = []

for i in xrange(10):
  barberi.append(Barbero())

# mossa
# dipende dalla prontezza del fantino
# dallo scatto del cavallo


while(1):  
  print barberi[0].d + 3000*barberi[0].giro, barberi[0].vel
  
  bd_smartino = 1000. - ((barberi[0].vel**2) - (barberi[0].rischio[barbero[0].giro]**2))/(2*barberi[0].dec)

  bd_casato = 2000. - ((barberi[0].vel**2) - (barberi[0].rischio[barbero[0].giro]**2))/(2*barberi[0].dec)  

  if ((barberi[0].d > bd_smartino and barberi[0].d < 1100) or
      (barberi[0].d > bd_casato and barberi[0].d < 2100)):
    if (barberi[0].vel > barberi[0].rischio[barbero[0].giro]):
      barberi[0].decelerate()	
  else:
    barberi[0].accelerate()
  
  # move
  barberi[0].move()

  # check falls
  #dipende da velocita
  # dipende da bravura fantino
  # dipende da precisione cavallo
  # in caso di caduta
  # il cavallo si ferma ? 50/50
  # infortunio fantino, cavallo
  
  # update fatigue
  barberi[0].fatigue()
  
  # check end
  if (barberi[0].d > 3000):
    barberi[0].d = barberi[0].d - 3000
    barberi[0].giro = barberi[0].giro + 1

  if (barberi[0].giro == 3):
    break
    
