import re, sys, math

from ROOT import TCanvas, TMarker, TH2F, TColor

def angle(x1, y1, x2, y2):
    angle = math.atan2((y2-y1), (x2-x1))
    return angle #math.degrees(angle)


def draw_potential():
    markers = []
    c1 = TCanvas("c1", "Prova")
    h2 = TH2F("h2", "h2", 1000, -100, 1200, 1000, 0, 1000)

    m = re.compile("(\d+)\s(\d+)\s([\-0-9\.]+)\s([\-0-9]+)")
    file = open("mappa_piazza.dat")
    while 1:
        line = file.readline()
        if (not line):
            break
        n = m.match(line)
        if (n):
            po = TMarker(float(n.group(1)), float(n.group(2)), 6)
            po.SetMarkerColor(abs(int(n.group(4)))+1)
            markers.append(po)

    h2.Draw()
    for i in markers:
        i.Draw("SAME")
    c1.SaveAs("potenziale_piazza.png")
    sys.exit(1)

draw_potential()


file = open("output")

m2 = re.compile("([0-9\.]+)\s+([0-9\.]+)\s+([0-9\.]+)\s+([0-9\.]+)")
m3 = re.compile("([0-9\.]+)\s+([0-9\.]+)(\s+\|\s+)([0-9\.]+)\s+([0-9\.]+)(\s+---)")
m4 = re.compile("####")

mappa = []
points = 0
steps = 0
counter = 0
counter_temp = -1
lines = []
while 1:
    line = file.readline()
    if (not line):
        break

    n4 = m4.match(line)
    if (n4):
        for j, i in enumerate(lines):
            mappa.append([points, int(i[0]), int(i[1]), j-counter_temp+1, steps])
            points += 1

        lines = []
        counter = 0
        steps += 1
        

    n2 = m2.match(line)
    if (n2):
        lines.append([float(n2.group(1)), float(n2.group(2))])

    n3 = m3.match(line)
    if (n3):
        counter_temp = counter
        lines.append([float(n3.group(1)), float(n3.group(2))])
    
    counter += 1

angoli = []
temp_coord = []
coord = []
for i in mappa:
    if (i[3] == 0):
        if (len(coord) == 0):
            coord = [i[1], i[2]]
        else:
            temp_coord = coord
            coord = [i[1], i[2]]
            #print temp_coord, coord
            angoli.append(angle(temp_coord[0], temp_coord[1], coord[0], coord[1]))

angoli[len(angoli)-1] = angoli[0]
angoli.append(angoli[0])            

file.close()

file = open("mappa_piazza.dat", "w")

for i in mappa:
    roots = []
    indice = i[4]
    d = i[3]
    if (indice == 340):
        indice = -1
    for j in mappa:
        if (j[4] == indice+1):
            if (j[3] == d or j[3] == d-1 or j[3] == d+1):
                roots.append(j[0])
    if (len(roots) != 0):
        if (indice == -1):
            indice = 340
        if (len(roots) == 1):
            file.write("%d %d %.3f %d %d %d\n" %(i[1], i[2], angoli[indice], i[3], i[4], roots[0]))
        if (len(roots) == 2):
            file.write("%d %d %.3f %d %d %d %d\n" %(i[1], i[2], angoli[indice], i[3], i[4], roots[0], roots[1]))
        if (len(roots) == 3):
            file.write("%d %d %.3f %d %d %d %d %d\n" %(i[1], i[2], angoli[indice], i[3], i[4], roots[0], roots[1], roots[2]))
sys.exit(1)


