from operator import itemgetter

def ruota(teams):
    for i in xrange(0, len(teams)-1):
        rotation = [teams[0]] + [teams[-1]] + teams[1:-1]
    return rotation

teams = ["=N"+str(i) for i in xrange(0, 6)]

giornate = dict()
# to be fixed for odd number of teams
matches = len(teams)-1
for m in xrange(1, matches+1):
    giornate[m] = []
    teams = ruota(teams)
    for i in xrange(len(teams)/2):
        if (m%2 == 0):
            giornate[m].append((teams[i], teams[len(teams)-1-i]))
        else:
            giornate[m].append((teams[len(teams)-1-i], teams[i]))
        
for g in giornate:
    ng = g
    #print "Giornata: ", ng
    giornate[g] = sorted(giornate[g], key=itemgetter(0))
    for i,m in enumerate(giornate[g]):
        #str1 = "=if(Giornata%d!F%d>65,if(Giornata%d!F%d<97,int(((Giornata%d!F%d-66)/6)+1),6),0)"%(ng, (i*22)+23,ng, (i*22)+23,ng, (i*22)+23)
        #str2 = "=if(Giornata%d!M%d>65,if(Giornata%d!M%d<97,int(((Giornata%d!M%d-66)/6)+1),6),0)"%(ng, (i*22)+23,ng, (i*22)+23,ng, (i*22)+23)
        str1 = "=Giornata%d!F%d"%(ng, (i*22)+91)
        str2 = "=Giornata%d!M%d"%(ng, (i*22)+91)
        print "%s %s"%(str1, str2)
        #print "%s - %s %s %s"%(m[0], m[1], str1, str2)
    print

for g in giornate:
    ng = g+len(giornate)
    #print "Giornata: ", ng
    giornate[g] = sorted(giornate[g], key=itemgetter(0))
    for i,m in enumerate(giornate[g]):
        #str1 = "=if(Giornata%d!F%d>65,if(Giornata%d!F%d<97,int(((Giornata%d!F%d-66)/6)+1),6),0)"%(ng, (i*22)+23,ng, (i*22)+23,ng, (i*22)+23)
        #str2 = "=if(Giornata%d!M%d>65,if(Giornata%d!M%d<97,int(((Giornata%d!M%d-66)/6)+1),6),0)"%(ng, (i*22)+23,ng, (i*22)+23,ng, (i*22)+23)
        str1 = "=Giornata%d!F%d"%(ng, (i*22)+91)
        str2 = "=Giornata%d!M%d"%(ng, (i*22)+91)
        print "%s %s"%(str1, str2)
        #str1 = "=if(Giornata%d!C%d>65,int(((Giornata%d!C%d-65)/3)+1),0)"%(ng, (i+1)*19,ng, (i+1)*19)
        #str2 = "=if(Giornata%d!G%d>65,int(((Giornata%d!G%d-65)/3)+1),0)"%(ng, (i+1)*19,ng, (i+1)*19)
        #print "%s - %s %s %s"%(m[0], m[1], str1, str2)
    print

for g in giornate:
    ng = g+2*len(giornate)
    #print "Giornata: ", ng
    giornate[g] = sorted(giornate[g], key=itemgetter(1))
    for i,m in enumerate(giornate[g]):
        #str1 = "=if(Giornata%d!F%d>65,if(Giornata%d!F%d<97,int(((Giornata%d!F%d-66)/6)+1),6),0)"%(ng, (i*22)+23,ng, (i*22)+23,ng, (i*22)+23)
        #str2 = "=if(Giornata%d!M%d>65,if(Giornata%d!M%d<97,int(((Giornata%d!M%d-66)/6)+1),6),0)"%(ng, (i*22)+23,ng, (i*22)+23,ng, (i*22)+23)
        str1 = "=Giornata%d!F%d"%(ng, (i*22)+91)
        str2 = "=Giornata%d!M%d"%(ng, (i*22)+91)
        print "%s %s"%(str1, str2)
        #str1 = "=if(Giornata%d!C%d>65,int(((Giornata%d!C%d-65)/3)+1),0)"%(ng, (i+1)*19,ng, (i+1)*19)
        #str2 = "=if(Giornata%d!G%d>65,int(((Giornata%d!G%d-65)/3)+1),0)"%(ng, (i+1)*19,ng, (i+1)*19)
        #print "%s - %s %s %s"%(m[0], m[1], str1, str2)
    print



