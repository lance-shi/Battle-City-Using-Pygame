import pygame

def init():
	global screen, sprites, bullets, players
	global DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT

	(DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT) = range(4)
	size = width, height = 480, 416
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Battle City")
	sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
	player = sprites.subsurface(0, 0, 13*2, 13*2)
	pygame.display.set_icon(player)
	bullets = []
	players = []