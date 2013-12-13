#! /usr/bin/python

from ROOT import *

limit =[0.960, 0.929, 0.891, 0.837, 0.787] 

file = TFile("endcap.root")

h = file.Get("likelihood")
#h.Draw()

for j in limit:
    integral = h.Integral()
    for i in xrange(0, h.GetNbinsX()+1):
        integral = integral - h.GetBinContent(i)
        eff = integral / h.Integral()
        if (eff < j):
            print 'eff %f - threshold %f'%(eff, h.GetBinCenter(i))
            break
