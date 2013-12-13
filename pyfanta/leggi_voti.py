#! /usr/bin/python
import re, os, sys
import Squadra, Giocatore, Punteggi
import IO
#               0          1        2         3         4             5              6              7      8
#giocatori =["BUFFON", "STORARI", "LUCIO", "CORDOBA", "RANOCCHIA", "PORTANOVA", "DE SILVESTRI", "GRAVA", "PERICO",
#     9           10       11       12          13      14        15      16           17       18       19   
# "VON BERGEN", "CONTI", "EKDAL", "GUBERTI", "HAMSIK", "KONE", "MENEZ", "PASTORE", "SISSOKO", "ETO'O", "IGHALO", 
#    20        21        22      23
#"KUTUZOV", "LAVEZZI", "PATO", "BUDAN"]

giornataDaScaricare = 21
s = IO.loadSquadra()

s.giornata = 21

# chiedi se scaricare o no
# protezione se non ho tutte le riserve
#if (os.path.exists("voti_"+str(g)+".html")):    
IO.scaricaPagina("matteosan", "fisica", giornataDaScaricare)
tags = IO.votiPerGiocatore(giornataDaScaricare)

print tags
sys.exit(0)

formazione = [0, 9, 3, 2, 10, 16, 15, 12, 21, 22, 18, 6, 5, 11, 14, 20, 23]
#formazione19 = [1, 2, 3, 5, 10, 15, 13, 16, 21, 22, 18, 9, 4, 12, 11, 20, -1]
#18formazione = [1, 2, 7, 5, 10, 13, 12, 16, 15, 22, 21, 3, 9, 11, 17, 20, -1]
#17formazione = [1, 2, 4, 5, 8, 10, 13, 12, 16, 15, 18, 9, 7, 14, 11, 20, -1]
#16formazione = [1, 2, 8, 4, 9, 10, 13, 12, 16, 15, 18, 3, 6, 14, 11, 21, 19]
#15formazione = [1, 9, 4, 6, 2, 13, 14, 10, 15, 16, 21, 3, 7, 12, 11, 19, -1]
#14formazione = [1, 9, 4, 3, 2, 13, 16, 10, 15, 12, 21, 8, 6, 11, 17, 19, 19]
#13formazione = [1, 5, 2, 4, 13, 16, 10, 14, 12, 18, 21, 3, 9, 15, 11, 20, 19]
#12formazione = [1, 5, 2, 4, 13, 15, 10, 11, 12, 18, 21, 3, 9, 16, 17, 20, 19]
#11formazione = [1, 5, 2, 4, 16, 10, 13, 12, 18, 22, 21, 3, 9, 17, 15, 20, 19]
#10formazione = [1, 5, 2, 4, 16, 15, 13, 12, 18, 22, 21, 9, 8, 10, 11, 20, 19]
#1formazione = [1, 4, 5, 9, 16, 10, 12, 11, 18, 22, 20, 9, 2, 14, 13, 19, 21]
#2formazione = [1, 6, 2, 4, 13, 16, 15, 12, 22, 18, 21, 5, 7, 10, 17, 20, 19]
#3formazione = [1, 6, 2, 4, 5, 13, 16, 15, 21, 18, 20, 9, 7, 17, 14, 19, 22]
#4formazione = [1, 6, 2, 4, 7, 13, 16, 12, 21, 18, 20, 5,9, 15, 14, 19, 22]
#5formazione = [1, 2, 4, 5, 9, 13, 16, 15, 21, 18, 20, 6, 3, 17, 12, 19, 22]
#6formazione = [0, 1, 3, 5, 8,15,12,14,17,19,20,4,8,13,14,18,-1]
#7formazione = [1, 2, 4, 5, 9, 13, 16, 15, 21, 18, 20, 6, 3, 17, 12, 19, 22]
#8formazione = [1, 2, 6, 4, 16, 13, 14, 12, 18, 22, 21, 5, 9, 11, 17, 20, 19]
#9formazione = [1, 5, 2, 4, 16, 11, 13, 12, 18, 22, 21, 8, 6, 14, 17, 20, 19]

print "FORMAZIONE"
for i in formazione[0:11]:
    print s.giocatori[i].cognome
print "--------------"
for i in formazione[11:]:
    print s.giocatori[i].cognome

s.addFormazione(formazione, giornataDaScaricare)
s.calcoloPrestazione(tags, giornataDaScaricare)

(formazione, panchina, totale) = s.totale(giornataDaScaricare)

print "\nFORMAZIONE FINALE"
for i in formazione:
    print s.giocatori[i[0]].cognome, i[1]

print "TOTALE:", totale

#IO.saveSquadra(s)
