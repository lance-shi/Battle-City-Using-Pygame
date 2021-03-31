import pygame
import settings

class Bullet:
	(DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT) = range(4)

	def __init__(self, x, y, direction, speed=5):
		self.direction = direction
		self.speed = speed
		self.image = settings.sprites.subsurface(75*2, 74*2, 3*2, 4*2)
		position = [x, y]

		if self.direction == settings.DIR_UP:
			self.rect = pygame.Rect(position[0] + 11, position[1] - 8, 6, 8)
		elif self.direction == settings.DIR_RIGHT:
			self.image = pygame.transform.rotate(self.image, 270)
			self.rect = pygame.Rect(position[0] + 26, position[1] + 11, 8, 6)
		elif self.direction == settings.DIR_DOWN:
			self.image = pygame.transform.rotate(self.image, 180)
			self.rect = pygame.Rect(position[0] + 11, position[1] + 26, 6, 8)
		elif self.direction == settings.DIR_LEFT:
			self.image = pygame.transform.rotate(self.image, 90)
			self.rect = pygame.Rect(position[0] - 8 , position[1] + 11, 8, 6)

	def update(self):
		if self.direction == settings.DIR_UP:
			self.rect.y -= self.speed
		if self.direction == settings.DIR_LEFT:
			self.rect.x -= self.speed
		if self.direction == settings.DIR_RIGHT:
			self.rect.x += self.speed
		if self.direction == settings.DIR_DOWN:
			self.rect.y += self.speed

	def draw(self):
		settings.screen.blit(self.image, self.rect.topleft)