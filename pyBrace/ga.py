import random
import copy

class Gruppo(object):
    
    def __init__(self, n, persone = 0):
        self.persone = persone or self._gruppocasuale()
        self.index = n

    def _gruppocasuale(self):
        return int(random.uniform(1, 10))

    def __str__(self):
        return "Gruppo: " + str(self.index) + " - "+ str(self.persone)


class Tavolo(object):

    def __init__(self, n, posti = 10):
        self.indice_gruppi = []
        self.posti = posti
        self.index = n
        
    def __str__(self):
        s = ""
        for i in self.indice_gruppi:
            s = s + str(i) + " "
        s = s + "\n"
        return s

class Cena(object):

    def __init__(self, tavoli = [], gruppi = []):
        self.gruppi = gruppi
        self.score = 0
        self.tavoli = tavoli
        self.gruppiInPiedi = []
        self.inPiediWeight = 2
        self.postiVuotiWeight = 1

    def riparaTavolo(self):
        for g in self.gruppi:
            pos = []
            for i,t in enumerate(self.tavoli):
                if (g.index in t.indice_gruppi):
                    pos.append(i)
            if (len(pos) > 1):
                indiceTavoli = random.choice(pos, len(pos)-1)
                for i in indiceTavoli:
                    self.tavoli[i].remove(g.index)
            else if (len(pos) == 0):
                self.gruppiInPiedi.append(g)
        # FIXME aggiungi a caso gruppi in piedi

    def personeGruppo(self, index):
        for g in self.gruppi:
            if g.index == index:
                return g.persone
        return -1

    def _score(self):
        s = 0
        for t in self.tavoli:
            p = 0
            for i in t.indice_gruppi:
                p += self.personeGruppo(i)
            diff = 0
            if p != 0:
                diff = (t.posti - p)
                s += -self.postiVuotiWeight*diff
        return s
            
    
    def crossover(self, other):
        pass

    def __str__(self):
        s = ""
        for t in self.tavoli:
            s = s + str(t)
        return s
        
    def __cmp__(self, other):
        return cmp(self._score(), other._score())
    

class Popolazione():
    cene = []
    gruppi = []
    tavoli = []
    popolazione = 0

    def __init__(self, popolazione = 10, gruppi = [], tavoli = []):
        self.popolazione = popolazione
        self.gruppi = gruppi
        self.tavoli = tavoli
        self.generaPopolazione()

    def generaPopolazione(self):
        for p in xrange(self.popolazione):
            tav = copy.deepcopy(self.tavoli)
            g = random.sample(self.gruppi, len(self.gruppi))
            gruppi_per_tavolo = len(g)/len(tav)+1
            for n,t in enumerate(tav):
                indici = [i.index for i in  g[n*gruppi_per_tavolo:(1+n)*gruppi_per_tavolo]]
                t.indice_gruppi = indici
                
            c = Cena(tav, self.gruppi)
            self.cene.append(c)

    def sort(self):
        self.cene.sort()

    def run(self):
        self.sort()
        self.cene = self.cene[0:self.popolazione/2]
        self.breeding()
        
        # fai accoppiare coppie casuali
        # muta il figlio
        # riparalo
        # ripeti finche` il numero di cene e` ristabilito

    def breeding(self):
        c1 = random.choice(self.cene)
        c2 = random.choice(self.cene)
        c = Cena(copy.deepcopy(self.tavoli), self.gruppi)
        for t1, t2 in zip(c1.tavoli, c2.tavoli):
            print t1






        
    def __str__(self):
        s = ""
        for i,c in enumerate(self.cene):
            s = s + "Cena " + str(i) + " (" + str(c._score()) + ")\n"
            s = s + str(c) 
            s = s + "\n"
        return s


if __name__ == "__main__":
    gruppi = []
    tavoli = []
    for i in xrange(4):
        gruppi.append(Gruppo(n=i))

    persone = 0
    for i in gruppi:
        persone += i.persone
        
    for i in xrange(persone/10 + 1):
        tavoli.append(Tavolo(n=i))
            
    env = Popolazione(10, gruppi, tavoli)
    env.run()
        

