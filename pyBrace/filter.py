import sys, copy
import partitions
import combinations

tavoli = [10, 40, 40, 20, 20, 20]
#prenotazioni = [35, 30, 21, 20, 18, 10, 8, 7, 6, 4, 3, 1]
prenotazioni = [4, 3, 2]
antiprenotazioni = []

print "Definizione tavoli/prenotazioni"

# xrange come il tavolo piu` capiente (considerare 1)
for i in xrange(2, 11):
    if (i not in prenotazioni):
        antiprenotazioni.append(i)

print "Check"

ospiti = 0
for i in prenotazioni:
    ospiti += i

posti = 0
for i in tavoli:
    posti += i

#deve controllare che i primi (tavoli) prenotazioni sono minori del numero 
#di posti per tavolo
if (ospiti > posti):
    print "Troppi ospiti"
    sys.exit(1)

print "Filtri tavoli"

parts = []

uni = posti - posti + prenotazioni.count(1)

for i in xrange(0,1):
    part = list(partitions.partitions(tavoli[i]))
    print part
    print len(part)
    for n in xrange(len(part)-1, -1, -1):
        for j in xrange(2, 11):
            if (j not in antiprenotazioni):
                ripetizioni = prenotazioni.count(j) 
                print ripetizioni, part[n].count(j)
                if (part[n].count(j) <= ripetizioni):
                    part.pop(n)
                    break

    print len(part)
            

                    
                    
#    for n, j  in enumerate(part):
#        if (j.count(1) > uni):
#            part.pop(n)
#
#    # filtra le partizioni
#    for j in antiprenotazioni:
#        for n in xrange(len(part)-1, -1, -1):
#            if (j in part[n]):
#                part.pop(n)
#                
    #print len(part)
    parts.append(part)
    print part

sys.exit(1)
G = combinations.GenerateCombinations(parts)

print "Combinazioni"
best_rate = 10000
for each in G:
    temp_each = copy.deepcopy(each)

    # mergia liste
    merged = []
    for i in temp_each:
        for j in i:
            merged.append(j)
    
    # filtra selezioni finali
    # prima guarda che ci siano le giuste prenotazioni
    rating = 0
    for i in prenotazioni:
        if (i == 1):
            continue

        volte1 = prenotazioni.count(i)
        volte2 = merged.count(i)

        if (volte1 != volte2):
            rating = 10000
            break
    
    if (rating != 10000):
        # poi calcola il minimizzatore
        for j in prenotazioni:
            if (j == 1):
                continue
            for i in temp_each:
                if (j in i):
                    i.remove(j)
                    break

        for i in temp_each:
            if (len(i) > 0):
                rating += 100
            for j in i:
                rating += j

    if (rating < best_rate):
        best_rate = rating
        print each, best_rate

    
