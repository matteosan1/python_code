import random

class Point:
    def __init__(self):
        self.coord = (0,0)
        self.angle = 0
        self.val = 0
        self.pos = 0
        self.leafs = (0,0,0)
    
    def set_point(self, p):
        self.coord = (int(p[0]), int(p[1]))
        self.angle = float(p[2])
        self.val = int(p[3])
        self.pos = int(p[4])
        self.leafs = (int(p[5]), int(p[6]), int(p[7]))

class Barbero:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.vel = 0
        self.fractale = 0
        self.percorso = []

        
class Engine:
    def __init__(self):
        self.players = []
        self.points = []
        self.framesPerSecond = 1

    def set_players(self, n):
        for i in xrange(n):
            p = Barbero()
            self.players.append(p)

    def load_map(self):
        file = open("mappa_piazza.csv")
        lines = file.readlines()
        for line in lines:
            numbers = (line.split("\n")[0]).split(",")
            p = Point()
            #print line
            p.set_point(numbers)
            self.points.append(p)
        
    def mossa(self):
        a = [0, 231, 510, 797, 796, 796, 796, 796, 796, 796]
        for n,i in enumerate(self.players):
            if (n == 0):
                i.posx = 0
            else:
                i.posx = a[n]
                print e.points[i.posx].pos, e.points[i.posx].val
            #i.posy = n
            #i.vel = 10

    def move(self):
        # riordinare i giocatori in base alla posizione
        for p in self.players:
            dx = p.vel/self.framePerSecond
            p.fractale += dx
            # direzione del cavallo (indice di leafs)
            if (p.fractale > 1):
                p.fractale = 1-p.fractale
                p.posx = self.points[p.posx].leafs[0]

    def pos(self, g):
        p = self.players[g]
        pos = (self.points[p.posx].coord, self.points[p.posx].angle)
        return pos
            
    def map(self, n):
        pass

    def u_horse(self, pos1, pos2):
        dy = abs(self.points[pos1].val - self.points[pos2].val)
        dx = self.points[pos1].pos - self.points[pos2].pos

        if ((dy > 2) or (dx > 0) or (dx < -2)):
            return 0
        elif (dy == 1):
            return 2
        elif (dy == 0 and dx == -2):
            return 4
        elif (dy == 0 and dx == -1):
            return 8
        elif (dy == 0 and dx == 0):
            return 9999
        else:
            return 2
    
    def print_dist(self):
        for i in xrange(10):
            if i == 0:
                continue
            dy = abs(self.points[self.players[0].posx].val - self.points[self.players[i].posx].val)
            dx = self.points[self.players[0].posx].pos - self.points[self.players[i].posx].pos

            print i, dx, dy,
        print

    def compute_paths(self):
        self.paths = [[0,],[1,],[2,]]
        for z in xrange(4):
            new_paths = []
            for i in self.paths:
                new_paths.append(i+[0])
                new_paths.append(i+[1])
                new_paths.append(i+[2])
            self.paths = new_paths
            

if __name__ == "__main__":
    e = Engine()
    e.compute_paths()
    e.load_map()
    e.set_players(10)
    e.mossa()
    #print e.pos(0)
    #index = e.points[e.players[0].posx].leafs
    #print index[0], e.points[index[0]].val
        
    for i in xrange(0,340):
        sums = []
        for path in e.paths:
            start = e.points[e.players[0].posx]
            sum = 0
            for element in path:                
                dir = start.leafs[element]
                if (dir != -1):
                    sum = sum + abs(e.points[dir].val)
                    for y in xrange(10):
                        if (y == 0): # se stesso
                            continue
                        sum = sum + e.u_horse(dir, e.players[y].posx)
                else:
                    sum = sum + 9999
            sums.append(sum)

        print min(sums)
        path_index = sums.index(min(sums))
        #print e.paths[path_index] 
        e.players[0].posx = e.points[e.players[0].posx].leafs[e.paths[path_index][0]]
        #e.players[0].posy = e.points[e.paths[path_index][0]].val
        print e.points[e.players[0].posx].pos,  e.points[e.players[0].posx].val
        e.print_dist()

        
#(1-t)*p0 + t*p1
