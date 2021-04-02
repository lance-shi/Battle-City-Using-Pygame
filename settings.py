import pygame
from timer import Timer

def init():
	global screen, sprites, bullets, players, enemies, gtimer
	global DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT
	global SIDE_PLAYER, SIDE_ENEMY, TILE_SIZE
	global tankImages

	(DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT) = range(4)
	(SIDE_PLAYER, SIDE_ENEMY) = range(2)
	TILE_SIZE = 16
	size = width, height = 480, 416
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Battle City")
	sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
	player = sprites.subsurface(0, 0, 13*2, 13*2)
	pygame.display.set_icon(player)
	bullets = []
	players = []
	enemies = []
	gtimer = Timer()

	playerImages = [
		(0, 0, 13*2, 13*2),
		(16*2, 0, 13*2, 13*2)
	]
	enemyImages = [
		(32*2, 0, 13*2, 15*2),
		(48*2, 0, 13*2, 15*2),
		(64*2, 0, 13*2, 15*2),
		(80*2, 0, 13*2, 15*2),
		(32*2, 16*2, 13*2, 15*2),
		(48*2, 16*2, 13*2, 15*2),
		(64*2, 16*2, 13*2, 15*2),
		(80*2, 16*2, 13*2, 15*2)
	]
	tankImages = [playerImages, enemyImages]