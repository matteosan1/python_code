class Point():
    def __init__(self):
        self.coord = (0, 0)
        self.angle = 0 # in radianti
        self.level = -1
        self.handicap = -1
        self.links = []
    
    def __str__(self):
        return str(self.handicap)+" " +str(self.level)+" "+str(self.links)

    def x(self):
        return self.coord[0]
    
    def y(self):
        return self.coord[1]

points = []
f = file("mappa_piazza.csv")
lines = f.readlines()
for line in lines:
    n = line.split("\n")[0].split(",")
    p = Point()
    p.coord = (int(n[0]), int(n[1]))
    p.angle =  float(n[2])
    p.handicap = int(n[3])
    p.level = int(n[4])
    p.links = [int(n[5]), int(n[6]), int(n[7])]
    points.append(p)
    #print p.coord, p.angle, p.links

for p in points:
    temp_links = [-1, -1, -1]
    for i in p.links:
        if (i == -1):
            continue
        diff = points[i].handicap - p.handicap + 1
        if (diff>2):
            print points[i], p
        else:
            temp_links[diff] = i

    p.links = temp_links

f1 = file("mappa_piazza2.csv", "w")
for p in points:
    f1.write(str(p.coord[0])+","+str(p.coord[1])+","+str(p.angle)+","+str(p.handicap)+","+str(p.level)+","+str(p.links[0])+","+str(p.links[1])+","+str(p.links[2])+"\n")

f1.close()
    
    
