import pygame, sys

def implies(i, j):
	k = j+i
	return (i, k), (j, k)

def back_implies(i, j):
	return i, j-i

COLOR = pygame.Color('#FFFFFF')
ITERATIONS = 400


class PrimeChart(object):
	def __init__(self, iterations):
		self.size = iterations
		self.surface = pygame.Surface((iterations, iterations))
		self.populate(iterations)

	def draw_and_crawl(self, source, threshold, color):
		for i, j in source:
			if i > threshold or j > threshold:
				continue
			self.surface.set_at((i-1, j-1), color)
			self.surface.set_at((j-1, i-1), color)
			k1, k2 = implies(i, j)
			yield k1
			yield k2
	
	def populate(self, threshold):
		source = [(1, 2)]
		for i in range(threshold):
			#cindex += sign
			#if cindex <= 0: 
			#	cindex = 2
			#	sign = 1
			#color = cindex, cindex, cindex
			source = list(self.draw_and_crawl(source, threshold, COLOR))

	def draw(self, surface, zoom, offset=(0,0)):
		size = self.size * zoom
		surface.blit(pygame.transform.scale(self.surface, (size, size)), offset)

pygame.init()
screen = pygame.display.set_mode((ITERATIONS*2, ITERATIONS*2))
chart = PrimeChart(ITERATIONS)
zoom = 2
chart.draw(screen, zoom)
pygame.display.flip()

offsetmap = {273:(0,-1),
		274:(0,1),
		275:(1,0),
		276:(-1,0),}

zoommap = {'o': -1,
	'i':1}

offset = (0,0)

while True:
	event = pygame.event.wait()
	if event.type == pygame.QUIT: sys.exit()
	if event.type == pygame.KEYDOWN:
		if event.key in offsetmap:
			off = offsetmap[event.key]
			offset = (offset[0]+off[0]*zoom, offset[1]+off[1]*zoom)
			chart.draw(screen, zoom, offset)
			pygame.display.flip()
		elif event.unicode in zoommap:
			zoom += zoommap[event.unicode]
			if zoom > 1:
				chart.draw(screen, zoom)
				pygame.display.flip()
			else:
				zoom = 2
		elif event.unicode == 'q':
			sys.exit()

