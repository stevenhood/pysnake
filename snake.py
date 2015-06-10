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

def main():
	screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
	pygame.display.set_caption('Snake')
	background = pygame.Surface(WINDOW_DIMENSIONS)
	background.fill(pygame.Color(0, 0, 0, 100)) # Black
	screen.blit(background, (0, 0))

	clock = pygame.time.Clock()

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

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN and event.key in key_map:
				key_map[event.key]()
				# print event

if __name__ == "__main__":
	main()