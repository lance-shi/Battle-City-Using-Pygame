import pygame
import settings

from bullet import *
from tank import *

class Player(Tank):
	def __init__(self, level, position, type = 0, direction=None, speed=2):
		self.side = settings.SIDE_PLAYER
		Tank.__init__(self, level, position, type, direction, speed)

	def move(self, direction):
		if self.direction != direction:
			self.rotate(direction)

		if direction == settings.DIR_UP:
			newPosition = [self.rect.left, self.rect.top - self.speed]
			if newPosition[1] < 0:
				return
		elif direction == settings.DIR_RIGHT:
			newPosition = [self.rect.left + self.speed, self.rect.top]
			if newPosition[0] > (416 - 26):
				return
		elif direction == settings.DIR_DOWN:
			newPosition = [self.rect.left, self.rect.top + self.speed]
			if newPosition[1] > (416 - 26):
				return
		elif direction == settings.DIR_LEFT:
			newPosition = [self.rect.left - self.speed, self.rect.top]
			if newPosition[0] < 0:
				return

		playerRect = pygame.Rect(newPosition, [26, 26])

		# collisions with other players
		for player in settings.players:
			if player != self and playerRect.colliderect(player.rect) == True:
				return

		# collisions with enemies
		for enemy in settings.enemies:
			if playerRect.colliderect(enemy.rect) == True:
				return

		self.rect.topleft = (newPosition[0], newPosition[1])