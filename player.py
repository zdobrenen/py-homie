import os
import sys
import pygame
import math
import glob
import random

from pygame.locals import *

import maps

from loader import load_image


CENTER_X = -1
CENTER_Y = -1


def rot_image(player):
	""" Rotate Player - 
		rotate an image while keeping its center
	"""

	stationary = abs(0.0 - player.speed) <= 0.9

	if (player.dir >= 0 and player.dir < 45) \
	or (player.dir > 315 and player.dir <= 360):
		# UP
		if stationary or player.index >= len(player.U_IMAGES):
			player.index = 0

		player.image_og = player.U_IMAGES[player.index]

	if player.dir > 45 and player.dir < 135:
		# Left
		if stationary or player.index >= len(player.L_IMAGES):
			player.index = 0

		player.image_og = player.L_IMAGES[player.index]

	if player.dir > 135 and player.dir < 225:
		# DOWN
		if stationary or player.index >= len(player.D_IMAGES):
			player.index = 0

		player.image_og = player.D_IMAGES[player.index]

	if player.dir > 225 and player.dir < 315:
		# Right
		if stationary or player.index >= len(player.R_IMAGES):
			player.index = 0

		player.image_og = player.R_IMAGES[player.index]

	player.index += 1

	rot_image = pygame.transform.rotate(player.image_og, 0)
	rot_rect  = rot_image.get_rect(center=player.rect.center)
	return rot_image, rot_rect


def findspawn():
	x = random.randint(0, 9)
	y = random.randint(0, 9)

	while(maps.map_1[y][x] == 5):
		x = random.randint(0, 9)
		y = random.randint(0, 9)

	return x * 1000 + CENTER_X, y * 1000 + CENTER_Y



class Player(pygame.sprite.Sprite):


	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		CENTER_X = int(pygame.display.Info().current_w / 2)
		CENTER_Y = int(pygame.display.Info().current_h / 2)

		self.x = CENTER_X
		self.y = CENTER_Y

		self.L_IMAGES = [load_image('player/{}'.format(f.split('/')[-1]))
				for f in glob.glob('media/player/*.png')
				if 'walkleft' in f
			   ]

		self.R_IMAGES = [load_image('player/{}'.format(f.split('/')[-1]))
				for f in glob.glob('media/player/*.png')
				if 'walkright' in f
			   ]

		self.U_IMAGES = [load_image('player/{}'.format(f.split('/')[-1]))
				for f in glob.glob('media/player/*.png')
				if 'walkup' in f
			   ]

		self.D_IMAGES = [load_image('player/{}'.format(f.split('/')[-1]))
				for f in glob.glob('media/player/*.png')
				if 'walkdown' in f
			   ]


		self.index          = 0
		self.image          = self.U_IMAGES[self.index]
		self.rect           = self.image.get_rect()
		self.image_og       = self.image
		self.screen         = pygame.display.get_surface()
		self.area           = self.screen.get_rect()
		self.rect.topleft   = self.x, self.y
		self.x, self.y      = findspawn()

		self.dir            = 0
		self.speed          = 0.0
		self.maxspeed       = 12.0
		self.minspeed       = -1.85
		self.acceleration   = 0.3
		self.deacceleration = 0.7
		self.softening      = 0.3
		self.steering       = 10.00

		self.coin           = 0
		self.beer           = 0
		self.weed           = 0


	def reset(self):
		self.x = int(pygame.display.Info().current_w / 2)
		self.y = int(pygame.display.Info().current_h / 2)
		
		self.speed = 0.0
		self.dir   = 0
		
		self.image, self.rect = rot_image(self)
		self.rect.topleft = self.x, self.y
		self.x, self.y = findspawn()


	def accelerate(self):
		if self.speed < self.maxspeed:
			self.speed += self.acceleration

		self.image, self.rect = rot_image(self)


	def deaccelerate(self):
		if self.speed > self.minspeed:
			self.speed -= self.deacceleration

		self.image, self.rect = rot_image(self)


	def steerleft(self):
		self.dir = self.dir + self.steering

		if self.dir > 360:
			self.dir = 0

		self.image, self.rect = rot_image(self)


	def steerright(self):
		self.dir = self.dir - self.steering

		if self.dir < 0:
			self.dir = 360

		self.image, self.rect = rot_image(self)


	def soften(self):
		if self.speed > 0:
			self.speed -= self.softening

		if self.speed < 0:
			self.speed += self.softening

		self.image, self.rect = rot_image(self)


	def collect(self, art):
		
		if art == 'coin':
			self.coin += 1

		if art == 'beer':
			self.beer += 1

		if art == 'weed':
			self.weed += 1


	def update(self, cam_x, cam_y):
		self.x = self.x + self.speed * math.cos(math.radians(270-self.dir))
		self.y = self.y + self.speed * math.sin(math.radians(270-self.dir))