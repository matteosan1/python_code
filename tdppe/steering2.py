import pygame
import sys, math
from Vector import Vector, Path

class Cavallo():
    def __init__(self, pos = [130,0],vmax = 60., thePath=[]):
        self.currentNode = 0
        self.pathDir = 1
        self.nodes = thePath.getNodes()
        self.t = self.nodes[self.currentNode]
        self.max_v = vmax
        self.p = Vector(pos)
        self.v = Vector([0., 0.])
        self.max_see_ahead = 30
        self.max_avoid_force = 1.5
        self.obstacles = []

    def setObstacles(self, obs):
        self.obstacles = obs

    def updatePosition(self, dt):
        self.p = self.p + (self.v*dt)

    def collisionDetector(self):
        dynamic_length = self.v.mod()/self.max_v*self.max_see_ahead
        ahead = self.p + self.v.norm(dynamic_length)
        ahead2 = self.p + self.v.norm(dynamic_length*0.5)
        obstacle = self.takeOver(ahead, ahead2)
        avoidance = Vector()
 
        if (obstacle.p.coord() != [-1, -1]):
            avoidance = ahead-obstacle.p
            if (avoidance.x() == 0):
                avoidance = Vector([self.max_avoid_force, 0])
            elif (avoidance.y() == 0):
                avoidance = Vector([0, self.max_avoid_force])

        return avoidance

    def takeOver(self, ahead, ahead2):
        obstacle = Obstacle([-1, -1])
        min_distance = 9999.
        for o in self.obstacles:
            collision = self.lineIntersectsCircle(o, ahead, ahead2)
            if (o.p.coord() != self.p.coord()): # avoid self veto
                distance = o.p - self.p
                if (distance.dot(ahead) > 0.):
                    if (collision and distance.mod() < min_distance):
                        obstacle = o
                        min_distance = obstacle.p.distance(self.p)

        return obstacle
                
    def lineIntersectsCircle(self, o, ahead, ahead2):
        dist1 = o.p.distance(self.p)
        dist2 = o.p.distance(ahead2)
        return (o.p.distance(ahead) <= o.radius*1.5) or (dist2 <= o.radius*1.5) or (dist1<=(o.radius+15.))
 
    def steering(self):
        current_v = self.v.mod()
        desired_velocity = (self.t-self.p).norm(current_v)
        steering = (desired_velocity-self.v)
        avoid = self.collisionDetector()
        if (steering.mod() < avoid.mod()*2.5):
            steering = avoid
        else:
            steering = steering + avoid

        if (steering.mod() > 2.):
            steering = steering.norm(2.)

        # r = v*v/a_t
        #if (steering.transv(self.v) != 0):
            #r = self.v.mod()*self.v.mod()/steering.transv(self.v)
            #k = 0.5
            #print math.sqrt(k*r)
            
        self.v = self.v + steering
        self.v = self.v.norm(current_v)

    def move(self, dt):
        # FIXME SCEGLI STRATEGIA
        self.pathFollowing()
        self.speedUp()
        self.steering()
        self.updatePosition(dt)

    def speedUp(self):
        #FIXME assegna uno scatto
        current_v = self.v.mod()
        if (current_v == 0.):
            # deve cambiare con il tipo di mossa
            self.direzione = -0.7854
            self.v = Vector([math.cos(self.direzione), math.sin(self.direzione)])
        else:
            updated_v = current_v + 1.
            if (updated_v >= self.max_v):
                updated_v = self.max_v
            
            self.v = self.v.norm(updated_v)

    def pursuit(self):
        pass
        #public function pursuit(t :Boid) :Vector3D {
        #    var distance :Vector3D = t.position - position;
        #    var T :int = distance.length / MAX_VELOCITY;
        #    futurePosition :Vector3D = t.position + t.velocity * T;
        #    return seek(futurePosition);
        #    }

    def pathFollowing(self):
        
        if (self.t.distance(self.p) <= 50.):
            self.currentNode += self.pathDir
            if (self.currentNode >= len(self.nodes) or self.currentNode < 0):
                self.pathDir *= -1 
                self.currentNode += self.pathDir

            self.t = self.nodes[self.currentNode]

class Obstacle():
    def __init__(self, pos=[-1, -1]):
        self.p = Vector(pos)
        self.radius = 10
        self.type = "block"

def distPuntoRetta(p, back_point, m, q):
    target_cavallo = back_point - p
    d = abs(p[1] - m*p[0] - q)/math.sqrt(1+m*m)
    angolo = target_cavallo.dot(self.v)  # se maggiore di 0 ....
    return True
    

def retta(p1, p2, delta = 10, mq=False):
    linea = [0,0,0,0]
    if (p2[0] != p1[0]):
        m = (p2[1] - p1[1])/(p2[0]-p1[0])
        delta = delta*math.cos(math.atan(m))
        q = (p2[0]*p1[1] - p1[0]*p2[1])/(p2[0] - p1[0])
        if (mq):
            print m,q
            return (m, q)
        if (p2[0] < p1[0]):
            linea = (p1[0]+delta, (p1[0]+delta)*m+q, p1[0]-delta, (p1[0]-delta)*m+q)
        else:
            linea = (p1[0]-delta, (p1[0]-delta)*m+q, p1[0]+delta, (p1[0]+delta)*m+q)

    return linea
    
def perpendicolare(p1, p2, delta1=10, delta2=-10, mq=False):
    linea = [0,0,0,0]
    if (p2[0] == p1[0]):
        return linea
    if (p1[1] != p2[1]):
        m = -1 / ((p2[1] - p1[1])/(p2[0]-p1[0]))
        q = -m*p1[0]+p1[1]
        print m, q,
        if (mq):
            return (m,q)
        delta1 = delta1*math.cos(math.atan(m))
        delta2 = delta2*math.cos(math.atan(m))
        if (p2[0] < p1[0]):
            linea = (p1[0]+delta1, (p1[0]+delta1)*m+q, p1[0]-delta1, (p1[0]-delta1)*m+q)
        else:
            linea = (p1[0]+delta2, (p1[0]+delta2)*m+q, p1[0]-delta2, (p1[0]-delta2)*m+q)
    else:
        linea = (p1[0], p1[1]-delta1, p1[0], p1[1]+10)
        
    return linea
        
def coeffAngolare(points, interno):
    linee = []
    #interni = []
    for i in xrange(len(points)-1):
        p2 = points[i+1]
        p1 = points[i]
        # way-point
        print p1[0], p1[1], 
        q1 = retta(p1, p2, 20)
        # back-point
        print q1[0], q1[1],
        # m, q
        linee.append(perpendicolare(q1[0:2],q1[2:4],10))
        #if (len(interno) != 0):
        #    interni = retta(interno[i][0], interno[i][1], 10, True)
                
        
    p2 = points[0]
    p1 = points[len(points)-1]
    print p1[0], p1[1], 
    q1 = retta(p1, p2, 20)
    print q1[0], q1[1],
    linee.append(perpendicolare(q1[0:2],q1[2:4],10))
    #if (len(interno) != 0):
    #    interni = retta(interno[len(points)-1][0], interno[len(points)-1][1], 10, True)
    return linee


def intersezione(m, q, n, r):
    x = (r-q)/(m-n)
    y = m*(r-q)/(m-n)+q

    return (x, y)

#7,4,4,4,9,2,8,11,3,2,8,2,1,1   (partenza) 2
def interno():
    b = []
    f = open("interno_piazza.dat")
    lines = f.readlines()
    f.close()
    
    for l in lines:
        items = l.split()
        print items
        b.append(((float(items[0])-70)*1.08, (float(items[1])-30)*0.95))
    return b
#6,4,3,2,3,2,3,7,2,6,1,,2,10,1,4,5,3,4
def esterno():
    b = []
    f = open("esterno_piazza.dat")
    lines = f.readlines()
    f.close()
    
    for l in lines:
        items = l.split()
        b.append(((float(items[0])-70)*1.1, (float(items[1])-50)*1.))
    return b


def bordiPiazza():
    points = []
    linee = []
    f = open("tdp_geometry.dat")#piazza_racing_line_v3.dat")
    lines = f.readlines()
    f.close()
    
    for i in xrange(0, len(lines), 5):
        print lines[i].split()[0]
        x = float(lines[i].split()[0])+30
        y = 1000-float(lines[i].split()[1])-50
        points.append((x, y))

    return points

esterno = esterno()
interno = interno()
bordi = bordiPiazza()

#interno2 = [interno[0:2],interno[0:2],interno[1:3],interno[1:3],interno[1:3],interno[1:3],
#            interno[2:4],interno[2:4],interno[2:4],interno[2:4],
#            interno[3:5],interno[3:5],interno[4:6],interno[4:6],interno[4:6],
#            interno[5:7],interno[5:7],interno[5:7],interno[5:7],interno[5:7],
#            interno[6:8],interno[6:8],
#            interno[7:9],interno[7:9],interno[7:9],interno[7:9],interno[7:9],interno[7:9],interno[7:9],
#            interno[8:10],interno[8:10],interno[8:10],interno[8:10],interno[8:10],interno[8:10],interno[8:10],interno[8:10],interno[8:10],
#            interno[9:11],interno[9:11],interno[9:11],interno[9:11],interno[10:12],
#            interno[11:13],interno[11:13],interno[11:13],interno[11:13],interno[11:13],interno[11:13],interno[11:13],interno[11:13],
#            interno[12:14],interno[12:14],interno[0:2]]

linee = coeffAngolare(bordi, interno)
#sys.exit()
#path = Path()
#for t in bordi:
#    path.addNode(Vector(t))

#c1 = Cavallo([230,285], 40, path)
#c2 = Cavallo([151,602], 50, path)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200, 1000))
white = (255, 255, 255)
red = (255, 0 , 0)
black = (0, 0, 0)
blue = (0, 0, 255)

while(True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit(0)
    
    screen.fill(black)
    msElapsed = clock.tick(1)

    #obstacles = []
    #o = Obstacle(c1.p.coord())
    #obstacles.append(o)
    #o = Obstacle(c2.p.coord())
    #obstacles.append(o)
    #c1.setObstacles(obstacles)
    #c2.setObstacles(obstacles)
    #
    #c1.move(msElapsed/1000.)
    #c2.move(msElapsed/1000.)

    #pygame.draw.circle(screen, red, c1.p.coord(), 5, 0)
    #pygame.draw.circle(screen, white, c2.p.coord(), 5, 0)

    for b in bordi:
        b = (int(b[0]), int(b[1]))
        pygame.draw.circle(screen, blue, b, 1, 0)
    for l in linee:
        #print l[0:2]
        l1 = (int(l[0]), int(l[1]))
        l2 = (int(l[2]), int(l[3]))
        pygame.draw.line(screen, blue, l1, l2, 1)
    
    for i in interno:
        b = (int(i[0]), int(i[1]))
        pygame.draw.circle(screen, red, b, 1, 0)
    for i in xrange(len(interno)-1):
        p1 = interno[i]
        p2 = interno[i+1]
        pygame.draw.line(screen, red, p1, p2, 1)
    
    for i in esterno:
        b = (int(i[0]), int(i[1]))
        pygame.draw.circle(screen, red, b, 1, 0)
    for i in xrange(len(esterno)-1):
        p1 = esterno[i]
        p2 = esterno[i+1]
        pygame.draw.line(screen, red, p1, p2, 1)
        
    pygame.display.update()
    #if (c.p.x() > 640):
    #    sys.exit()
    #if (c.p.y() > 480):
    #    sys.exit()
