#! /usr/bin/python
import re

def filtra_giocatori():
    r = re.compile("<div class=\"[sd]x\">([A-Z]+)</div>")

    file = open("probform.html")
    lines = file.readlines()
    file.close()
    
    formazione = []
    
    panchina = False
    for line in lines:
        if ("panchinasx" in line or "panchinadx" in line):
            panchina = True
        if ("team" in line):
            panchina = False
        s = r.search(line)
        if (s):
            formazione.append((s.group(1), panchina))

    return formazione
