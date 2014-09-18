import ROOT
import math

def module(v1):
    return math.sqrt(v1[0]*v1[0]+v1[1]*v1[1])

field = ROOT.TH2F("f", "f", 700, -35, 35, 500, 0, 50)

p1 = (-4., 0.)
p2 = (3., 0.)

vals = []
for x in xrange(0, 1400):
    for y in xrange(0, 1000):
        g = (round(float(x-700.)/20., 2), round(float(y)/20.,2))
        #print g
        cosTheta = -1
        if (g[0] > -20 and g[0]<20. and g[1] < 16.5):
            cosTheta = 0
        else:
            v1 = (g[0]-p1[0], g[1]-p1[1])
            v2 = (g[0]-p2[0], g[1]-p2[1])
            #print v1, v2
            mod1 = module(v1)
            mod2 = module(v2)
            if (mod1 == 0 or mod2 == 0):
                cosTheta = 0
            else:
                cosTheta = math.acos((v1[0]*v2[0]+v1[1]*v2[1])/(mod1*mod2))
        vals.append(cosTheta)
        bin = field.FindBin(g[0], g[1])
        field.SetBinContent(bin, cosTheta)
        
#field.GetZaxis().SetRangeUser(0, 3.14)
field.Draw("COLZ")
raw_input()

#16.50x40
