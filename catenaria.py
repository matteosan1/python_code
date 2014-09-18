import ROOT
import math, array,numpy
import sys

points = 100
l = 2.
h = 5.
a = 5.5778
cableL = 15
g = 800
H = 100

# beta  = 4.0609
# alpha = sh-1(0.3499) = 0.3431
# 2.800

197./800*(
1.059-1194.58




def asymCatenary():
    global y, z1, z2
    a = ((z1+z2)*(y*y-(z1-z2)*(z1-z2))-2*y*math.sqrt(z1*z2*(y*y-(z1-z2)*(z1-z2))))/(2*(z1-z2)*(z1-z2))
    
    y1 = math.sqrt(z1*z1+2*z1*a)
    y2 = math.sqrt(z2*z2+2*z2*a)
    print y1, y2, z1, z2
    x1 = a*math.log((z1+y1+a)/a)
    x2 = a*math.log((z2+y2+a)/a)
    
    return (a, x1, x2)

def catenary(x, H):
    global g, h
    y = (H/g)*(math.cosh((g/H)*x)-1)
    return y

def catenary2(x, a):
    y = a*(math.cosh(x/a)-1)
    return y

def beta(H):
    global g, l
    return (g*l)/(2*H)

def alpha(H):
    global h, l
    return math.asinh(beta(H)*(h/l)*(1/math.sinh(beta(H))))

def L(H):
    global g
    return 2*H/g*math.sinh(beta(H))*math.cosh(alpha(H)-beta(H))

def minuitFunction(nDim, gout, result, par, flg):
    global g, l
    result[0] = math.pow(L(par[0]) - cableL, 2)

def findMinimum():
    minimizer = ROOT.TFitter(1)
    minimizer.SetFCN(minuitFunction)
    minimizer.SetParameter(0, "H", H, 10., 0, 1e8)
    #minimizer.ExecuteCommand("SIMPLEX",  numpy.array(xrange(8), dtype=float) , 0)
    minimizer.ExecuteCommand("MIGRAD", numpy.array(xrange(8), dtype=float) , 0)
    params = array.array('f', [0,0])
    return minimizer.GetParameter(0)# params[0], params[1])

H = findMinimum()
print L(H), H

#(a,x1, x2) = asymCatenary()

#print x1, x2
x = array.array('f', [])
y = array.array('f', [])

#a = a + 1
for i in xrange(points):
    #x.append((x1+x2)/float(points)*float(i)-x1)
    x.append(l/float(points)*float(i))
    y.append(-(H/g)*(math.cosh(alpha(H))-math.cosh((2*beta(H)/l)*x[-1]-alpha(H))))
    #y.append(a*(math.cosh(x[-1]/a)-1))

graph = ROOT.TGraph(points, x, y)
graph.SetMarkerStyle(7)
graph.Draw("PA")
raw_input()
    
