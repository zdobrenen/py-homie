import os
import sys
import pygame
import random
import array

from pygame.locals import *

from camera import Camera
from loader import load_image
from maps import Map, map_files, map_tiles, map_1, map_1_rot
from player import Player





def main():
	# initializion
	pygame.init()

	clock   = pygame.time.Clock()
	running = True
	font    = pygame.font.Font(None, 24)

	screen = pygame.display.set_mode(
		(
			pygame.display.Info().current_w,
			pygame.display.Info().current_h
		),
		pygame.FULLSCREEN
	)

	pygame.display.set_caption('BudWatch - The Game')
	pygame.mouse.set_visible(False)

	CENTER_W = int(pygame.display.Info().current_w / 2)
	CENTER_H = int(pygame.display.Info().current_h / 2)

	# new background surface
	background = pygame.Surface(screen.get_size())
	background = background.convert_alpha()
	background.fill((26, 26, 26))

	# initialize game objects
	camera = Camera()
	player = Player()

	# create sprite groups
	map_s     = pygame.sprite.Group()
	player_s  = pygame.sprite.Group()


	for tile in map_tiles:
		map_files.append(load_image('landscape/{}'.format(tile), False))

	for x in range (0, 10):
		for y in range (0, 10):
			map_s.add(Map(map_1[x][y], x * 1000, y * 1000, map_1_rot[x][y]))


	player_s.add(player)


	# enter game loop
	while running:

		# check menu/reset, (keyup event - trigger once)
		for event in pygame.event.get():

			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					running = False
					break

			if event.type == pygame.KEYUP:

				if event.key == pygame.K_q:
					pygame.quit()
					sys.exit(0)

		# check key input, (keydown event - trigger many)
		keys = pygame.key.get_pressed()

		if keys[K_LEFT]:
			player.steerleft()

		if keys[K_RIGHT]:
			player.steerright()

		if keys[K_UP]:
			player.accelerate()
		else:
			player.soften()

		if keys[K_DOWN]:
			player.deaccelerate()


		camera.set_pos(player.x, player.y)

		screen.blit(background, (0, 0))

		map_s.update(camera.x, camera.y)
		map_s.draw(screen)

		player_s.update(camera.x, camera.y)
		player_s.draw(screen)

		pygame.display.flip()
		clock.tick(64)

main()

pygame.quit()
sys.exit(0)