#! /usr/bin/python
import re, os, sys
import Squadra, Giocatore, Punteggi
import IO

s = IO.loadSquadra()

g = Giocatore.Giocatore()
g.cognome = "BUDAN"
g.nome = "IGOR"
g.ruolo = 3
g.squadra = "CESENA"
g.prezzo = 4

#aggiorna tutti i voti fino alla giornata corrente
for i in xrange(s.giornata+1):
    g.prestazioni.append([0,[0,0],0,0,0,0,0,0])

s.addGiocatore(g)
IO.saveSquadra(s)
