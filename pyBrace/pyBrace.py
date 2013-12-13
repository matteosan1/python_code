#! /usr/bin/python
import sys
import random

class pyBrace():
    mutazioni = 20
    best = 0
    very_best = 0
    best_table = []
    best_resto = []
    last_iter = -1

    gruppi = [23,17,4,6,15,5,11,9,2,8,7,6,9,9,19,4,15,11,9,11,3,24,14,7,2,19,20,11,16,4,13,17,4,14,22,6,4,22,8,6,20,4,6,20,5,23,7,8,20,15, 6, 23,17,4,6,15,5,11,9,2,8,7,6,9,9,19,4,15,11,9,11,3,24,14,7,2,19,20,11,16,4,13,17,4,14,22,6,4,22,8,6,20,4,6,20,5,23,7,8,20,15, 6]

    tav = [7, 28, 28, 28, 56, 56, 21, 28, 28, 28, 56, 56, 56, 56, 56, 21, 14, 28, 28, 56, 56, 21, 28, 28, 56, 56, 56, 56, 56]

    pos = []
    resto = []

    def __init__(self):
        self.tav.sort(reverse=True)
        #i = 0
        #while(i < len(self.gruppi)):
        #    if (self.gruppi[i] < 7):
        #        j = i + 1
        #        while (j < len(self.gruppi)):
        #            if (self.gruppi[i] + self.gruppi[j] == 7):
        #                self.gruppi[i] = 7
        #                self.gruppi.pop(j)
        #                break
        #            j += 1
        #    i += 1

        self.preparaTavoli()

    def persone(self):
        return sum(self.gruppi)
    
    def tavoli(self):
        return sum(self.tav)
    
    def preparaTavoli(self):
        for t in self.tav:
            self.pos.append([t, []])

        for i in self.gruppi:
            l = 0
            loop = True
            while (loop):
                j = 0
                while(j<len(self.tav)):
                    if (self.pos[j][0] > i and len(self.pos[j][1]) == l):
                        self.pos[j][1].append(i)
                        loop = False
                        break
                    j+=1
                l +=1

    def cleaning(self):
        for t in self.pos:
            while (sum(t[1]) > t[0]):
                m = t[1].index(min(t[1]))
                c = t[1][m]
                self.resto.append(c)
                t[1].pop(m)

    def sums(self):
        posti = 0
        gruppi = 0
        for t in self.pos:
            posti += t[0]
            gruppi += sum(t[1])

        return (posti, gruppi, sum(self.resto))

    def score(self):
        sco = 0
        dummy, t1, t2 = self.sums()
        sco = t1 - t2
        for i in self.pos:
            s = sum(i[1])
            diff = s - i[0]
            #if (diff == 1):
            #    sco -= 5
        return sco
                
    def checkScore(self, iteration, thrs=.98):
        t = self.score()
        #print t, self.best
        if (t > self.best and t > self.very_best*thrs):
            self.best_table = self.pos
            self.best_resto = self.resto
            if (iteration > -1):
                self.last_iter = iteration
                self.best = t
                if (t > self.very_best):
                    self.very_best = t
                    self.mutazioni = 22 - int((float(self.very_best)/float(self.persone()))*10)*2
                print "best:[",self.best,"]", self.best_table, self.best_resto, self.sums(), (float(self.very_best)/float(self.persone()))
                if (len(self.best_resto) == 0):
                    print "Convergenza"
                    sys.exit()

    def swapResto(self):
        for r1, r in enumerate(self.resto):
            diff = -1
            t1 = int(random.uniform(0, len(self.pos)))
            self.pos[t1][1].append(self.resto[r1])
            self.resto.pop(r1)

    def mutate(self):
        for i in xrange(self.mutazioni):
            i1 = 0
            t1 = 0
            t2 = 0
            while(t1 == t2):
                t1 = int(random.uniform(0, len(self.pos)))
                t2 = int(random.uniform(0, len(self.pos)))
                i1 = int(random.uniform(0, len(self.pos[t1][1])))

            if (len(self.pos[t1][1]) != 0):
                self.pos[t2][1].append(self.pos[t1][1][i1])
                self.pos[t1][1].pop(i1)
                
    def  assignResto(self):
        for r1, r in enumerate(self.resto):
            diff = -1
            for t1 in xrange(len(self.pos)):
                diff = self.pos[t1][0] - sum(self.pos[t1][1])
                if (diff > self.resto[r1]):
                    self.pos[t1][1].append(self.resto[r1])
                    self.resto.pop(r1)
                    break
    
    def ratio(self):
        return float(self.very_best)/float(self.persone())
        
    def mainLoop(self, iterations=1000000):
        self.checkScore(-1)
        cicli = 0
        for i in xrange(iterations):
            if (i%100000 == 0):
                print i
            if (i%2 == 0):
                self.swapResto()
            else:
                self.mutate()

            self.cleaning()
            self.checkScore(i)
            cicli += 1
        
            if (cicli > 50000):
                self.assignResto()
                self.checkScore(i)
            
            if (self.ratio() > 0.90 and (i - self.last_iter)> 200000):
                sys.exit()


p = pyBrace()
p.mainLoop()
