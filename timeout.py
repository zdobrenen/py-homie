import pygame

from pygame.locals import *

from loader import load_image


NOTE_HALF_X = 212
NOTE_HALF_Y = 112

#Alert body.
class TimeOut(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('alerts/{}'.format('timeout.png'))
        self.rect = self.image.get_rect()
        self.x =  int(pygame.display.Info().current_w /2) - NOTE_HALF_X
        self.y =  int(pygame.display.Info().current_h /2) - NOTE_HALF_Y
        self.rect.topleft = self.x, self.y