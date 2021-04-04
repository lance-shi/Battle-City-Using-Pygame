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
		playerTank = Player(None, (100, 300))
		self.maxEnemies = 4
		settings.players.append(playerTank)
		settings.gtimer.add(3000, lambda :self.createEnemy())
		while run:
			timePassed = clock.tick(60)
			self.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE and playerTank.state == playerTank.STATE_ALIVE:
						settings.sounds["fire"].play()
						playerTank.fire()

			keys_pressed = pygame.key.get_pressed()
			if playerTank.state == playerTank.STATE_ALIVE:
				if keys_pressed[pygame.K_a]:
					playerTank.move(settings.DIR_LEFT)
				if keys_pressed[pygame.K_s]:
					playerTank.move(settings.DIR_DOWN)
				if keys_pressed[pygame.K_d]:
					playerTank.move(settings.DIR_RIGHT)
				if keys_pressed[pygame.K_w]:
					playerTank.move(settings.DIR_UP)
			
			settings.gtimer.update(timePassed)
			self.draw()
		pygame.quit()

	def createEnemy(self):
		if len(settings.enemies) >= self.maxEnemies:
			return

		enemy = Enemy(None)
		settings.enemies.append(enemy)

	def update(self):
		for bullet in settings.bullets:
			if bullet.state == bullet.STATE_REMOVED:
				settings.bullets.remove(bullet)
			bullet.update()
		for player in settings.players:
			player.update()
		for enemy in settings.enemies:
			if enemy.state == enemy.STATE_DEAD:
				settings.enemies.remove(enemy)
			enemy.update()
			
	def draw(self):
		settings.screen.fill([0, 0, 0])
		for player in settings.players:
			player.draw()
		for enemy in settings.enemies:
			enemy.draw()
		for bullet in settings.bullets:
			bullet.draw()
		pygame.display.update()