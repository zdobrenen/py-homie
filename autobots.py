import os
import sys
import math
import random
import pygame

from pygame.locals import *

import maps

from loader import load_image


HALF_TILE = 500
FULL_TILE = 1000
CENTER_W = -1
CENTER_H = -1

TURN_RADIUS = 20

def rot_image(autobot):

	rot_image = pygame.transform.rotate(autobot.image, autobot.dir)
	rot_rect  = rot_image.get_rect(center=autobot.rect.center)
	return rot_image, rot_rect


def cpoints(center, r=TURN_RADIUS, n=4):

	return [(
		int(center[0]+(math.cos(2 * math.pi / n * x) * r)), 
		int(center[1] + (math.sin(2 * math.pi / n * x) * r))
	) for x in xrange(0, n)]



class AutoBot(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image          = load_image('automobiles/{}'.format('car_0.png'), True)
		self.rect           = self.image.get_rect()
		self.image_og       = self.image
		self.screen         = pygame.display.get_surface()

		self.x              = 5
		self.y              = 5

		self.dir            = 0
		self.speed          = 0
		self.maxspeed       = 10.0
		self.minspeed       = -1.85
		self.acceleration   = 0.3
		self.deacceleration = 0.7
		self.softening      = 0.3
		self.steering       = 10.00
		self.wait_turn      = True
		self.generate()


	def generate(self):
		x = random.randint(0, 9)
		y = random.randint(0, 9)

		while (maps.map_1[y][x] == 5):
			x = random.randint(0, 9)
			y = random.randint(0, 9)

		self.x = x * FULL_TILE + HALF_TILE
		self.y = y * FULL_TILE + HALF_TILE

		self.rect.topleft = self.x, self.y


	def grass(self, x, y):

		value = self.screen.get_at((x, y)).g

		return value > 75


	def move(self):
		idx_x, idx_y = int((self.x + CENTER_W) / 1000), int((self.y + CENTER_H) / 1000)

		try:
			tile_type = maps.map_1[idx_y][idx_x]
			tile_rot  = maps.map_1_rot[idx_y][idx_x]
		except IndexError as e:
			pass
		else:
			tile_x = self.x % 1000
			tile_y = self.y % 1000

			if tile_type == maps.turn:
				if tile_rot == 0:
					turn_at = (480, 480)
					
					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = random.choice([270, 180])
						self.wait_turn = False
					else:
						self.wait_turn = True

				if tile_rot == 1:
					turn_at = (480, 512)
					
					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = random.choice([90, 180])
						self.wait_turn = False
					else:
						self.wait_turn = True

				if tile_rot == 2:
					turn_at = (512, 512)
					
					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = random.choice([0, 90])
						self.wait_turn = False
					else:
						self.wait_turn = True

				if tile_rot == 3:
					turn_at = (512, 480)

					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = random.choice([0, 270])
						self.wait_turn = False
					else:
						self.wait_turn = True

			if tile_type == maps.split:
				if tile_rot == 0:
					turn_at = (480, 480)

					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = random.choice([90, 180, 270])
						self.wait_turn = False
					else:
						self.wait_turn = True

				if tile_rot == 1:
					turn_at = (480, 512)

					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = random.choice([0, 90, 180])
						self.wait_turn = False
					else:
						self.wait_turn = True

				if tile_rot == 2:
					turn_at = (512, 512)

					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = random.choice([0, 90, 270])
						self.wait_turn = False
					else:
						self.wait_turn = True

				if tile_rot == 3:
					turn_at = (512, 480)

					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = random.choice([0, 180, 270])
						self.wait_turn = False
					else:
						self.wait_turn = True

			if tile_type == maps.crossing:
				turn_at = (512, 480)

				if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
					self.dir = random.choice([0, 90, 180, 270])
					self.wait_turn = False
				else:
					self.wait_turn = True

			if tile_type == maps.deadend:
				
				if tile_rot == 0:
					turn_at = (512, 225)

					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = 180
						self.wait_turn = False
					else:
						self.wait_turn = True

				if tile_rot == 1:
					turn_at = (255, 480)

					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = 90
						self.wait_turn = False
					else:
						self.wait_turn = True

				if tile_rot == 2:
					turn_at = (512, 750)

					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = 0
						self.wait_turn = False
					else:
						self.wait_turn = True

				if tile_rot == 3:
					turn_at = (730, 480)

					if abs(turn_at[0] - tile_x) <= TURN_RADIUS and abs(turn_at[1] - tile_y) <= TURN_RADIUS and self.wait_turn:
						self.dir = 270
						self.wait_turn = False
					else:
						self.wait_turn = True

			if random.random() < .95:
				self.accelerate()
			else:
				self.deaccelerate()

			self.image, self.rect = rot_image(self)


	def accelerate(self):
		if self.speed < self.maxspeed:
			self.speed += self.acceleration


	def deaccelerate(self):
		if self.speed > self.minspeed:
			self.speed -= self.deacceleration


	def soften(self):
		if self.speed > 0:
			self.speed -= self.softening

		if self.speed < 0:
			self.speed += self.softening


	def update(self, cam_x, cam_y):
		self.move()

		self.x = self.x + self.speed * math.cos(math.radians(270-self.dir))
		self.y = self.y + self.speed * math.sin(math.radians(270-self.dir))

		self.rect.topleft = self.x - cam_x, self.y - cam_y