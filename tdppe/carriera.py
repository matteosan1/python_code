import datetime, random, pickle
import contrada

class carriera:
    def __init__(self):
        self.debug = True
        self.anno = 2014
        self.las = 0 # luglio=0,agosto=1,settembre=2

        # inizializzazione contrade 
        random.seed(1)
        self.luglio = random.sample(xrange(0, 17), 17)
        self.agosto = random.sample(xrange(0, 17), 17)
        self.straordinario = random.sample(xrange(0, 17), 17)
        self.prove = []

        self.status = "non attivo"
        self.giocatori = []

    def salvaStato(self):
        with open("current_setup.pickle", "wb") as handle:
            pickle.dump(self, handle)

    def caricaStato(self):
        with open("current_setup.pickle", "rb") as handle:
            self = pickle.load(handle)

    def assegnaContrada(self):
        pass
    
    def loop(self):
        if (self.status == "non attivo" and not self.debug):
            if (len(self.giocatori) > 0):
                self.status = "attivo"
                return
        else:
            # 0 Lunedi -> 6 Domenica
            weekday = datetime.datetime.today().weekday()
            hour = datetime.datetime.today().hour
            if (self.debug):
                weekday = 0
                hour = 18
            # estrazione
            if (weekday == 0 and hour == 18):
                self.estrazione()
            elif (weekday == 3 and hour == 10):
                self.sceltacavalli()
            elif (weekday == 3 and hour == 13):
                self.assegnazione()
            elif (weekday == 3 and hour == 19):
                self.prova()
            elif (weekday == 4 and hour == 9):
                self.prova()
            elif (weekday == 4 and hour == 19):
                self.prova()
            elif (weekday == 5 and hour == 9):
                self.prova()
            elif (weekday == 5 and hour == 19):
                self.prova()
            elif (weekday == 6 and hour == 9):
                self.prova()
            elif (weekday == 6 and hour == 11):
                self.segnatura()
            elif (weekday == 6 and hour == 19):
                self.palio()
        
    def estrazione(self):
        # estrazione palio straordinario
        if (self.las == 2):
            self.straordinario = random.sample(xrange(0, 17), 17)
    
        # estrazione normale
        if (self.las == 0):
            self.luglio = self.luglio[10:17] + random.sample(self.luglio[0:10], 10)
            self.prove.append([self.luglio[0:10]])
            self.prove.append([self.luglio[10:0]]) 

        if (self.las == 1):
            self.agosto = self.agosto[10:17] + random.sample(self.agosto[0:10], 10)
            self.prove.append([self.agosto[0:10]])
            self.prove.append([self.agosto[10:0]]) 
        
        if (self.debug):
            print self.luglio
        self.salvaStato()

    def assegnazione(self):
        result = []
        orecchio = random.sample(xrange(0, 10), 10)
        contrada = random.sample(xrange(0, 10), 10)
        # ordina le contrade secondo il numero di orecchio capitato
        # FIXME torna ????
        self.prove.append([orecchio[0:10]]) 
        self.prove.append([orecchio[10:0]]) 
        self.prove.append([contrada[0:10]]) 
        self.prove.append([contrada[10:0]]) 
    
        for i in xrange(0, 10):
            result.append([orecchio[i], contrada[i]])
    
        return result

    def prova(self):
        pass

    def segnatura(self):
        pass
    
    def palio(self):
        pass


c = carriera()
c.loop()
