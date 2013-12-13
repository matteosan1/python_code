#! /usr/bin/python
import os, pickle, re

def loadSquadra(nome="squadra.txt"):
    return pickle.load(open(nome))
    
def saveSquadra(s, nome="squadra.txt"):
    pickle.dump(s, open(nome, 'w'))

def scaricaPagina(username, pwd, giornata, checkDownload=False):
    if (checkDownload and os.path.exists("./voti_"+str(giornata)+".hmtl")):
        return (0,0)

    out1 = os.system("curl --connect-timeout 15 -s -c cookie -d UserName="+username+" -d Password="+pwd+" -d ricorda=NO http://www.fantagazzetta.com/login.asp > dump")

    # check error somehow 
    #print "curl -s -b cookie http://www.fantagazzetta.com/voti_fantagazzetta_serie_a.asp?g="+str(giornata)+"&p=2 > voti_"+str(giornata)+".html"
    # Versione 2010-11
    #out2 = os.system("curl -s -b cookie \"http://www.fantagazzetta.com/voti_fantagazzetta_serie_a.asp?g="+str(giornata)+"&p=2\" > voti_"+str(giornata)+".html")

    # Versione 2011-12
    out2 = os.system("curl -s -b cookies.txt \"http://www.fantagazzetta.com/voti-fantagazzetta-serie-A-"+str(giornata)+"-giornata \" > voti_"+str(giornata)+".html")
    return (out1, out2)

def convertiTag(tag):
    if ("-" in tag):
        return 0
    elif ("," in tag):
        return float(tag.replace(",","."))
    else:
        return float(tag)

def analizzaTag(tag, index, amm):
    if (index == 1):
        #print "RUOLO: ", tag
        if (tag == "A"):
            return 3
        if (tag == "P"):
            return 0
        if (tag == "D"):
            return 1
        if (tag == "C"):
            return 2
    elif (index == 2):
        #print "NOME: ", tag.split("&")[0]
        return  tag.split("&")[0]
    elif (index == 3):
        #print "VOTO: ",  convertiTag(tag)
        tag = tag.split("<")[0]
        if (tag == "&nbsp;"):
            return float(0)
        #if ("," in tag):
        #    tag = tag[0:-1]
        return [convertiTag(tag), amm]
    elif (index == 4):
        #print "Goal Fatti: ",  convertiTag(tag)
        return convertiTag(tag)
    elif (index == 5):
        #print "Goal Rigori: ",  convertiTag(tag)
        return convertiTag(tag)
    elif (index == 6):
        #print "Goal Subiti: ",  convertiTag(tag)
        return convertiTag(tag)
    elif (index == 7):
        #print "Rigori Parati: ",  convertiTag(tag)
        return convertiTag(tag)
    elif (index == 8):
        #print "Rigori Sbagliati: ",  convertiTag(tag)
        return convertiTag(tag)
    elif (index == 9):
        #print "Autogoal: ",  convertiTag(tag)
        return convertiTag(tag)


def votiPerGiocatore(g):
    r = re.compile("\"([a-zA-Z]+)\">(.+)<")
    tags = {}
    file = open("voti_"+str(g)+".html")
    lines = file.readlines()
    file.close()
    lines = lines.split(">")
    print lines
    for line in range(len(lines)):
        if ("team" in lines[line]):
            j = line
            tag = []
            temp_ruolo = ""
            for i in range(j, j+10):
                m = r.search(lines[i])
                if (m):
                    if (m.group(2) == "P"):
                        temp_ruolo = "P"
                    if ((i == (line+1)) and (m.group(2) != "A") and (m.group(2) != "P") and (m.group(2) != "C") and (m.group(2) != "D")):
                        break

                    amm = -1
                    if ("votoverdee" in lines[i]):
                        amm = 2
                    elif ("votoverdea" in lines[i]):
                        amm = 1
                    else:
                        amm = 0

                    # FIXME with regolamento per il sei politico
                    if (m.group(1) == "grigio" and temp_ruolo != "P"):
                        tag.append(analizzaTag("0", i-j, amm))
                    else:
                        tag.append(analizzaTag(m.group(2), i-j, amm))
                elif (i == (line+1)):
                    break
            line = line + 10
            if (len(tag) > 1):
                tags[tag[1]] = [tag[0]]+tag[2:]
    print tags
    return tags
