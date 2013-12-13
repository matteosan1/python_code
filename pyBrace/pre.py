#! /usr/bin/python
import random
import sys

mutazioni = 20
best = 0
very_best = 0
best_table = []
best_resto = []

def cleaningPhase(d, resto):
    tavoli_finali = []
    a = []
    tav = []
    for i, t in enumerate(d):
        if (t[0] == sum(t[1])):
            tavoli_finali.append(t)
        else:
            tav.append(t[0])
            for g in t[1]:
                a.append(g)

    for i in resto:
        a.append(i)
        
    tav[0] += 7
    tav[1] += 7
        
    return (a, tav, tavoli_finali)

def checkScore(d, resto, best, very_best):
    t = score(d, resto)
    if (t > best and t > very_best*.98):
        best_table = d
        best_resto = resto
        best = t
        if (t > very_best):
            very_best = t
            mutazioni = int((float(very_best)/float(persone))*10)*2
        print "best:[",best,"]", best_table, best_resto, sums(best_table, best_resto)
        print (float(very_best)/float(persone))
        if (len(best_resto) == 0):
            print "Convergenza"
            sys.exit()
        return True
    return False

def main_loop(d, resto):
    best_table = d
    best_resto = resto
    best = score(d, resto)
    very_best = best

    cicli = 0
    for i in xrange(1000000):
        if (i%100000 == 0):
            print i
        if (i%2 == 0):
            d, resto = swapResto(d, resto)
        else:
            d, resto = swap(d, resto)
        d, resto = cleaning(d, resto)
        
        if (not checkScore(d, resto, best, very_best)):
            cicli += 1
            d = best_table
            resto = best_resto
        
        if (cicli > 50000 or ((float(very_best)/float(persone)) > 0.90) or len(best_resto) < 5):
            d, resto = assignResto(best_table, best_resto)
            checkScore(d, resto, best, very_best)

    return (best_table, best_resto)
    
def init(tav, a):
    d = []
    for t in tav:
        d.append([t, []])

    for i in a:
        turno = 0
        loop = True
        while (loop):
            j = 0
            while(j<len(tav)):
                if (d[j][0] > i and len(d[j][1]) == turno):
                    d[j][1].append(i)
                    loop = False
                    break
                j+=1
            turno +=1

    return d

def sums(tav, resto):
    posti = 0
    gruppi = 0
    for t in tav:
        posti += t[0]
        gruppi += sum(t[1])

    return (posti, gruppi, sum(resto))

def cleaning(tav, resto):
    for t in tav:
        while (sum(t[1]) > t[0]):
            m = t[1].index(min(t[1]))
            c = t[1][m]
            resto.append(c)
            t[1].pop(m)

    return (tav, resto)

def swapResto(tav, resto):
    for r1, r in enumerate(resto):
        diff = -1
        t1 = int(random.uniform(0, len(tav)))
        tav[t1][1].append(resto[r1])
        resto.pop(r1)
    return (tav, resto)

def assignResto(tav, resto):
    for r1, r in enumerate(resto):
        diff = -1
        for t1 in xrange(len(tav)):
            diff = tav[t1][0] - sum(tav[t1][1])
            if (diff > resto[r1]):
                tav[t1][1].append(resto[r1])
                resto.pop(r1)
                break
    return (tav, resto)

def swap(b, resto):
    for i in xrange(mutazioni):
        i1 = 0
        t1 = 0
        t2 = 0
        while(t1 == t2):
            t1 = int(random.uniform(0, len(b)))
            t2 = int(random.uniform(0, len(b)))
            i1 = int(random.uniform(0, len(b[t1][1])))

        if (len(b[t1][1]) != 0):
            b[t2][1].append(b[t1][1][i1])
            b[t1][1].pop(i1)
        
    return b, resto

def score(d, resto):
    sco = 0
    dummy, t1, t2 = sums(d, resto)
    sco = t1 - t2
    for i in d:
        s = sum(i[1])
        diff = s - i[0]
        #if (diff == 1):
        #    sco -= 5

    return sco

a = [23,17,4,6,15,5,11,9,2,8,7,6,9,9,19,4,15,11,9,11,3,24,14,7,2,19,20,11,16,4,13,17,4,14,22,6,4,22,8,6,20,4,6,20,5,23,7,8,20,15, 6]
#, 23,17,4,6,15,5,11,9,2,8,7,6,9,9,19,4,15,11,9,11,3,24,14,7,2,19,20,11,16,4,13,17,4,14,22,6,4,22,8,6,20,4,6,20,5,23,7,8,20,15, 6]

persone = sum(a)
print "PERSONE: ", persone

tav = [7, 14, 14, 28, 28, 56, 56, 7, 14, 14, 14, 28, 28, 56, 56, 56, 56, 56]
#, 7, 14, 14, 28, 28, 56, 56, 7, 14, 28, 28, 56, 56, 56, 56, 56]
tav.sort(reverse=True)

print "TAVOLI:  ", sum(tav)


for cycles in xrange(3): 
    d = init(tav, a)
    d,resto = cleaning(d, [])



    best_table, best_resto = main_loop(d, resto)

    print "Another phase is needed"
    mutazioni = 20
    a, tav, tavoli_finali = cleaningPhase(best_table, best_resto)
    print tavoli_finali

print "[best] ", best_table, best_resto, sums(best_table, best_resto)
print tavoli_finali

