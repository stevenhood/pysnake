#! /usr/bin/env python

# Snake
# version 0.1
# Steven Hood

# Python 2.7.3
# Pygame 1.9.1 (release)

import sys
import pygame
from pygame.sprite import Sprite

pygame.init()

WINDOW_DIMENSIONS = (WINDOW_WIDTH, WINDOW_HEIGHT) = 640, 480

class Part(Sprite):
	def __init__(self, x, y, velocity_x, velocity_y):
		Sprite.__init__(self)
		self.image = pygame.Surface([5, 5])
		self.image.fill(pygame.Color(0, 255, 0, 100)) # Green
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.velocity_x = velocity_x
		self.velocity_y = velocity_y

	def update(self):
		self.rect.move_ip(self.velocity_x, self.velocity_y)

class Snake(Sprite):
	pass

def main():
	screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
	pygame.display.set_caption('Snake')
	background = pygame.Surface(WINDOW_DIMENSIONS)
	background.fill(pygame.Color(0, 0, 0, 100)) # Black
	screen.blit(background, (0, 0))

	clock = pygame.time.Clock()
	part = Part(10, 10, 1, 1)
	sprites = pygame.sprite.Group([part])

	def end():
		sys.exit(0)

	key_map = {
		pygame.K_ESCAPE: end
	}
	pygame.key.set_repeat(1, 50)

	running = True
	while running:
		clock.tick(30)
		pygame.display.set_caption('Snake :: {0:.2f} fps'.format(clock.get_fps()))

		sprites.update()
		sprites.draw(screen)
		pygame.display.flip()
		sprites.clear(screen, background)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN and event.key in key_map:
				key_map[event.key]()
				# print event

if __name__ == "__main__":
	main()