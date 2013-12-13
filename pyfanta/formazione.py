#! /usr/bin/python
import os, re, sys
import Squadra, IO, Punteggi
import filtra_giocatori

r = re.compile(">([A-Z]+)\s-\s([A-Z]+)<")
r2 = re.compile("id=\"([A-Z]+)\"")
r3 = re.compile("\"([ACD])\">([ACD])<")
r4 = re.compile("\"mv\">(.+)<")


def scaricaProbabiliFormazioni(username, pwd):
    os.system("curl --connect-timeout 15 -s -c cookie -d user="+username+" -d password="+pwd+" -d ricorda=NO http://www.fantagazzetta.com/login.asp > dump")
    # check error somehow    
    os.system("curl -s -b cookie http://www.fantagazzetta.com/probabili_formazioni_serie_a.asp > probform.html")
    os.system("grep intestazione probform.html > formazione.html")
    

scaricaProbabiliFormazioni("matteosan", "fisica")

team = IO.loadSquadra()

partite = {}

file = open("formazione.html")
lines = file.readlines()
for line in lines:
    s = r.search(line)
    if (s):
        partite[s.group(1)] = s.group(2)
        partite[s.group(2)] = s.group(1)
file.close()

medie_totali = {}
for g in xrange(team.giornata-4, team.giornata):
    if (g < 1):
        continue
    if (not os.path.exists("voti_"+str(g)+".html")):
        scaricaPaginaVoti("matteosan", "fisica", g)
    os.system("grep -e \"team\\\" id\" -e \"mv\" -e\">D<\" -e \">A<\" -e \">C<\" voti_"+str(g)+".html > voti_"+str(g)+".txt")

    file = open("voti_"+str(g)+".txt")
    lines = file.readlines()
    medie = {}
    file.close()
    for l in xrange(len(lines)):
        squadra = ""
        ruolo = ""
        media = [[],[],[]]
        if ("team" in lines[l] and "id" in lines[l]):
            s2 = r2.search(lines[l])
            if (s2):
                squadra = s2.group(1)
                l = l+3
                while(1):
                    s3 = r3.search(lines[l+1])
                    if (s3):
                        ruolo = s3.group(2)
                        s41 = r4.search(lines[l+2])
                        s42 = r4.search(lines[l+3])
                        s43 = r4.search(lines[l+4])
                    else:
                        break
                    if (s41 and s42 and s43):
                        m = (float(s41.group(1).replace(",",".").replace("-", "0")) + 
                             float(s42.group(1).replace(",",".").replace("-", "0")) + 
                             float(s43.group(1).replace(",",".").replace("-", "0"))) / 3.
                        if (m != 0):
                            if (ruolo == "D"):
                                media[0].append(m)
                            elif (ruolo == "C"):
                                media[1].append(m)
                            elif (ruolo == "A"):
                                media[2].append(m)
                    l = l + 4
            medie[squadra] = [sum(i)/len(i) for i in media]
    
    for m in medie.keys():    
        if (m in medie_totali.keys()):
            medie_totali[m] = [i+j for i,j in zip(medie[m],medie_totali[m])]
        else:
            medie_totali[m] = medie[m]

for m in medie_totali:
    medie_totali[m] = [i/4. for i in medie_totali[m]] 

# filtra giocatori
inFormazione = [-1 for i in xrange(len(team.giocatori))]
prob = filtra_giocatori.filtra_giocatori()

print prob

for n,i in enumerate(team.giocatori):
    # verificare il nome completo per i duplicati
    for j in prob:
        if (i.cognome == j[0]):
            if (j[1]):
                inFormazione[n] = 2
            else:
                inFormazione[n] = 1

difensori = []
centrocampisti = []
attaccanti = []     
for n,i in enumerate(team.giocatori):
    if (inFormazione[n] == -1):
        print i.cognome
        continue
    if (i.ruolo == 1):
        difensori.append(i)
    if (i.ruolo == 2):
        centrocampisti.append(i)
    if (i.ruolo == 3):
        attaccanti.append(i)

# per la lista di giocatori normalizza 1 per giocate/totali 
# aggiungi lista in base alle quotazioni iniziali

punti = Punteggi.Punteggi()

d_weight = []
c_weight = []
a_weight = []
for i in difensori:
    weight = medie_totali[i.squadra][i.ruolo-1]/medie_totali[partite[i.squadra]][2-i.ruolo];
    d_weight.append(i.mediaUltime4(6, punti)*weight)

for i in centrocampisti:
    weight = medie_totali[i.squadra][i.ruolo-1]/medie_totali[partite[i.squadra]][2-i.ruolo];
    c_weight.append(i.mediaUltime4(6, punti)*weight)

for i in attaccanti:
    weight = medie_totali[i.squadra][i.ruolo-1]/medie_totali[partite[i.squadra]][2-i.ruolo];
    a_weight.append(i.mediaUltime4(6, punti)*weight)

difEd_weight = zip(d_weight, difensori)
difEd_weight.sort(reverse = True)
sortedd_weight, sortedDifensori = zip(*difEd_weight)

centEc_weight = zip(c_weight, centrocampisti)
centEc_weight.sort(reverse = True)
sortedc_weight, sortedCentrocampisti = zip(*centEc_weight)

attEa_weight = zip(a_weight, attaccanti)
attEa_weight.sort(reverse = True)
sorteda_weight, sortedAttaccanti = zip(*attEa_weight)

tot_max = 0
index = 0
for j, i in enumerate(punti.schemi):
    totale = 0
    totale = (sum(sortedd_weight[0:int(i[0])]) + 
              sum(sortedc_weight[0:int(i[1])]) + 
              sum(sorteda_weight[0:int(i[2])]))
    print i, totale
    if (tot_max < totale):
        tot_max = totale
        index = j

print "-------------------"
print "SCHEMA SCELTO: ", punti.schemi[index]
squadra_finale = sortedDifensori[0:int(punti.schemi[index][0])] + sortedCentrocampisti[0:int(punti.schemi[index][1])] + sortedAttaccanti[0:int(punti.schemi[index][2])]

for i in squadra_finale:
    print i.cognome
                                               

# considerare infortuni
# spingere un po' per il prezzo iniziale
# avvantaggiare schemi piu` offensivi
