import math, sys

L = 300 # longitudinal length in m 
Delta = 400 # height in m
q = 8 # weight/mt in Kg
Ta = 16000

Ya = Ta/q
Phia = math.atan(Delta/L-L/(2*Ya))

while(1):
    h = Ya*math.cos(Phia)
    print h
    Phib = math.atan(math.sinh(L/h + math.asinh(math.tan(Phia))))
    print Phib

    Yb = h/math.cos(Phib)
    print math.cos(Phib)
    print Yb, Ya
    sys.exit()
    if ((Yb - Ya - Delta) < 0.001):
        S = h*(math.tan(Phib)-math.tan(Phia))
        Tb = Yb*q

        Yx = h*math.cosh(x/h+math.asinh(math.tan(Phia)))-Ya
        fx = x*Delta/L-Ya
        break

    

