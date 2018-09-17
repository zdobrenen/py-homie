import pygame
import random
import math

from pygame.locals import *

import maps

from loader import load_image


HALF_TILE = 500
FULL_TILE = 1000



class Coin(pygame.sprite.Sprite):

	

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image('artifacts/{}'.format('coin.png'))
		self.rect  = self.image.get_rect()

		self.x     = 5
		self.y     = 5

		self.generate()


	def generate(self):
		x = random.randint(0, 9)
		y = random.randint(0, 9)

		while (maps.map_1[y][x] == 5):
			x = random.randint(0, 9)
			y = random.randint(0, 9)


		self.x = x * FULL_TILE + random.randint(HALF_TILE / 2, HALF_TILE)
		self.y = y * FULL_TILE + random.randint(HALF_TILE / 2, HALF_TILE)

		r = 150 * math.sqrt(random.random())
		theta = random.random() * 2 * math.pi

		self.x = self.x + (r * math.cos(theta))
		self.y = self.y + (r * math.sin(theta))

		self.rect.topleft = self.x, self.y


	def update(self, cam_x, cam_y):
		self.rect.topleft = self.x - cam_x, self.y - cam_y



class Beer(pygame.sprite.Sprite):

	

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image('artifacts/{}'.format('beer.png'))
		self.rect  = self.image.get_rect()

		self.x     = 5
		self.y     = 5

		self.generate()


	def generate(self):
		x = random.randint(0, 9)
		y = random.randint(0, 9)

		while (maps.map_1[y][x] == 5):
			x = random.randint(0, 9)
			y = random.randint(0, 9)

		self.x = x * FULL_TILE + random.randint(HALF_TILE / 2, HALF_TILE)
		self.y = y * FULL_TILE + random.randint(HALF_TILE / 2, HALF_TILE)

		r = 150 * math.sqrt(random.random())
		theta = random.random() * 2 * math.pi

		self.x = self.x + (r * math.cos(theta))
		self.y = self.y + (r * math.sin(theta))

		self.rect.topleft = self.x, self.y


	def update(self, cam_x, cam_y):
		self.rect.topleft = self.x - cam_x, self.y - cam_y



class Weed(pygame.sprite.Sprite):

	

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image('artifacts/{}'.format('weed.png'))
		self.rect  = self.image.get_rect()

		self.x     = 5
		self.y     = 5

		self.generate()


	def generate(self):
		x = random.randint(0, 9)
		y = random.randint(0, 9)

		while (maps.map_1[y][x] == 5):
			x = random.randint(0, 9)
			y = random.randint(0, 9)

		self.x = x * FULL_TILE + random.randint(HALF_TILE / 2, HALF_TILE)
		self.y = y * FULL_TILE + random.randint(HALF_TILE / 2, HALF_TILE)


		r = 150 * math.sqrt(random.random())
		theta = random.random() * 2 * math.pi

		self.x = self.x + (r * math.cos(theta))
		self.y = self.y + (r * math.sin(theta))

		self.rect.topleft = self.x, self.y


	def update(self, cam_x, cam_y):
		self.rect.topleft = self.x - cam_x, self.y - cam_y