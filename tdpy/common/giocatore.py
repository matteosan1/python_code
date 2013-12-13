from PyQt4.QtCore import QString

class Giocatore:
    def __init__(self):
        self.nome = QString("")
        self.cognome = QString("")
        self.username = QString("")
        self.contrada = -1
        self.tempo_in_carica = 0
        self.score = [0,0]
	self.sta_giocando = False
    
    def __str__(self):
        s = str(self.nome) + " " + str(self.cognome)
        return s

    def corsi(self):
        return score[0]

    def vittorie(self):
        return score[1]

    def inTextStreamer(self, stream):
        t = QString()
        stream >> t
        self.nome = QString(t)
        stream >> t
        self.cognome = QString(t)
        stream >> t
        self.username = QString(t)
        stream >> t
        self.contrada = int(t)
        stream >> t
        self.tempo_in_carica = int(t)
        stream >> t
        self.score[0] = int(t)
        stream >> t
        self.score[1] = int(t)
        stream >> t
        self.sta_giocando = bool(int(t))
        
    def outTextStreamer(self, stream):
        if (self.nome != ""):
            stream << self.nome << "\n"
        else:
            stream << "-\n"
        if (self.cognome != ""):
            stream << self.cognome << " \n"
        else:
            stream << "-\n"
        stream << self.username << "\n"
        stream << self.contrada << "\n"
        stream << self.tempo_in_carica << "\n"
        stream << self.score[0] << "\n"
        stream << self.score[1] << "\n"
        stream << int(self.sta_giocando) << "\n"

    def outStreamer(self, stream):
        stream << QString(self.nome)
        stream << QString(self.cognome)
        stream << QString(self.username)
        stream.writeInt16(self.contrada)
        stream.writeInt16(self.tempo_in_carica)
        stream.writeInt16(self.score[0])
        stream.writeInt16(self.score[1])
        stream.writeInt16(int(self.sta_giocando))

    def inStreamer(self, stream):
        stream >> self.nome
        stream >> self.cognome
        stream >> self.username
        self.contrada = stream.readInt16()
        self.tempo_in_carica = stream.readInt16()
        self.score[0] = stream.readInt16()
        self.score[1] = stream.readInt16()
        self.sta_giocando = bool(stream.readInt16())

