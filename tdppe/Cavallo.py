import sys, math
from Vector import Vector, Path, Obstacle

class Cavallo():
    def __init__(self, currentNode, vmax = 0., thePath=[]):
        #FIXME Caratteristiche cavallo
        self.currentNode = currentNode+1
        self.pathDir = 1
        self.nodes = thePath.nodes
        self.t     = self.nodes[self.currentNode].waypoint
        self.max_v = self.nodes[self.currentNode].vmax
        #self.p = Vector(pos)
        self.p     = self.nodes[currentNode].waypoint
        self.v     = Vector([0., 0.])
        self.max_see_ahead = 30
        self.max_avoid_force = 1.5
        self.obstacles = []
        self.strategy = "mossa"

    def setObstacles(self, obs):
        self.obstacles = obs

    def updatePosition(self, dt):
        self.p = self.p + (self.v*dt)

    def collisionDetector(self):
        if (self.max_v != 0):
            dynamic_length = self.v.mod()/self.max_v*self.max_see_ahead
        else:
            return Vector()
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
        return (o.p.distance(ahead) <= o.radius*2.) or (dist2 <= o.radius*2.) or (dist1<=(o.radius*2))
 
    def steering(self):
        current_v = self.v.mod()
        desired_velocity = (self.t-self.p).norm(current_v)
        steering = (desired_velocity-self.v)
        avoid = self.collisionDetector()
        steering = steering + avoid

        if (steering.mod() > 2.5):
            steering = steering.norm(2.5)

        # r = v*v/a_t
        #if (steering.transv(self.v) != 0):
            #r = self.v.mod()*self.v.mod()/steering.transv(self.v)
            #k = 0.5
            #print math.sqrt(k*r)
            
        self.v = self.v + steering

    def thrust(self, slowDown=False):
        current_v = self.v.mod()

        if (current_v == 0.):
            self.v = Vector([-1., -1.])

        if (current_v > self.max_v):
            if ((current_v - 0.5) <= 0):
                self.v = self.v.norm(0)
            else:
                self.v = self.v.norm(current_v - 0.5)
        elif (current_v < self.max_v):
            self.v = self.v.norm(current_v + 0.5)
        else:
            self.v = self.v.norm(current_v)

    def postoAlCanape(self, posto):
        p = Path("ingresso_canape.dat")
        self.nodes += p.nodes
        self.nodes.append(self.nodes[-1])
        self.nodes[-posto-2].vmax = 1
        self.nodes[-posto-1].vmax = 0

    def move(self, dt):
        if (self.strategy == "mossa"):
            self.pathFollowing()
            self.steering()
            self.thrust()
            self.updatePosition(dt)

    def start(self):
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

        #print angle, d
        if (angle<0 and d < 10):
            self.currentNode += self.pathDir
            # TORNA INDIETRO
            #if (self.currentNode >= len(self.nodes) or self.currentNode < 0):
            #    self.pathDir *= -1 
            #    self.currentNode += self.pathDir
            if (self.currentNode == len(self.nodes)):
                self.currentNode = 0 
                           
            self.t     = self.nodes[self.currentNode].waypoint
            self.max_v = self.nodes[self.currentNode].vmax

