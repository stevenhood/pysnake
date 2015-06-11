#! /usr/bin/env python

# Snake
# version 0.1
# Steven Hood

# Python 2.7.3
# Pygame 1.9.1 (release)
# enum34 for IntEnum

import sys
import pygame
from pygame.sprite import Sprite
from enum import IntEnum

pygame.init()

WINDOW_DIMENSIONS = (WINDOW_WIDTH, WINDOW_HEIGHT) = 640, 480
PART_DIMENSIONS = [15, 15]
START_POS = (START_X, START_Y) = WINDOW_WIDTH/2, WINDOW_HEIGHT/2
VELOCITY = 15

class Direction(IntEnum):
	up    = -1
	down  = 1
	left  = -2
	right = 2

class Part(Sprite):
	topid = 0
	def __init__(self, x, y, color):
		Sprite.__init__(self)
		self.image = pygame.Surface(PART_DIMENSIONS)
		self.image.fill(color) # Green
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.id = Part.topid
		Part.topid += 1

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
		self.head = Part(x, y, pygame.Color(0, 255, 0, 100))
		# List of parts must be in order, starting with head
		self.parts = pygame.sprite.OrderedUpdates([self.head])
		# Testing: Add a few parts
		for i in range(1, 10):
			self.parts.add(Part(x, y - (PART_DIMENSIONS[1] * i), pygame.Color(255, 0, 0, 100)))
		self.direction = direction
		self.set_velocity(direction)

	def set_velocity(self, direction):
		# Do not allow changing to the opposite direction
		if self.direction + direction == 0:
			return
		self.direction = direction
		if direction == Direction.up:
			self.velocity = (0, -VELOCITY)
		elif direction == Direction.down:
			self.velocity = (0, VELOCITY)
		elif direction == Direction.left:
			self.velocity = (-VELOCITY, 0)
		elif direction == Direction.right:
			self.velocity = (VELOCITY, 0)

	def update(self):
		self.head.move(*self.velocity)
		previous = self.head
		for part in self.parts:
			# Head position is updated below
			if part == self.head:
				print "head"
				continue
			# Set each part to the position of the one in front of it
			part.rect.center = previous.rect.center
			print part.id, "move to", previous.id
			previous = part

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
		# Unnecessary: Part objects don't have an update method
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