#!/usr/lib/python
import os

linese1 = os.popen("grep -e eta1 output_endcap").readlines()
linese2 = os.popen("grep -e eta2 output_endcap").readlines()
linesb0 = os.popen("grep -e eta0 output_barrel").readlines()
linesb1 = os.popen("grep -e eta1 output_barrel").readlines()
linesb2 = os.popen("grep -e eta2 output_barrel").readlines()
linesb3 = os.popen("grep -e eta3 output_barrel").readlines()
linesb4 = os.popen("grep -e eta4 output_barrel").readlines()
linesb5 = os.popen("grep -e eta5 output_barrel").readlines()
linese3 = os.popen("grep -e eta3 output_endcap").readlines()
linese4 = os.popen("grep -e eta4 output_endcap").readlines()

for i in xrange(len(linese1)):
    print "++++++++++++"
    print linese1[i].split("\n")[0]
    print linese2[i].split("\n")[0]
    print linesb0[i].split("\n")[0]
    print linesb1[i].split("\n")[0]
    print linesb2[i].split("\n")[0]
    print linesb3[i].split("\n")[0]
    print linesb4[i].split("\n")[0]
    print linesb5[i].split("\n")[0]
    print linese3[i].split("\n")[0]
    print linese4[i].split("\n")[0]



