import pygame
from bullet import *

class Game:
	(DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT) = range(4)

	def __init__(self):
		size = self.width, self.height = 480, 416

		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption("Battle City")
		self.clock = pygame.time.Clock()
		self.sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
		
		self.player = self.sprites.subsurface(0, 0, 13*2, 13*2)
		pygame.display.set_icon(self.player)
		self.bullets = []
		self.mainLoop()

	def mainLoop(self):
		run = True
		playerRect = pygame.Rect(100, 300, 13*2, 13*2)
		tankSpeed = 2
		while run:
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						newBullet = Bullet(self.screen, self.sprites, playerRect.x, playerRect.y, self.DIR_UP)
						self.bullets.append(newBullet)

			for bullet in self.bullets:
				bullet.update()

			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_a] and playerRect.x - tankSpeed > 0:
				playerRect.x -= tankSpeed
			if keys_pressed[pygame.K_s] and playerRect.y + playerRect.height + tankSpeed < self.height:
				playerRect.y += tankSpeed
			if keys_pressed[pygame.K_d] and playerRect.x + playerRect.width + tankSpeed < self.width:
				playerRect.x += tankSpeed
			if keys_pressed[pygame.K_w] and playerRect.y - tankSpeed > 0:
				playerRect.y -= tankSpeed
			self.draw(playerRect)
				
		pygame.quit()

	def draw(self, playerRect):
		self.screen.fill([0, 0, 0])
		self.screen.blit(self.player, playerRect.topleft)
		for bullet in self.bullets:
			bullet.draw()
		pygame.display.update()