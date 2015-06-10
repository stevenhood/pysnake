#! /usr/bin/env python

# Snake
# version 0.1
# Steven Hood

# Python 2.7.3
# Pygame 1.9.1 (release)
# enum34 for Enum

import sys
import pygame
from pygame.sprite import Sprite
from enum import Enum

pygame.init()

WINDOW_DIMENSIONS = (WINDOW_WIDTH, WINDOW_HEIGHT) = 640, 480
PART_DIMENSIONS = [15, 15]
START_POS = (START_X, START_Y) = WINDOW_WIDTH/2, WINDOW_HEIGHT/2
VELOCITY = 3

Direction = Enum('Direction', 'up down left right')

class Part(Sprite):
	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = pygame.Surface(PART_DIMENSIONS)
		self.image.fill(pygame.Color(0, 255, 0, 100)) # Green
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def move(self, x, y):
		self.rect.move_ip(x, y)

class Snake(object):
	key_map = {
		pygame.K_UP:    Direction.up,
		pygame.K_DOWN:  Direction.down,
		pygame.K_LEFT:  Direction.left,
		pygame.K_RIGHT: Direction.right
	}

	def __init__(self, x, y, direction):
		self.head = Part(x, y)
		# List of parts must be in order, starting with head
		self.parts = pygame.sprite.OrderedUpdates([self.head])
		self.set_velocity(direction)

	def set_velocity(self, direction):
		if direction == Direction.up:
			self.velocity = (0, -VELOCITY)
		elif direction == Direction.down:
			self.velocity = (0, VELOCITY)
		elif direction == Direction.left:
			self.velocity = (-VELOCITY, 0)
		elif direction == Direction.right:
			self.velocity = (VELOCITY, 0)

	def update(self):
		self.parts.update()
		for part in self.parts:
			part.move(*self.velocity)

	def key_down(self, key):
		self.set_velocity(Snake.key_map[key])

def main():
	screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
	pygame.display.set_caption('Snake')
	background = pygame.Surface(WINDOW_DIMENSIONS)
	background.fill(pygame.Color(0, 0, 0, 100)) # Black
	screen.blit(background, (0, 0))

	clock = pygame.time.Clock()
	snake = Snake(START_X, START_Y, Direction.down)
	sprites = pygame.sprite.Group([])

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
		snake.update()
		snake.parts.update()

		sprites.draw(screen)
		snake.parts.draw(screen)

		pygame.display.flip()

		sprites.clear(screen, background)
		snake.parts.clear(screen, background)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN and event.key in Snake.key_map:
				snake.key_down(event.key)
			elif event.type == pygame.KEYDOWN and event.key in key_map:
				key_map[event.key]()
				# print event

if __name__ == "__main__":
	main()