#! /usr/bin/python
import Punteggi

class Giocatore():
    def __init__(self):
        self.indice = -1
        self.nome = ""
        self.cognome = ""
        self.ruolo = 0   # 0 portiere, 1 difensore, 2 centrocampista, 3 attaccante, 4 fuori rosa
        self.prezzo = 0
        self.squadra = ""
        self.prestazioni = [[0,[0,0],0,0,0,0,0,0]]
        self.inFormazione = -1

    def nomeCompleto(self):
        return self.cognome+" "+self.nome[0]+"."

    def haSegnato(self, p):
        if self.ruolo == 0:
            if self.prestazioni[p][4] != 0 or self.prestazioni[p][6] != 0:
                return True
            else:
                return False
        else:
            if self.prestazioni[p][2] != 0 or self.prestazioni[p][3] != 0:
                return True
            else:
                return False

    def ammonito(self, p):
        if (self.prestazioni[p][1][1] == 1):
            return True
        else:
            return False
    
    def espulso(self, p):
        if (self.prestazioni[p][1][1] == 2):
            return True
        else:
            return False

    def addPrestazione(self, p):
        self.prestazioni.append(p)
        
    def replacePrestazione(self, g, p):
        self.prestazioni[g] = p
    
    # FIXME cosi` e` sbagliata
    def mediaUltime4(self, giornata, punti):
        return self.faiPunteggio(giornata, punti)

    def voto(self, giornata, punti):
        return self.faiPunteggio(giornata, punti)
    
    def media(self, punti):
        totale = 0
        giocate = 0
        for i,p in enumerate(self.prestazioni):
            if (p[1][0] != 0):
                totale += self.faiPunteggio(i, punti)
                giocate += 1
        if totale == 0:
            return 0
        else:
            return float(totale)/float(giocate)

    def giocate(self):
        giocate = 0
        for p in self.prestazioni:
            if (p[1][0] != 0):
                giocate += 1

        return giocate

    def ammonizioni(self):
        amm = 0
        for p in self.prestazioni:
            if (p[1][1] == 1):
                amm += 1

        return amm

    def espulsioni(self):
        amm = 0
        for p in self.prestazioni:
            if (p[1][1] == 2):
                amm += 1

        return amm

    def goal(self):
        goal = 0
        if self.ruolo == 0:
            for p in self.prestazioni:
                goal += p[4]
        else:
            for p in self.prestazioni:
                goal += p[2]
        
        return goal

    def autogoal(self):
        goal = 0
        for p in self.prestazioni:
            goal += p[7]

        return goal

    def rigori(self):
        rigori = 0
        sbagliati = 0
        if self.ruolo == 0:
            for p in self.prestazioni:
                rigori += p[5]
            if rigori != 0:
                return str(int(rigori))
            else:
                return ""
        else:
            for p in self.prestazioni:
                rigori += p[3]
                sbagliati += p[6]
            if (rigori != 0 or sbagliati != 0):
                return str(int(rigori))+"("+str(int(sbagliati))+")"
            else:
                return ""

    def faiPunteggio(self, giornata, punti):
        tags = self.prestazioni[giornata]
        if (tags[1][1] == 1):
            totale = tags[1][0] + punti.am + tags[2]*punti.gse + tags[3]*punti.rse + tags[4]*punti.gsu + tags[5]*punti.rp + tags[6]*punti.rsb + tags[7]*punti.au
        elif (tags[1][1] == 2):
            totale = tags[1][0] + punti.es + tags[2]*punti.gse + tags[3]*punti.rse + tags[4]*punti.gsu + tags[5]*punti.rp + tags[6]*punti.rsb + tags[7]*punti.au
        else:
            totale = tags[1][0] + tags[2]*punti.gse + tags[3]*punti.rse + tags[4]*punti.gsu + tags[5]*punti.rp + tags[6]*punti.rsb + tags[7]*punti.au

        # quattro punti per il goal del difensore
        if (tags[0] == 1 and tags[2] > 0):
            totale += tags[2]
            
        if (tags[1][0] == 0 and tags[1][1] > 0):
            totale += 6.0

        return totale
