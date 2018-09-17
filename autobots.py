import os
import sys
import math
import random
import pygame

from pygame.locals import *

import maps

from loader import load_image

BOUND_MIN = 0
BOUND_MAX = 1000 * 10

HALF_TILE = 500
FULL_TILE = 1000
CENTER_W = -1
CENTER_H = -1

TURN_RADIUS = 150


def rot_image(autobot):

	rot_image = pygame.transform.rotate(autobot.image_og, autobot.dir)
	rot_rect  = rot_image.get_rect(center=autobot.rect.center)
	return rot_image, rot_rect


def cpoints(center, r=TURN_RADIUS, n=4):

	return [(
		int(center[0]+(math.cos(2 * math.pi / n * x) * r)), 
		int(center[1] + (math.sin(2 * math.pi / n * x) * r))
	) for x in xrange(0, n)]



class AutoBot(pygame.sprite.Sprite):

	def __init__(self, id):
		pygame.sprite.Sprite.__init__(self)

		self.id             = id
		
		self.image          = load_image('automobiles/{}'.format('car_0.png'), True)
		self.rect           = self.image.get_rect()
		self.image_og       = self.image
		self.screen         = pygame.display.get_surface()

		self.x              = 5
		self.y              = 5

		self.dir            = 0
		self.dir_og         = self.dir
		self.speed          = 0
		self.maxspeed       = 20.0
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

		while (maps.map_1[y][x] == 5) or (maps.map_1[y][x]):
			x = random.randint(0, 9)
			y = random.randint(0, 9)

		self.x = x * FULL_TILE + HALF_TILE
		self.y = y * FULL_TILE + HALF_TILE

		self.rect.topleft = self.x, self.y


	def inbounds(self):
		if self.x < BOUND_MIN or self.x > BOUND_MAX:
			return False

		if self.y < BOUND_MIN or self.y > BOUND_MAX:
			return False

		return True


	def move(self):

		if not self.inbounds():
			self.generate()

		idx_x, idx_y = int((self.x + CENTER_W) / 1000), int((self.y + CENTER_H) / 1000)

		try:
			tile_type = maps.map_1[idx_y][idx_x]
			tile_rot  = maps.map_1_rot[idx_y][idx_x]
		except IndexError as e:
			pass
		else:
			tile_x = int(self.x % 1000)
			tile_y = int(self.y % 1000)


			if tile_type == maps.turn:
				if tile_rot == 0:
					turn_at = (480, 480)
					options = [90, 180]
					
					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = random.choice([d for d in options if d != (self.dir + 180) % 360])
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_y <= 300:
						self.generate()

					if tile_x >= 700:
						self.generate()

				if tile_rot == 1:
					turn_at = (480, 512)
					options = [270, 180]

					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = random.choice([d for d in options if d != (self.dir + 180) % 360])
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_y <= 300:
						self.generate()

					if tile_x <= 300:
						self.generate()

				if tile_rot == 2:
					turn_at = (512, 512)
					options = [0, 270]

					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = random.choice([d for d in options if d != (self.dir + 180) % 360])
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_y >= 700:
						self.generate()

					if tile_x <= 300:
						self.generate()

				if tile_rot == 3:
					turn_at = (512, 480)
					options = [0, 90]

					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = random.choice([d for d in options if d != (self.dir + 180) % 360])
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_y >= 700:
						self.generate()

					if tile_x >= 700:
						self.generate()

			if tile_type == maps.split:
				if tile_rot == 0:
					turn_at = (485, 485)
					options = [90, 180, 270]

					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = random.choice([d for d in options if d != (self.dir + 180) % 360])
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_y <= 300:
						self.generate()

				if tile_rot == 1:
					turn_at = (480, 512)
					options = [0, 270, 180]

					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = random.choice([d for d in options if d != (self.dir + 180) % 360])
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_x <= 300:
						self.generate()

				if tile_rot == 2:
					turn_at = (510, 520)
					options = [0, 90, 270]

					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = random.choice([d for d in options if d != (self.dir + 180) % 360])
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_y >= 700:
						self.generate()

				if tile_rot == 3:
					turn_at = (512, 480)
					options = [0, 180, 90]

					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = random.choice([d for d in options if d != (self.dir + 180) % 360])
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_x >= 700:
						self.generate()
						

			if tile_type == maps.crossing:
				turn_at = (512, 480)
				options = [0, 90, 180, 270]

				dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

				if dist <= TURN_RADIUS:

					if self.wait_turn:
						self.dir = random.choice([d for d in options if d != (self.dir + 180) % 360])
						self.wait_turn = False

						self.image, self.rect = rot_image(self)
				else:
					self.wait_turn = True

			if tile_type == maps.deadend:
				
				if tile_rot == 0:
					turn_at = (512, 225)
					options = [180]

					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = options[0]
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_y <= 60:
						self.generate()

				if tile_rot == 1:
					turn_at = (255, 480)
					options = [270]

					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = options[0]
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_x <= 60:
						self.generate()

				if tile_rot == 2:
					turn_at = (512, 750)
					options = [0]

					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = options[0]
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_y >= 940:
						self.generate()

				if tile_rot == 3:
					turn_at = (730, 480)
					options = [90]

					dist = int(math.sqrt(int(abs(turn_at[0] - tile_x))**2 + int(abs(turn_at[1] - tile_y))**2))

					if dist <= TURN_RADIUS:

						if self.wait_turn:
							self.dir = options[0]
							self.wait_turn = False

							self.image, self.rect = rot_image(self)
					else:
						self.wait_turn = True

					if tile_x >= 940:
						self.generate()

			if random.random() < .95:
				self.accelerate()
			else:
				self.deaccelerate()


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
		self.x = self.x + self.speed * math.cos(math.radians(270-self.dir))
		self.y = self.y + self.speed * math.sin(math.radians(270-self.dir))

		self.move()
		
		self.rect.topleft = self.x - cam_x, self.y - cam_y