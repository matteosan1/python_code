#! /usr/bin/python

import re

def votiPerGiocatore_2011_12(g):
    r1 = re.compile("\"v(amm|esp)?\">(.+)<")
    r2 = re.compile("\"v(amm|esp)?\">(.+)")

    file = open("voti_"+str(g)+".html")
    lines = file.readlines()
    file.close()

    tags = {}
    leggi = 10
    bonus = 0
    voto = []
    nome = ""
    amm = ""

    for l in lines:
        subline = l.split("</")
        for s in subline:
            if ("class=\"P\"" in s):
                ruolo = s[-1]
                if (ruolo == "A" or ruolo == "C" or ruolo == "D" or ruolo == "P"):
                    voto = []
                    bonus = 0
                    leggi = 0
                    if (ruolo == "A"):
                        voto.append(3)
                    if (ruolo == "P"):
                        voto.append(0)
                    if (ruolo == "D"):
                        voto.append(1)
                    if (ruolo == "C"):
                        voto.append(2)
    
            if ("class=\"n\"" in s):
                nome = s.split(">")[-1]
 
            if ("class=\"v" in s or "class=\"u" in s):
                leggi += 1
                if (leggi == 1):
                    v1 = r1.search(s)
                    v2 = r2.search(s)             
                    if (v1):
                        v = v1.group(2)
                        amm = v1.group(1)
                    elif (v2):
                        v = v2.group(2)
                        amm = v2.group(1)
                    else:
                        v = "0"
                        amm = ""

                    if ("class=\"u" in s and ruolo == "P"):
                        v = "6"
    
                    if ("," in v):
                        v = v.replace(",", ".")
    
                    if (amm == "amm"):
                        voto.append([float(v), 1])
                    elif (amm == "esp"):
                        voto.append([float(v), 2])
                    else:
                        voto.append([float(v), 0])
    
            if ("class=\"b" in s and leggi == 1):
                if (bonus < 6):
                    if (s[-1] != "-"):
                        voto.append(float(s[-1]))
                    else:
                        voto.append(0)
                    if (bonus == 5):
                        tags[nome.upper()] = voto
                bonus += 1

    return tags
