import os
import sys
import pygame
import math
import glob

import maps

from pygame.locals import *

from loader import load_image



def rot_center(image, rect, angle):
	""" Rotate Player - 
		rotate an image while keeping its center
	"""
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect  = rot_image.get_rect(center=rect.center)
	return rot_image, rot_rect


class Player(pygame.sprite.Sprite):


	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		CENTER_X = int(pygame.display.Info().current_w / 2)
		CENTER_Y = int(pygame.display.Info().current_h / 2)

		self.x = CENTER_X
		self.y = CENTER_Y

		self.L_IMAGES = [load_image('blocky/{}'.format(f.split('/')[-1]))
				for f in glob.glob('media/blocky/*.png')
				if 'walkleft' in f
			   ]

		self.R_IMAGES = [load_image('blocky/{}'.format(f.split('/')[-1]))
				for f in glob.glob('media/blocky/*.png')
				if 'walkright' in f
			   ]

		self.U_IMAGES = [load_image('blocky/{}'.format(f.split('/')[-1]))
				for f in glob.glob('media/blocky/*.png')
				if 'walkup' in f
			   ]

		self.D_IMAGES = [load_image('blocky/{}'.format(f.split('/')[-1]))
				for f in glob.glob('media/blocky/*.png')
				if 'walkdown' in f
			   ]

		self.image        = self.U_IMAGES[0]
		self.rect         = self.image.get_rect()
		self.image_og     = self.image
		self.screen       = pygame.display.get_surface()
		self.area         = self.screen.get_rect()
		self.rect.topleft = self.x, self.y

		self.dir            = 0
		self.speed          = 0.0
		self.maxspeed       = 20.5
		self.minspeed       = -1.85
		self.acceleration   = 0.6
		self.deacceleration = 0.35
		self.softening      = 0.04
		self.steering       = 2.60


	def accelerate(self):
		if self.speed < self.maxspeed:
			self.speed += self.acceleration


	def deaccelerate(self):
		if self.speed > self.minspeed:
			self.speed -= self.deacceleration


	def steerleft(self):
		self.dir = self.dir + self.steering

		if self.dir > 360:
			self.dir = 0

		self.image, self.rect = rot_center(self.image_og, self.rect, self.dir)


	def steerright(self):
		self.dir = self.dir - self.steering

		if self.dir < 0:
			self.dir = 360

		self.image, self.rect = rot_center(self.image_og, self.rect, self.dir)


	def soften(self):
		if self.speed > 0:
			self.speed -= self.softening

		if self.speed < 0:
			self.speed += self.softening


	def update(self, last_x, last_y):
		self.x = self.x + self.speed * math.cos(math.radians(270-self.dir))
		self.y = self.y + self.speed * math.sin(math.radians(270-self.dir))