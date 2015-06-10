#! /usr/bin/env python

# Snake
# version 0.1
# Steven Hood

# Python 2.7.3
# Pygame 1.9.1 (release)

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

	running = True
	while running:
		pass

if __name__ == "__main__":
	main()