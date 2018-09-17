import os
import sys
import pygame

from pygame.locals import *


def load_image(file, transparent=True):
	fullname = os.path.join('media', file)

	image = pygame.image.load(fullname)

	if transparent:
		image = image.convert()
		colorkey = image.get_at((0, 0))

		image.set_colorkey(colorkey, pygame.RLEACCEL)
	else:
		image = image.convert_alpha()

	return image