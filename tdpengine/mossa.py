# ostacolo dei partiti: 
# ostacolo = brav_partiti_fantino, chi_ha_la_mossa, prontezze fantini
# facile da la mossa, toglie la mossa a 2 soli cavalli
# per il resto solo se sono accanto ???????

import random

#FIXME da aggiungere i partiti

def mossa(cavalli, fantini):
  result = []
  for i in range(0,10):
    limite = cavalli[i].scatto + fantini[i].prontezza
    result.append(randint(-3, limite)

  return result
