import os
import sys
import pygame
import random
import array

from pygame.locals import *

from artifacts import Coin, Beer, Weed
from autobots import AutoBot
from bounds import Bound, breaking
from camera import Camera
from gamemode import GameMode
from lifeout import LifeOut
from loader import load_image
from maps import Map, map_files, map_tiles, map_1, map_1_rot
from player import Player
from timeout import TimeOut


ARTIFACT_COUNT = 1000
AUTOBOT_COUNT  = 250


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
	camera  = Camera()
	player  = Player()
	bound   = Bound()
	timeout = TimeOut()
	lifeout = LifeOut()

	# create sprite groups
	map_s      = pygame.sprite.Group()
	player_s   = pygame.sprite.Group()
	autobot_s  = pygame.sprite.Group()
	bound_s    = pygame.sprite.Group() 
	coin_s     = pygame.sprite.Group()
	beer_s     = pygame.sprite.Group()
	weed_s     = pygame.sprite.Group()
	timeout_s  = pygame.sprite.Group()
	lifeout_s  = pygame.sprite.Group()


	for tile in map_tiles:
		map_files.append(load_image('landscape/{}'.format(tile), False))

	for x in range (0, 10):
		for y in range (0, 10):
			map_s.add(Map(map_1[x][y], x * 1000, y * 1000, map_1_rot[x][y]))


	player_s.add(player)
	bound_s.add(bound)
	timeout_s.add(timeout)
	lifeout_s.add(lifeout)


	for id in xrange(0, AUTOBOT_COUNT):
		autobot_s.add(AutoBot(id))

	for _ in xrange(0, ARTIFACT_COUNT):
		choice = random.choice(['coin', 'beer', 'weed'])

		if choice == 'coin':
			coin_s.add(Coin())

		elif choice == 'beer':
			beer_s.add(Beer())

		else:
			weed_s.add(Weed())

	


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

				if event.key == pygame.K_p:
					player.reset()


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

		if keys[K_s]:
			player.smoke()

		if keys[K_d]:
			player.drink()

		if keys[K_t]:
			player.timer()


		# align camera view w/ player pos
		camera.set_pos(player.x, player.y)


		# render text data
		text_fps     = font.render('FPS: {}'.format(str(int(clock.get_fps()))), 1, (224, 16, 16))
		textpos_fps  = text_fps.get_rect(centery=25, centerx=60) 

		text_time    = font.render('Time: ' + str(int((player.timeleft / 60)/60)) + ":" + str(int((player.timeleft / 60) % 60)), 1, (224, 16, 16))
		textpos_time = text_fps.get_rect(centery=45, centerx=60)

		text_life    = font.render('Life: {}'.format(str(player.health)), 1, (224, 16, 16))
		textpos_life = text_fps.get_rect(centery=65, centerx=60)

		text_coin    = font.render('Coin: {}'.format(str(player.coin)), 1, (224, 16, 16))
		textpos_coin = text_fps.get_rect(centery=85, centerx=60)

		text_beer    = font.render('Beer: {}'.format(str(player.beer)), 1, (224, 16, 16))
		textpos_beer = text_fps.get_rect(centery=105, centerx=60)

		text_weed    = font.render('Weed: {}'.format(str(player.weed)), 1, (224, 16, 16))
		textpos_weed = text_fps.get_rect(centery=125, centerx=60)

		text_bac    = font.render('BAC: {}'.format(str(player.drunkness)), 1, (224, 16, 16))
		textpos_bac = text_fps.get_rect(centery=145, centerx=60)

		text_thc    = font.render('THC: {}'.format(str(player.stoneness)), 1, (224, 16, 16))
		textpos_thc = text_fps.get_rect(centery=165, centerx=60)


		screen.blit(background, (0, 0))


		# update sprite objects
		map_s.update(camera.x, camera.y)
		map_s.draw(screen)

		player.grass(screen.get_at(((int(CENTER_W-5), int(CENTER_H-5)))).g)

		player_s.update(camera.x, camera.y)
		player_s.draw(screen)

		autobot_s.update(camera.x, camera.y)
		autobot_s.draw(screen)

		coin_s.update(camera.x, camera.y)
		coin_s.draw(screen)

		beer_s.update(camera.x, camera.y)
		beer_s.draw(screen)

		weed_s.update(camera.x, camera.y)
		weed_s.draw(screen)


		# conditional events
		if breaking(player.x + CENTER_W, player.y + CENTER_H):
			bound_s.update()
			bound_s.draw(screen)

		if player.timeleft == 0:
			timeout_s.update()
			timeout_s.draw(screen)
			player.speed = 0

		if player.health == 0:
			lifeout_s.update()
			lifeout_s.draw(screen)
			player.speed = 0

		# check collisions
		if pygame.sprite.spritecollide(player, coin_s, True):
			player.collect('coin')

		if pygame.sprite.spritecollide(player, beer_s, True):
			player.collect('beer')

		if pygame.sprite.spritecollide(player, weed_s, True):
			player.collect('weed')

		if pygame.sprite.spritecollide(player, autobot_s, False):
			player.smacked()

		# blit blit
		screen.blit(text_fps, textpos_fps)
		screen.blit(text_time, textpos_time)
		screen.blit(text_life, textpos_life)
		screen.blit(text_coin, textpos_coin)
		screen.blit(text_beer, textpos_beer)
		screen.blit(text_weed, textpos_weed)
		screen.blit(text_bac, textpos_bac)
		screen.blit(text_thc, textpos_thc)

		# show display
		pygame.display.flip()
		clock.tick(64)

main()

pygame.quit()
sys.exit(0)