import pygame
import sys, math
from Vector import Vector, Path

class Cavallo():
    def __init__(self, pos = [130,0],vmax = 60., thePath=[]):
        self.currentNode = 0
        self.pathDir = 1
        self.nodes = thePath.nodes
        self.t = self.nodes[self.currentNode].waypoint
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
        #FIXME scegli una direzione di partenza e assegna uno scatto
        current_v = self.v.mod()
        if (current_v == 0.):
            self.v = Vector([1., 0.])
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
        target_boundary = self.nodes[self.currentNode].backpoint - self.p
        m = self.nodes[self.currentNode].m
        q = self.nodes[self.currentNode].q
        d = abs(self.p.p[1] - m*self.p.p[0] - q)/math.sqrt(1+m*m)
        angle = target_boundary.dot(self.v)  

        if (angle<0 and d < 10):
        #if (self.t.distance(self.p) <= 50.):
            self.currentNode += self.pathDir
            if (self.currentNode >= len(self.nodes) or self.currentNode < 0):
                self.pathDir *= -1 
                self.currentNode += self.pathDir

            self.t = self.nodes[self.currentNode].waypoint

class Obstacle():
    def __init__(self, pos=[-1, -1]):
        self.p = Vector(pos)
        self.radius = 10
        self.type = "block"

    
path = Path("piazza_racing_line_v2.dat")
#for t in bordi:
#    path.addNode(Vector(t))
c1 = Cavallo([171,582], 50, path)
c2 = Cavallo([151,602], 40, path)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200, 1200))
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

    obstacles = []
    o = Obstacle(c1.p.coord())
    obstacles.append(o)
    o = Obstacle(c2.p.coord())
    obstacles.append(o)
    c1.setObstacles(obstacles)
    c2.setObstacles(obstacles)
    
    c1.move(msElapsed/1000.)
    c2.move(msElapsed/1000.)

    pygame.draw.circle(screen, red, c1.p.coord(), 5, 0)
    pygame.draw.circle(screen, white, c2.p.coord(), 5, 0)

    for n in path.nodes:
        b = (int(n.backpoint.p[0]), int(n.backpoint.p[1]))
        pygame.draw.circle(screen, blue, b, 1, 0)
    #for l in linee:
    #    #print l[0:2]
    #    l1 = (int(l[0]), int(l[1]))
    #    l2 = (int(l[2]), int(l[3]))
    #pygame.draw.line(screen, blue, l1, l2, 1)
    
    pygame.display.update()
    #if (c.p.x() > 640):
    #    sys.exit()
    #if (c.p.y() > 480):
    #    sys.exit()
