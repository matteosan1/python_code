# -*- coding: utf-8 -*-
from ROOT import TCanvas, TGraph, TMarker, TH2F, TLine
from array import array
import math

class point:
  def __init__(self, x, y):
    px = x
    py = y
    

def corsie(n, x1, y1, x2, y2):
  #m = -1/m
  #q = y - m*x
  
  theta = math.pi/2. + math.atan2(y2-y1, x2-x1)
  
  xn = x1 + (n*10.)*math.cos(theta) #- (n*10.)*math.sin(theta)
  yn = y1 + (n*10.)*math.sin(theta) #+ (n*10.)*math.cos(theta)
  
  return (xn, yn)

def intersezione(x, y):
  m1 = (y[1]-y[0])/(x[1]-x[0])
  m1 = -1/m1
  q1 = y[0] - m1*x[0]
  #return (m1,q1)
  
  m2 = (y[2]-y[3])/(x[2]-x[3])
  q2 = y[2] - m2*x[2]
  #return (m2, q2)
  ix = (q1-q2)/(m2-m1)
  iy = m1*(q1-q2)/(m2-m1) + q1
  
  return (ix, iy)

c1 = TCanvas("c1", "Prova", 1200, 1000)
h2 = TH2F("h2", "h2", 1000, -100, 1200, 1000, 0, 1000)
h2.Draw("N")

n1 = 340
##n2 = 170
n3 = 45
#x1, y1 = array('f'), array('f')
##x2, y2 = array('f'), array('f')
x3, y3 = array('f'), array('f')
#edge_in = array('i')
#edge_out = array('i')
#coeff_ang = array('f')

#file = open("tdp_geometry.dat")
#line = file.readline()

##i = 0
#while True:
    #line = file.readline()
    #if not line:
        #break

    #if (line !=  "\n"):
        #xtemp = line.split(" ")
        ##if (i < 10):
	#x1.append(float(xtemp[0]))
	#y1.append(float(xtemp[1]))
	#coeff_ang.append(float(xtemp[2]))
	#edge_in.append(int(xtemp[4]))
	#edge_out.append(int(xtemp[5]))
        ##else:
        ##    x2.append(float(xtemp[0]))
        ##    y2.append(float(xtemp[1]))
    ##i+=1
    ##if (i == 20):
    ##    i = 0


file = open("bordo_piazza.dat")
for i in xrange(42):
  line = file.readline()
  xtemp = line.split(" ")
  x3.append(float(xtemp[0])*0.95)
  y3.append(float(xtemp[2])*1.01)

l=[]
for i in xrange(1, 42):
  if (i == 13):
    continue
  l.append(TLine(x3[i], y3[i], x3[i-1], y3[i-1]))
  l[-1].Draw("SAME")

#gr3 = TGraph(n3, x3, y3)
#gr3.SetLineColor(1)
#gr3.SetMarkerColor(1)
#gr3.SetMarkerStyle(2)
#gr3.Draw("LSAME")

#gr1 = TGraph(n1, x1, y1)
#gr1.SetLineColor(2)
#gr1.SetMarkerColor(2)
#gr1.SetMarkerStyle(6)
#gr1.Draw("PSAME")

#gr2 = TGraph(n2, x2, y2)
#gr2.SetLineColor(4)
#gr2.SetMarkerColor(4)
#gr2.SetMarkerStyle(3)
#gr2.Draw("PSAME")

#file1 = open("true_geometry_temp.dat", "write")

#markers = []
## arriva a 340
#for i in range(0, 340):
  ##print x1[i]
  ##print edge[i]
  #px = [x1[i],x1[i+1], x3[edge_in[i]], x3[edge_in[i]+1]]
  #py = [y1[i],y1[i+1], y3[edge_in[i]], y3[edge_in[i]+1]]
  #a,b = intersezione(px, py)  
  #dist3 = math.sqrt(math.pow(x1[i+1]-x1[i],2)+math.pow(y1[i+1]-y1[i],2))
  #dist1 = math.sqrt(math.pow(a-x1[i],2)+math.pow(b-y1[i],2))
  #ddx = int(dist1 / 12.)

  ##print a,b
  ##for j in xrange(x1[i], x1[i]+100):
  ##po = TMarker(j, a*j+b, 6)
  #po = TMarker(a, b, 6)
  #po.SetMarkerColor(4)
  #markers.append(po)

  #px = [x1[i],x1[i+1], x3[edge_out[i]], x3[edge_out[i]+1]]
  #py = [y1[i],y1[i+1], y3[edge_out[i]], y3[edge_out[i]+1]]
  #a,b = intersezione(px, py)
  #dist2 = math.sqrt(math.pow(a-x1[i],2)+math.pow(b-y1[i],2))
  #dsx = int(dist2 / 10.)
  
  #po = TMarker(a, b, 6)
  #po.SetMarkerColor(4)
  #markers.append(po)

  ##print i, math.degrees(math.atan2(y1[i+1]-y1[i], x1[i+1]-x1[i])), \
  ##math.degrees(math.pi/2. + math.atan2(y1[i+1]-y1[i], x1[i+1]-x1[i]))
  #for j in xrange(ddx+1, 0, -1):
    #a, b = corsie(-j, x1[i], y1[i], x1[i+1], y1[i+1])
    ##po = TMarker(a, b, 6)
    ##po.SetMarkerColor(1)
    ##markers.append(po)
    #file1.write(str(a)+" "+str(b)+"\n")
    
  #file1.write(str(x1[i])+" "+str(y1[i])+" ---\n")  
  #for j in xrange(1, dsx+1):
      #a, b = corsie(j, x1[i], y1[i], x1[i+1], y1[i+1])
      ##print x1[i], y1[i], a, b, math.degrees(math.pi/2. + math.atan(coeff_ang[i]))
      ##po = TMarker(a, b, 6)
      ##po.SetMarkerColor(3)
      ##markers.append(po)
      #file1.write(str(a)+" "+str(b)+"\n")    
  ##print ddx, dsx
  #file1.write("####\n")
  
#file1.close()

#file1 = open ("true_geometry.dat")

##while 1:
#counter = 0
#color = 2
##for i in range(0,0):
#while 1:
  #line = file1.readline()
  #if (not line):
    #break

  #if (line.find("#") == -1):
    #coord = line.split(" ")
    #po = TMarker(float(coord[0]), float(coord[1]), 6)
    #po.SetMarkerColor(color)
    #markers.append(po)
  #elif (line == "####\n"):
    #counter += 1
    #if (color == 2):
      #color = 4
    #else: 
      #color = 2
      
#file1.close()
#print counter
#for i in markers:
#  i.Draw("SAME")
  
c1.SaveAs("bordo_piazza.root")
