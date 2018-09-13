import pygame

from loader import load_image

from pygame.locals import *

BOUND_MIN = 0
BOUND_MAX = 1000 * 10
NOTE_HALF_X = 211
NOTE_HALF_Y = 112


def breaking(x, y):
	if x < BOUND_MIN or x > BOUND_MAX:
		return True

	if y < BOUND_MIN or y > BOUND_MAX:
		return True

	return False


class Bound(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image('alerts/{}'.format('bounds.png'))
		self.rect = self.image.get_rect()
		self.x = int(pygame.display.Info().current_w / 2) - NOTE_HALF_X
		self.y = int(pygame.display.Info().current_h / 2) - NOTE_HALF_Y
		self.rect.topleft = self.x, self.y