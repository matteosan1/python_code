import Cavallo
import pygame
from pygame.locals import *
from Vector import Vector, Path, Obstacle

path = Path("tondino.dat")
path.add("ingresso_canape.dat")


cavalli = []

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200, 1200))
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0 , 0)

cavalli.append(Cavallo.Cavallo(5, 50, path))
cavalli.append(Cavallo.Cavallo(8, 50, path))
cavalli.append(Cavallo.Cavallo(10, 50, path))
cavalli.append(Cavallo.Cavallo(12, 50, path))

for c in cavalli:
    c.start()

chiamata_mossa = 0
mossa = [1,3,0,2]

pygame.time.set_timer(USEREVENT+1, 10000)
while(True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit(0)
        if event.type == (USEREVENT+1):
            if ((chiamata_mossa>0 and cavalli[mossa[chiamata_mossa-1]].currentNode > 24) or chiamata_mossa == 0):
                cavalli[mossa[chiamata_mossa]].postoAlCanape(chiamata_mossa)
                chiamata_mossa += 1
                if (chiamata_mossa == 4):
                    pygame.time.set_timer(USEREVENT+1, 0)
    
    screen.fill(black)
    msElapsed = clock.tick(60)

    for n in path.nodes:
        b = (int(n.backpoint.p[0]), int(n.backpoint.p[1]))
        pygame.draw.circle(screen, blue, b, 1, 0)

    for c in cavalli:
        c.move(msElapsed/1000.)
        pygame.draw.circle(screen, red, c.p.coord(), 5, 0)
    
    pygame.display.update()
