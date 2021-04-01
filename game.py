import pygame
import settings
from bullet import *
from tank import *
from player import *
from enemy import *

class Game:
	def __init__(self):
		self.mainLoop()

	def mainLoop(self):
		run = True
		clock = pygame.time.Clock()
		playerTank = Player(100, 300)
		enemyTank = Enemy(0, 0)
		settings.players.append(playerTank)
		settings.enemies.append(enemyTank)
		while run:
			clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						playerTank.fire()

			for bullet in settings.bullets:
				bullet.update()

			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_a]:
				playerTank.move(settings.DIR_LEFT)
			if keys_pressed[pygame.K_s]:
				playerTank.move(settings.DIR_DOWN)
			if keys_pressed[pygame.K_d]:
				playerTank.move(settings.DIR_RIGHT)
			if keys_pressed[pygame.K_w]:
				playerTank.move(settings.DIR_UP)
			
			self.draw()
		pygame.quit()

	def draw(self):
		settings.screen.fill([0, 0, 0])
		for player in settings.players:
			player.draw()
		for enemy in settings.enemies:
			enemy.draw()
		for bullet in settings.bullets:
			bullet.draw()
		pygame.display.update()