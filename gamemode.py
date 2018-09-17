import pygame
import random

from pygame.locals import *

import maps

from loader import load_image




class GameMode(pygame.sprite.Sprite):

	coin_probability = 0.2
	beer_probability = 0.4
	weed_probability = 0.5


	def __init__(self):
		pass


	def generate_artifacts(self):
		for _ in xrange(200):
			x = random.randint(0, 9)
			y = random.randint(0, 9)

			while (maps.map_1[y][x] == 5):
				x = random.randint(0, 9)
				y = random.randint(0, 9)

			if random.random() < self.coin_probability:
				pass

			if random.random() < self.beer_probability:
				pass

			if random.random() < self.weed_probability:
				pass
			
