#ifndef GIOCATORE_H
#define GIOCATORE_H

#include <QString>
#include <QTextStream>
#include <QDataStream>

using namespace std;
//FIXME da ogni classe "base" togliere namespace std;
class Giocatore
{
    public:
        Giocatore();
        virtual ~Giocatore();
	
	void setUsername(QString n) { username = n; };
        void setNome(QString n) { Nome = n; };
        void setCognome(QString n) { Cognome = n; };
        void setContrada(int a) { Contrada = a; };
	void setGioca() { sta_giocando = true; };

	QString userName() { return username; };
        QString nome() { return Nome; };
        QString cognome() { return Cognome; };
        QString nomeCompleto() { return Nome + " " + Cognome; };

	bool gioca() { return sta_giocando; };
        int contrada() { return Contrada; };
        int tempo() { return Tempo_in_carica; };
        int corsi() { return Score[0]; };
        int vittorie() { return Score[1]; };

        friend QDataStream& operator<<(QDataStream& out, Giocatore x);
        friend QTextStream& operator<<(QTextStream& out, Giocatore x);
        friend QDataStream& operator>>(QDataStream& in, Giocatore& x);
        friend QTextStream& operator>>(QTextStream& in, Giocatore& x);

    private:
        QString Nome, Cognome, username;
        int Contrada;
        int Tempo_in_carica;
        int Score[2];
	bool sta_giocando;
};
#endif
