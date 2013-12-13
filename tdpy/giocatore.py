# -*- coding: utf-8 -*-

class Giocatore:
  def __init__(self):
    self.nome = [QString(""), QString(""), QString("")] # QString Nome, Cognome, username;
    self.contrada = int()
    self.tempo_in_carica = 0
    self.score = (0, 0)    # corsi vinti

        #friend QDataStream& operator<<(QDataStream& out, Giocatore x);
        #friend QTextStream& operator<<(QTextStream& out, Giocatore x);
        #friend QDataStream& operator>>(QDataStream& in, Giocatore& x);
        #friend QTextStream& operator>>(QTextStream& in, Giocatore& x);

