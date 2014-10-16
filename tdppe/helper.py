import math
from Vector import Path, Vector

def retta(p1, p2, delta = 1, mq=False):
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
    
def perpendicolare(p1, p2, delta1=1, delta2=-1, mq=False):
    linea = [0,0,0,0]
    if (p2[0] == p1[0]):
        #print "QUI"
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
        m = 100000.
        q = -m*p1[0]+p1[1]
        print m, q,
        linea = (p1[0], p1[1]-delta1, p1[0], p1[1]+10)
    return linea


def coeffAngolare(points, dist=20):
    linee = []
    for i in xrange(len(points)-1):
        p2 = points[i+1]
        p1 = points[i]
        # way-point
        print p1[0], p1[1], 
        q1 = retta(p1, p2, dist)
        # back-point
        print q1[0], q1[1],
        # m, q
        linee.append(perpendicolare(q1[0:2],q1[2:4],10))
        #if (len(interno) != 0):
        #    interni = retta(interno[i][0], interno[i][1], 10, True)
        #if (len(esterno) != 0):
        #    esterni = retta(esterno[i][0], esterno[i][1], 10, True)
        print  
        
    p2 = points[0]
    p1 = points[len(points)-1]
    print p1[0], p1[1], 
    q1 = retta(p1, p2, dist)
    print q1[0], q1[1],
    linee.append(perpendicolare(q1[0:2],q1[2:4],10))
    #if (len(interno) != 0):
    #    interni = retta(interno[len(points)-1][0], interno[len(points)-1][1], 10, True)
    #if (len(esterno) != 0):
    #    esterni = retta(esterno[i][0], esterno[i][1], 10, True)
    print
    return linee

def findWayline(filename):
    path = Path(filename)
    points = []
    for p in path.nodes:
        points.append((p.waypoint.p[0], p.waypoint.p[1]))
    coeffAngolare(points, 2)

findWayline("ingresso_canape.dat")
