#! /usr/bin/python
import re, os, sys
import Squadra, Giocatore, Punteggi
import IO

s = IO.loadSquadra()

g = "BUDAN"

for i in s.giocatori:
    if (i.cognome == g):
        #i.prestazioni = []
        #for j in xrange(s.giornata+1):
        #    i.prestazioni.append([0,[0,0],0,0,0,0,0,0])
        i.ruolo = i.ruolo + 10

IO.saveSquadra(s)
