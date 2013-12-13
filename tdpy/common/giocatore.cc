#include "giocatore.h"

// FIXME prevedi giocatori con nomi o cognomi con spazi

Giocatore::Giocatore() {
    Nome = "";
    Cognome = "";
    Contrada = -1;
    Tempo_in_carica = 0;
    Score[0] = 0;
    Score[1] = 0;
    sta_giocando = false;	
}

Giocatore::~Giocatore()
{}

QDataStream& operator<<(QDataStream& out, Giocatore x) {

  out << x.username;	
  out << x.Nome; 
  out << x.Cognome;
  out << x.Contrada;
  out << x.Tempo_in_carica;
  out << x.sta_giocando;

  for(int i=0; i<2; i++)
    out << x.Score[i];

  return out;
}

QTextStream& operator<<(QTextStream& out, Giocatore x) {

  out << x.username << " ";	
  out << x.Nome << " "; 
  out << x.Cognome << " ";
  out << x.Contrada << " ";
  out << x.Tempo_in_carica << " ";

  for(int i=0; i<2; i++)
    out << x.Score[i] << " ";
  out << "\n";

  return out;
}

QDataStream& operator>>(QDataStream& in, Giocatore& x) {

  in >> x.username;
  in >> x.Nome;
  in >> x.Cognome;
  in >> x.Contrada;
  in >> x.Tempo_in_carica;
  in >> x.sta_giocando;

  for(int i=0; i<2; i++)
    in >> x.Score[i];
  
  return in;
}

QTextStream& operator>>(QTextStream& in, Giocatore& x) {

  in >> x.username;
  in >> x.Nome;
  in >> x.Cognome;
  in >> x.Contrada;
  in >> x.Tempo_in_carica;
  
  for(int i=0; i<2; i++)
    in >> x.Score[i];
  
  return in;
}
