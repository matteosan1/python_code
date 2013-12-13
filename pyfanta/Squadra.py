#! /usr/bin/python
import re
import Giocatore
import Punteggi, IO
from operator import attrgetter

class Squadra():
    def __init__(self):
        self.nome = ""
        self.anno = 1974
        self.giornata = -1
        self.giocatori = []
        self.prestazioni = [0]
        self.formazioni = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]*40
        self.punteggi = Punteggi.Punteggi()

    def schemaPerGiornata(self, p):
        indici = [i.indice for i in self.giocatori]
        ruoli = [0,0,0]
        for i in self.formazioni[p][0:11]: 
            indice = indici.index(i)
            ruolo = (self.giocatori[indice].ruolo)%10
            if ruolo != 0:
                ruoli[ruolo-1] += 1
        return str(ruoli[0])+"-"+str(ruoli[1])+"-"+str(ruoli[2])
        
    def ordinaGiocatori(self):
        for i in self.giocatori:
            i.cognome = str(i.cognome)
            i.nome = str(i.nome)
            i.squadra = str(i.squadra)
        self.giocatori = sorted(self.giocatori, key=attrgetter('ruolo', 'cognome', 'nome'))
        
    def presenze(self, g):
        partite = 0
        panchine = 0
        for i,p in enumerate(self.formazioni[1:]):
            if (self.giocatori[g].indice in p):
                pos = p.index(self.giocatori[g].indice)
                if pos < 11:
                    partite += 1
                else:
                    panchine += 1

        return str(partite)+"("+str(panchine)+")"

    def haGiocato(self, p, g):
        formazione_finale = [a[0] for a in self.sostituzioni(p)[0]]
        if (g in formazione_finale):
            if self.giocatori[g].prestazioni[p][1][0] != 0:
                return 1
            else:
                return 2

        return 0
               
    def addFormazione(self, f, g):
        self.formazioni[g] = f
        
    def addGiocatore(self, g):
        g.prestazioni = [[0,[0,0],0,0,0,0,0,0]]*40
        self.giocatori.append(g)

    def mediaTotale(self):
        totale = 0
        for i in xrange(1, self.giornata+1):
            totale += self.totale(i)[2]
        return float(totale)/float(self.giornata)

    def sostituzioni(self, giornata):
        indici = [g.indice for g in self.giocatori]
        formazione = []
        panchina = []
        for i in self.formazioni[giornata][0:11]:
            formazione.append([indici.index(i), self.giocatori[indici.index(i)].faiPunteggio(giornata, self.punteggi)])
        for i in self.formazioni[giornata][11:]:
            if (i != -1):
                panchina.append([indici.index(i), self.giocatori[indici.index(i)].faiPunteggio(giornata, self.punteggi)])
            else:
                panchina.append([-1, 0])
              
        panchina = [panchina[0]]+[panchina[2]]+[panchina[4]]+[panchina[1]]+[panchina[3]]+[panchina[5]]
        panchina = panchina[0:3]+sorted(panchina[3:], key=lambda panchina: panchina[1], reverse = True)
    
        sv = [j for j,i in enumerate(formazione) if i[1] == 0]
        if (len(sv) > 0):
           # print sv
            sost = 0
            for i in panchina:
                if (i[0] == -1):
                    continue
                #print i
                ruolo = self.giocatori[i[0]].ruolo%10
                for j in sv:
                    #print "j",j
                    if (self.giocatori[formazione[j][0]].ruolo%10 == ruolo):
                        temp = formazione[j]
                        formazione[j] = i
                        i = temp
                        sost = sost+1
                        sv.remove(j)
                        break
                    if (sost == 3):
                        break
        return (formazione, panchina)

    def totale(self, giornata):
        formazione = self.sostituzioni(giornata)[0]
        panchina = self.sostituzioni(giornata)[1]
        totale = 0.0

        for i in formazione:
            totale = totale + i[1]
            # FIXME per casi specialissimi...
            if (self.giocatori[i[0]].ruolo == 0 and self.giocatori[i[0]].prestazioni[giornata][1][0] == 0):
                totale += 6.0
            
        if (giornata <= self.giornata):
            self.prestazioni[giornata] = totale
        elif (giornata > self.giornata+1):
            for i in xrange(self.giornata, giornata):
                self.prestazioni.append(0)
            self.prestazioni.append(totale)
        else:
            self.prestazioni.append(totale)

        return (formazione, panchina, totale)

    def trovaGiocatore(self, l, lista):
        for j,i in enumerate(lista):
            if (l == i):
                return j
        else:
            return -1
    
    def calcoloPrestazione(self, tags, giornata):
        for ind,g in enumerate(self.giocatori):
            nome = g.cognome.upper() + " " + g.nome.upper()
            match = ""
            for string in tags.keys():
                n = nome[0:len(string)].upper()
                if (string.endswith(".")):
                    n = n[:-1]+ "."
                #m = re.match(n, string)
                #if (m is not None):
                #    match = string
                #    break
                if (n == string):
                    match = string
                    break
            
            if (match != ""):
                g.replacePrestazione(giornata, tags[match])
            else:
                g.replacePrestazione(giornata, [0,[0,0],0,0,0,0,0,0])

