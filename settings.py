import pygame
from timer import Timer

def init():
	global screen, sprites, bullets, players, enemies, gtimer, sounds
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
	sounds = {}
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

	pygame.mixer.init(44100, -16, 1, 512)
	sounds["start"] = pygame.mixer.Sound("sounds/gamestart.ogg")
	sounds["end"] = pygame.mixer.Sound("sounds/gameover.ogg")
	sounds["score"] = pygame.mixer.Sound("sounds/score.ogg")
	sounds["bg"] = pygame.mixer.Sound("sounds/background.ogg")
	sounds["fire"] = pygame.mixer.Sound("sounds/fire.ogg")
	sounds["bonus"] = pygame.mixer.Sound("sounds/bonus.ogg")
	sounds["explosion"] = pygame.mixer.Sound("sounds/explosion.ogg")
	sounds["brick"] = pygame.mixer.Sound("sounds/brick.ogg")
	sounds["steel"] = pygame.mixer.Sound("sounds/steel.ogg")