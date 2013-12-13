#! /usr/bin/python

class Punteggi:
    def __init__(self):
        self.n_portieri, self.n_difensori, self.n_centrocampisti, self.n_attaccanti = 1,8,8,5
        self.auto_portiere, self.sv_portiere, self.sei_politico = 1,1,1
        self.reti = [66, 72, 78, 84, 92, 100, 106, 112, 118, 124]
        self.schemi = ["631", "541", "532", "451", "442", "433", "361", "352", "343"]
        self.gsu, self.rp, self.rsb, self.gse, self.ass, self.am, self.es, self.rse, self.au = -1, 3, -3, 3, 0, -0.5, -1, 2, -2
