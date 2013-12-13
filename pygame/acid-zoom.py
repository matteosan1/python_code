"""
Program		:	Acid Blur (not that I'd know)
Author		:	Gareth "Korruptor" Noyce (<a href=http://www.korruptor.demon.co.uk/>Home</a>)
Depend		:	Numeric, Pygame with Surfarray
Description	:

    This is probably familiar to anyone who uses iTunes or Winamp visualisations, 
and it's another *really* easy one.

Basically, a four step process:

1) Scale the display surface
2) Blur the scaled surface
3) Draw something onto the blurred, scaled surface
3) Blit the central portion of this to the display

I'll leave out the goto 1 ;-)

The blur is a basic convolution, as demonstrated by Pete in his excellent Surfarray
tutorial. The only thing here that's new is our use of pygame's transform functions 
to scale the surface.

This is dedicated to slm, who seems to think I'm writing a visualisation library. :)
"""

import pygame, pygame.transform, pygame.image
from pygame.surfarray import *
from pygame.locals import *
from Numeric import *

# ------------------------------------------------------------------------------------
# Glob decs

# Screen resolution...
RES 	= array((320,200))
PI 	= 3.14159
DEG2RAD = PI/180

# -----------------------------------------------------------------------------------
def main():
    
    pygame.init()

    # Setup an 8bit screen...
    screen = pygame.display.set_mode(RES,0,8)
    
    # Load a sprite and setup the palettes and colorkey info
    sprite = pygame.image.load("sprite.gif")
    sprite.set_palette(sprite.get_palette())
    sprite.set_colorkey((0,0,0))

    screen.set_palette(sprite.get_palette())

    # This is our "working surface"...
    worksurf = pygame.Surface(RES,0,8)
    worksurf.set_palette(sprite.get_palette())

    
    # Angle deltas for sin/cos
    xd = 0
    yd = 0
    
    # Fruity loops...
    while 1:
        # Have we received an event to quit the program?
        for e in pygame.event.get():
            if e.type in (QUIT,KEYDOWN,MOUSEBUTTONDOWN):
                return

        # Calculate a new x/y position for the sprite...
        x    = ((RES[1]/4))*cos((xd*DEG2RAD) * 2.75)
        y    = ((RES[1]/4))*sin((yd*DEG2RAD) * 1.13)

        # Increment the 'angles'
        xd  += 1.5
        yd  += 3

        # Scale the working surface up by 16px x 16px -- obviously
        # smaller values == a slower blur.
        worksurf = pygame.transform.scale(screen, (RES[0]+16,RES[1]+16))

        # Copy the surf array of the scaled surface to a temporary array
        tmp = pygame.surfarray.array2d(worksurf)
        
        # Workarr will contain the 'blurred' version of the scaled surface
        workarr = array(tmp)

        # This is exactly the same blur that's demonstrated in the Surfarray
        # tutorial by Pete Shinners. An 8px version would probably look a 
        # little better, but it's no great shakes for this demo...
        workarr[1:,:]  += tmp[:-1,:]*8
        workarr[:-1,:] += tmp[1:,:]*8
        workarr[:,1:]  += tmp[:,:-1]*8
        workarr[:,:-1] += tmp[:,1:]*8
        workarr /= 33
        
        # Take the central portion of the scaled (and now blurred) array
        # and blit it to the screen. This creates an inward zoom...
        # If you change the blit offset, you can move the blur 
        # e.g.: workarr[16:RES[0]+16,8:RES[1]+8].shape == left motion,
        # so moving them about a sine would be easy and look quite nice ;)
        blit_array(screen, workarr[8:RES[0]+8,8:RES[1]+8])
        screen.blit(sprite,(x+110,y+50))
        
        # show the results...
	pygame.display.update()

if __name__ == '__main__': main()

