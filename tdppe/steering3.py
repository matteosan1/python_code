import pygame
import sys, math
from Vector import Vector, Path, Obstacle
import Cavallo

def interno():
    b = []
    f = open("interno_piazza.dat")
    lines = f.readlines()
    f.close()
    
    for l in lines:
        items = l.split()
        b.append(((float(items[0])-70)*1.08, (float(items[1])-30)*0.95))
    return b

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
        x = float(lines[i].split()[0])+30
        y = 1000-float(lines[i].split()[1])-50
        points.append((x, y))

    return points

esterno = esterno()
interno = interno()
#bordi = bordiPiazza()
#for t in bordi:
#    path.addNode(Vector(t))

path = Path("piazza_racing_line_v3.dat")
#for t in bordi:
#    path.addNode(Vector(t))

#c = []
offset = (0, 0)
c1 = Cavallo.Cavallo(0, offset, path)
offset = (+12, +12)
c2 = Cavallo.Cavallo(0, offset, path)
offset = (-12, -12)
c3 = Cavallo.Cavallo(0, offset, path)
offset = (-24, -24)
c4 = Cavallo.Cavallo(0, offset, path)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200, 1200))
white = (255, 255, 255)
red   = (255, 0 , 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)

c1.start("corsa")
c2.start("corsa")
c3.start("corsa")
c4.start("corsa")

while(True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit(0)
    
    screen.fill(black)
    msElapsed = clock.tick(60)

    obstacles = []
    obstacles.append(Obstacle(c1.p.coord()))
    obstacles.append(Obstacle(c2.p.coord()))
    obstacles.append(Obstacle(c3.p.coord()))
    obstacles.append(Obstacle(c4.p.coord()))
    c1.setObstacles(obstacles)
    c2.setObstacles(obstacles)
    c3.setObstacles(obstacles)
    c4.setObstacles(obstacles)
    
    c1.move(msElapsed/1000.)
    c2.move(msElapsed/1000.)
    c3.move(msElapsed/1000.)
    c4.move(msElapsed/1000.)
    
    pygame.draw.circle(screen, red,   c1.p.coord(), 5, 0)
    pygame.draw.circle(screen, white, c2.p.coord(), 5, 0)
    pygame.draw.circle(screen, blue,  c3.p.coord(), 5, 0)
    pygame.draw.circle(screen, green, c4.p.coord(), 5, 0)
    #
    for n in path.nodes:
        b = (int(n.backpoint.p[0]), int(n.backpoint.p[1]))
        pygame.draw.circle(screen, blue, b, 1, 0)
    ##for l in linee:
    ##    #print l[0:2]
    ##    l1 = (int(l[0]), int(l[1]))
    ##    l2 = (int(l[2]), int(l[3]))
    ##pygame.draw.line(screen, blue, l1, l2, 1)
    #

    #for i in interno:
    #    b = (int(i[0]), int(i[1]))
    #    pygame.draw.circle(screen, red, b, 1, 0)
    for i in xrange(len(interno)-1):
        p1 = interno[i]
        p2 = interno[i+1]
        pygame.draw.line(screen, red, p1, p2, 1)
    
    #for i in esterno:
    #    b = (int(i[0]), int(i[1]))
    #    pygame.draw.circle(screen, red, b, 1, 0)
    for i in xrange(len(esterno)-1):
        p1 = esterno[i]
        p2 = esterno[i+1]
        pygame.draw.line(screen, red, p1, p2, 1)
        
    pygame.display.update()
    ##if (c.p.x() > 640):
    ##    sys.exit()
    ##if (c.p.y() > 480):
    ##    sys.exit()
