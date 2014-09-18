import pygame
import sys, math

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
        return Vector([self.p[0]/n*k, self.p[1]/n*k])

class Path():
    def __init__(self):
        self.nodes = []
 
    def setPath(self, p):
        for point in p:
            self.nodes.append(point)
 
    def addNode(self, node):
        self.nodes.append(node)
 
    def getNodes(self):
        return self.nodes

class Cavallo():
    def __init__(self, pos = [130,0], thePath=[], obs=[]):
        self.currentNode = 0
        self.pathDir = 1
        self.nodes = thePath.getNodes()
        self.t = self.nodes[self.currentNode]
        self.max_v = 100.
        self.p = Vector(pos)
        self.v = Vector([0., self.max_v])
        self.max_see_ahead = 30
        self.max_avoid_force = 1.5
        self.obstacles = obs
        self.closestApproach = 999.

    def updatePosition(self, dt):
        self.p = self.p + (self.v*dt)

    def collisionDetector(self):
        dynamic_length = self.v.mod()/self.max_v*self.max_see_ahead
        ahead = self.p + self.v.norm(dynamic_length)
        ahead2 = self.p + self.v.norm(dynamic_length*0.5)
        obstacle = self.findMostThreateningObstacle(ahead, ahead2)
        avoidance = Vector()
 
        if (obstacle.p.coord() != [-1, -1]):
            avoidance = ahead-obstacle.p
            if (avoidance.x() == 0):
                avoidance = Vector([self.max_avoid_force, 0])
            elif (avoidance.y() == 0):
                avoidance = Vector([0, self.max_avoid_force])

        return avoidance

    def findMostThreateningObstacle(self, ahead, ahead2):
        obstacle = Obstacle([-1, -1])
 
        for o in self.obstacles:
            collision = self.lineIntersectsCircle(o, ahead, ahead2)
            if (collision and ((obstacle.p.coord() == (-1, -1)) or
                               o.p.distance(self.p) < obstacle.p.distance(self.p))):
                obstacle = o

        return obstacle

    def lineIntersectsCircle(self, o, ahead, ahead2):
        return o.p.distance(ahead) <= o.radius*2. or o.p.distance(ahead2) <= o.radius*2. or o.p.distance(self.p)<=(o.radius+15.)
 
    def steering(self):
        current_v = self.v.mod()
        desired_velocity = (self.t-self.p).norm(current_v)
        steering = (desired_velocity-self.v)
        avoid = self.collisionDetector()
        if (steering.mod() < avoid.mod()*2.5):
            steering = avoid
        else:
            steering = steering + avoid

        if (steering.mod() > 2.5):
            steering = steering.norm(2.5)

        # r = v*v/a_t
        if (steering.transv(self.v) != 0):
            r = self.v.mod()*self.v.mod()/steering.transv(self.v)
            k = 0.5
            print math.sqrt(k*r)
            
        self.v = self.v + steering
        self.v = self.v.norm(current_v)

    def pursuit(self):
        pass
        #public function pursuit(t :Boid) :Vector3D {
        #    var distance :Vector3D = t.position - position;
        #    var T :int = distance.length / MAX_VELOCITY;
        #    futurePosition :Vector3D = t.position + t.velocity * T;
        #    return seek(futurePosition);
        #    }

    def pathFollowing(self):
        
        if (self.t.distance(self.p) <= 30.):
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

obstacles = []
o = Obstacle([130, 100])
obstacles.append(o)
o = Obstacle([180, 150])
obstacles.append(o)
o = Obstacle([230, 200])
obstacles.append(o)


targets = [(130,200),(320, 240), (300, 300), (200, 150)]
path = Path()
for t in targets:
    path.addNode(Vector(t))
c = Cavallo([130,10], path, obstacles)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640, 480))
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
    msElapsed = clock.tick(60)
    c.pathFollowing()
    c.steering()
    c.updatePosition(msElapsed/1000.)

    pygame.draw.circle(screen, red, c.p.coord(), 5, 0)
    for t in targets:
        pygame.draw.circle(screen, white, t, 2, 0)
    for o in obstacles:
        pygame.draw.circle(screen, blue, o.p.coord(), o.radius, 0)

    pygame.display.update()
    if (c.p.x() > 640):
        sys.exit()
    if (c.p.y() > 480):
        sys.exit()
