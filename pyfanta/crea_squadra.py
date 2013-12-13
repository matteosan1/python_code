#! /usr/bin/python
import re, os, sys
import Squadra, Giocatore, Punteggi
import IO

s = Squadra.Squadra()
s.nome = "Black Hole Thoiry"
s.anno = "2011-2012"

prezzo = [11, 1, 3, 3, 8, 11, 1, 3, 7, 6, 16, 6, 3, 24, 3, 16, 3, 12, 16, 12, 29, 26, 31]
nome = ["SEBASTIEN", "CRISTIANO", "CESARE", "NICOLO", "KAKHABER", "CRISTIAN", "CICERO JOAO", "NICHOLAS", "DANIELE", "STEVE", "MILOS", "FRANCESCO", "EMMANUEL AGYEMANG", "MAREK", "PAOLO", "ESTEBAN", "CHRISTIAN", "VALTER", "DAVID", "SIMONE", "ALESSANDRO", "GASTON", "ALEXANDRE"]
ruolo = [0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3]
giocatori =["FREY", "LUPATELLI", "NATALI", "CHERUBIN", "KALADZE", "ZACCARDO", "CICINHO", "FREY", "PORTANOVA", "VON BERGEN", "KRASIC", "VALIANI", "BADU", "HAMSIK", "GROSSI", "CAMBIASSO", "OBODO", "BIRSA", "DI MICHELE", "TIRIBOCCHI", "MATRI", "MAXI LOPEZ", "PATO"]
squ = ["GENOA", "GENOA", "FIORENTINA", "SIENA", "GENOA", "PARMA", "ROMA", "CHIEVO", "BOLOGNA", "CESENA", "JUVENTUS", "PARMA", "UDINESE", "NAPOLI", "SIENA", "INTER", "LECCE", "GENOA", "LECCE", "ATALANTA", "JUVENTUS", "CATANIA", "MILAN"]

for j,i in enumerate(giocatori):
    g = Giocatore.Giocatore()
    g.cognome = giocatori[j]
    g.indice = j
    g.nome = nome[j]
    g.ruolo = ruolo[j]
    g.squadra = squ[j]
    g.prezzo = prezzo[j]
    s.addGiocatore(g)

IO.saveSquadra(s)
