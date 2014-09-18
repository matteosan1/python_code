import queryUpdatedDB
import Sunto
import subprocess

# controlla aggiornamenti del DB
if (not queryUpdatedDB.checkSize()):
    queryUpdatedDB.getUpdatedDB()
else:
    print "Il DB non e` stato aggiornato recentemente."


# estrazione contrade
#   data + inserimento contrade + chi ha estratto chi
# ad ogni step aggiorna DB in rete

# notizie generali palio
#   pittore, dedica, dirigenze...

# tratta

link = raw_input()

if (not link == ""):
    #inserimento manuale
    subprocess.call("wget -O lista_cavalli.txt http://www.sunto.biz/2014/06/29/la_presentazione_dei_cavalli.htm", shell=True)
    Sunto.parseHTML()
else:
    pass
    Sunto.parseHTML()



#   raccogli lista cavalli (via rete con parsing pdf ?), inserimento mauale
#   tabella con dati assegnazione (senza batterie)

# prove
#   note/per prova (corsa, mossa, cambi fantini...)

# palio
#   mossa, tempo, descrizione, 

