import math

class Vector():
    def __init__(self, pos=[0,0]):
        self.p = pos

    def long(self, v):
        l = self.dot(v)*self.mod()
        return l

    def transv(self, v):
        return math.sqrt(self.mod2() - self.long(v)*self.long(v))

    def dot(self, p1):
        if (self.mod() != 0 and p1.mod() != 0):
            r = (self.p[0]*p1.p[0]+self.p[1]*p1.p[1])/(self.mod()*p1.mod())
            return r
        else:
            return 0
        
    def x(self):
        return int(self.p[0])
    
    def y(self):
        return int(self.p[1])

    def coord(self):
        return [int(self.p[0]), int(self.p[1])]

    def __iadd__(self, p1):
        self.p = [self.p[0]+p1.p[0], self.p[1]+p1.p[1]]

    def __isub__(self, p1):
        self.p = [self.p[0]-p1.p[0], self.p[1]-p1.p[1]]

    def __add__(self, p1):
        return Vector([self.p[0]+p1.p[0], self.p[1]+p1.p[1]])

    def __sub__(self, p1):
        return Vector([self.p[0]-p1.p[0], self.p[1]-p1.p[1]])

    def __mul__(self, n):
        return Vector([self.p[0]*n, self.p[1]*n])
 
    def distance(self, p1):
        dx = (self.p[0]-p1.p[0])*(self.p[0]-p1.p[0])
        dy = (self.p[1]-p1.p[1])*(self.p[1]-p1.p[1])
        return math.sqrt(dx+dy)

    def mod(self):
        return math.sqrt(self.mod2())

    def mod2(self):
        n = self.p[0]*self.p[0]+self.p[1]*self.p[1]
        return n
    
    def norm(self, k=1.):
        n = self.mod()
        if (n == 0):
            return Vector([self.p[0]*k, self.p[1]*k])
        else:
            return Vector([self.p[0]/n*k, self.p[1]/n*k])


class Node():
    def __init__(self, wp=Vector(), bp=Vector(), md=0, qd=0, vd=1000.):
        self.waypoint = wp
        self.backpoint = bp
        self.m = md
        self.q = qd
        self.vmax = vd

class Path():
    def __init__(self, filename=""):
        self.nodes = []
        if (filename != ""):
            self.add(filename)

    def add(self, filename):
        f = open(filename)
        lines = f.readlines()
        f.close()

        for l in lines:
            if ("#" in l):
                continue
            items = l.split("\n")[0].split()
            n = Node(Vector([float(items[0]), float(items[1])]), Vector([float(items[2]), float(items[3])]), float(items[4]), float(items[5]), float(items[6]))
            self.nodes.append(n)
        
class Obstacle():
    def __init__(self, pos=[-1, -1]):
        self.p = Vector(pos)
        self.radius = 10
        self.type = "block"

