import math
import ROOT

def combinazione(n, i):
    result = fattoriale(n)/(fattoriale(n-i)*fattoriale(i));
    return result 

def fattoriale(x):
    if (x<2):
        return 1

    result = 1
    for i in xrange(1, x+1):
        result = result*i    
    return result    

grado_curva = 243;
numero_punti = 340;

punti = []  
fi = open("piazza.dat");
while True:
    line = fi.readline()
    if not line:
        break
    converted = [float(line.split("  ")[0]), float(line.split("  ")[1])]
    punti.append(converted)

spread = 1.0/numero_punti;
x = []  
y = []

old_b = [0,0]
output = open("tdp_geometry.dat", "w")
output.write("x y ang rows best\n")

for j in xrange(numero_punti+1):
    t = spread*j
    b = [0, 0]
    for i in xrange(0, grado_curva+1):
        comb = combinazione(grado_curva, i)  
        pow1 = pow(t,i);
        pow2 = pow((1-t), (grado_curva-i));
        b[0] = b[0] + comb*punti[i][0]*pow1*pow2;
        b[1] = b[1] + comb*punti[i][1]*pow1*pow2;
   
    angle = 0    
    if (old_b != [0, 0]):
        angle = math.atan2((b[1]-old_b[1]), (b[0]-old_b[0]))
    old_b = b
    output.write("%.2f %.2f %f 6 -1\n" %(b[0], b[1], angle))

output.close()

c = ROOT.TCanvas("c", "c")
h = ROOT.TH2F("h2", "h2", 1146, 0, 1146, 956, 0, 956)
g = ROOT.TGraph("tdp_geometry.dat")
h.Draw()
g.Draw("SAME") 
c.SaveAs("piazza.png")
c.SaveAs("piazza.root")
