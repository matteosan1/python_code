from PyQt4 import QtGui, QtCore 
from math import *

class MyLabel(QtGui.QLabel):
    def __init__(self):
        QtGui.QLabel.__init__(self)

    def mouseReleaseEvent(self, event):
        self.offset = 0.15707963267948966
        self.x = event.posF().x() - 190
        self.y = -(event.posF().y() - 200)
        self.r2 = (pow(self.x, 2) + pow(self.y, 2))
        self.r = sqrt(self.r2)
        self.cos_phi2 = self.r2 - pow(self.y,2)
        print self.cos_phi2
        self.phi = acos(sqrt(self.cos_phi2)/self.r)
        if (self.y < 0 and self.x < 0):
            self.phi += pi
        if (self.y > 0 and self.x < 0):
            self.phi = pi - self.phi
        if (self.y < 0 and self.x > 0):
            self.phi = 2*pi - self.phi

        self.phi += self.offset
        if (self.phi > 2*pi):
            self.phi -= 2*pi

        print self.r, self.phi
        
    def points(self, radius, phi):
        self.offset = 0.15707963267948966*2
        self.p = (1,2,3,4,5,6,7,8
                  9,10,11,12,13,14,15,16,17,18,19,20)
        
        self.r = (5, 10, 100, 120, 200, 220)

        if radius < self.r[0]:
            return 50

        if radius < self.r[1] and radius > self.r[0]:
            return 25

        self.punteggio = self.p[int(phi/self.offset)]

        if radius < self.r[3] and radius > self.r[2]:
            self.punteggio *= 3

        if radius < self.r[5] and radius > self.r[4]:
            self.punteggio *= 2
            
        return self.punteggio
