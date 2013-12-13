#! /usr/bin/python

import sys

class Container:

    def __init__(self):
        self.mappa = [4, 20, 4, 8, 6, 15, 9, 9, 4, 23, 19, 22, 22, 3, 5, 16, 2, 20, 17, 20, 2, 14, 11, 6, 8, 11, 14, 17, 7, 19, 4, 11, 7, 6, 6, 15, 7, 24, 11, 13, 4, 20, 4, 8, 6, 15, 9, 9, 4, 23]
        print sum(self.mappa)
        self.tavoli = [7, 14, 14, 28, 28, 56, 56, 56, 56, 56, 56, 56, 56, 56, 28]
    
    def checkPosti(self, n):
        posti_tavolo = sum(self.tavoli)
        richieste = sum(self.mappa[0:n])
        if (posti_tavolo < richieste):
            print "Impossibile ! (%d, %d)" %(posti_tavolo, richieste)
            sys.exit(0)

    def matchTavGru(self, gen):
        m = []
        indice_mappa = 0
        for t in self.tavoli:
            r = t
            temp = []
            while(r > 0 and indice_mappa < len(gen)):
                r = r - self.mappa[gen[indice_mappa]]
                if (r < 0):
                    r = r + self.mappa[gen[indice_mappa]]
                    break
                temp.append(gen[indice_mappa])
                indice_mappa += 1
            temp.append("")
            temp.append(t - r)
            m.append(temp)
        
        return m

    def eval_func(self, gen):
        indice_gruppo = 0
        score = 0.0
        for t in self.tavoli:
            riempimento = t
            while (riempimento > 0 and indice_gruppo < len(gen)-1):
                riempimento -= self.mappa[gen[indice_gruppo]]
                indice_gruppo += 1
            if (riempimento == 0):
                score += t*2
            elif (riempimento == t):
                score -= t
            elif (riempimento == t and indice_gruppo == (len(gen)-1)):
                score = 0
            elif (riempimento > 0):
                score += 5*(t - riempimento)
            elif (riempimento < 0):
                score -= t
                
        #print indice_gruppo
        if (score < 0):
            score = 0

        for i in xrange(gen.getListSize()):
            c = gen.genomeList.count(i)
            if (c > 1):
                score = score/2.
                break

        #print indice_gruppo, len(gen)
        if (indice_gruppo != (len(gen)-1)):
            score = 0
        
        return score
