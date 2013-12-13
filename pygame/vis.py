import math
import pygame
import random
import engine

pygame.init()
from pygame.locals import*

screen = pygame.display.set_mode((800, 600))

class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pantera.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.reset()
        self.dy = 5

    def update(self):
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()

    def reset(self):
        self.rect.top = random.randrange(-500, -10)
        


class Truck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.frame = 0
        self.delay = 2
        self.pause = 0

        self.reset()

    def update(self):
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.truckImages):
                self.frame = 0
            self.image = self.truckImages[self.frame]


        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()

    def reset(self):
        self.rect.bottom = random.randrange(-500, -10)
        self.rect.centerx = random.randrange(150, 270)
        self.dy = random.randrange(6, 10)

    def loadImages(self):
        self.imageStand = pygame.image.load("fantino_nicchio.png")
        self.imageStand = self.imageStand.convert()

        self.truckImages = []
        for i in range(4):
            #imgName = "truck0%d.gif" % i
            imgName = "pantera.gif"
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            self.truckImages.append(tmpImage)
            
class SpriteCavallo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.centerx = 279 
        self.rect.centery = 154
        self.frame = 0
        self.angle = math.degrees(1.107)
        self.rotate(self.angle)
        self.delay = 0
        self.pause = 0
        
    def translate_coord(self, f):
        dx = 0
        dy = 0
        if (f == 1):
            dx = -70
            dy = -55
        else:
            dx = -70
            dy = -55
            
        self.rect.centerx = 279 - dx 
        self.rect.centery = 154 - dy

    def rotate(self, a):
        self.angle = a
        self.image = pygame.transform.rotate(self.image, a)
        
    def update(self):
        self.frame += 1
        if self.frame >= len(self.cavalloImages):
            self.frame = 0
        self.image = self.cavalloImages[self.frame]
        #self.rotate(self.angle)
        #key = pygame.key.get_pressed()
        #if key[K_RIGHT]:     
        #    self.rotate = pygame.transform.rotate
        #    self.image = self.rotate(surface, angle)
        #    self.rect.centerx += 5
        #if key[K_LEFT]:
        #    self.rect.centerx += -5
        #self.pause += 1
        #if self.pause >= self.delay:
        #    self.pause = 0
        #    self.frame += 1
        #    if self.frame >= len(self.carImages):
        #        self.frame = 0
        #    self.image = self.carImages[self.frame]
        #if self.rect.right > 400:
        #    self.rect.right = 400
        #if self.rect.left < 0:
        #    self.rect.left = 0

    def loadImages(self):
        self.imageStand = pygame.image.load("fantino_nicchio00.png")
        self.imageStand = self.imageStand.convert()
        self.cavalloImages = []
        for i in range(3):
            imgName = "fantino_nicchio0%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            self.cavalloImages.append(tmpImage)

class Piazza(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../../tdpengine/bordo_piazza_tmp.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.frame = 0
        self.set_frame(self.frame)

    def update(self):
        pass
        #self.rect.bottom += self.dy
        #if self.rect.top >= 0:
        #    self.reset()

    def set_frame(self, f):
        self.frame = f
        if (f == 1):
            self.rect.bottom = screen.get_height()+310
            self.rect.left = -335
        elif (f == 2):
            self.rect.bottom = screen.get_height()+310
            self.rect.left = -600
        elif (f == 3):
            self.rect.bottom = screen.get_height()+55
            self.rect.left = -600
        elif (f == 4):
            self.rect.bottom = screen.get_height()+55
            self.rect.left = -335
        elif (f == 5):
            self.rect.bottom = screen.get_height()+55
            self.rect.left = -70
        else:
            self.rect.bottom = screen.get_height()+310
            self.rect.left = -70

def main():
    screen = pygame.display.set_mode((280, 280))
    pygame.display.set_caption("TdP II Online")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,255,0))
    screen.blit(background, (0,0))

    #block = Block()
    #block2 = Block()
    #block2.rect.centerx = 350
    #truck = Truck()
    cavallo = SpriteCavallo()

    cavallo.rotate(15)

    piazza = Piazza()

    SpriteGroup = pygame.sprite.Group(piazza, cavallo)#, truck, block, block2)

    e = engine.Engine()
    e.compute_paths()
    e.load_map()
    e.set_players(10)
    e.mossa()


    #clock = pygame.time.Clock()
    #keepGoing = True
    SpriteGroup.draw(screen)
    #pygame.display.flip()
    #while keepGoing:
    #    clock.tick(30)
    #       for event in pygame.event.get():
    #           if event.type == pygame.QUIT: 
    #               keepGoing = False
    #       key = pygame.key.get_pressed()
    #       if car.rect.colliderect(truck.rect):
    #           road.dy = 0
    #           truck.reset()
    #           truck.dy = 0
    #           block.dy = 0
    #           block2.dy = 0
    #       if car.rect.colliderect(block.rect):
    #           road.dy = 0
    #           block.reset()
    #           block.dy = 0
    #           truck.dy = 0
    #           block2.dy = 0
    #       if car.rect.colliderect(block2.rect):
    #           road.dy = 0
    #           block2.reset()
    #           block2.dy = 0
    #           truck.dy = 0
    #           block.dy = 0
    #       if key[K_SPACE]:
    #           road.dy = 5
    #           block.dy = 5
    #           block2.dy = 5
    #           truck.dy = random.randrange(6, 10)
        SpriteGroup.clear(screen, background)
        SpriteGroup.update()
        SpriteGroup.draw(screen)
        pygame.display.flip()
        e.move()


if __name__ == "__main__":
    main()



# def update(self, cur_time):
#        if self.update_time < cur_time:
#            mov_x=math.cos(self.angle)
#            mov_y=math.sin(self.angle)
#            if self.speed < self.maxSpeed:
#                self.speed=self.speed + self.speedKoef* self.angle
#            if self.speed < 0:
#                self.speed = 0
#            pos_xo=self.pos_x
#            pos_yo=self.pos_y
#            self.pos_x=(self.pos_x + self.speed * mov_x) % self.win_x
#            self.pos_y=((self.pos_y + self.speed * mov_y))%self.win_y
#            self.next_update_time = cur_time + 10

#            self.image=pygame.transform.rotate(self.image,(self.angle))

#            self.rect=self.image.get_rect()

#            self.rect.top=self.pos_y
#            self.rect.left=self.pos_x


#called through
#            self.dogfighter.update(pygame.time.get_ticks())
#            rectlist=self.dogfighter.draw(self.window)
#            pygame.display.update(rectlist)
#            self.dogfighter.clear(self.window,self.background)


            
