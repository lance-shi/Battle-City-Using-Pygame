import pygame
import settings
import random

from bullet import *
from tank import *

class Enemy(Tank):
	def __init__(self, level, position=None, type = 0, direction=None, speed=2):
		self.side = settings.SIDE_ENEMY
		direction = settings.DIR_DOWN
		if position == None:
			position = (0, 0)
		Tank.__init__(self, level, position, type, direction, speed)
		self.path = self.generatePath(True)
		self.timerUuidFire = settings.gtimer.add(1000, lambda :self.fire())

	def move(self):
		try: 
			newPosition = next(self.path)
		except StopIteration:
			self.path = self.generatePath(False, True)
			newPosition = next(self.path)

		if self.direction == settings.DIR_UP:
			if newPosition[1] < 0:
				self.path = self.generatePath(True, True)
				return
		elif self.direction == settings.DIR_RIGHT:
			if newPosition[0] > (416 - 26):
				self.path = self.generatePath(True, True)
				return
		elif self.direction == settings.DIR_DOWN:
			if newPosition[1] > (416 - 26):
				self.path = self.generatePath(True, True)
				return
		elif self.direction == settings.DIR_LEFT:
			if newPosition[0] < 0:
				self.path = self.generatePath(True, True)
				return

		#To be honest, I feel like this should be 32 instead of 26
		newRect = pygame.Rect(newPosition, [26, 26])
		
		# collisions with other enemies
		for enemy in settings.enemies:
			if enemy != self and newRect.colliderect(enemy.rect):
				self.turnAround()
				self.path = self.generatePath(self.direction)
				return

		# collisions with players
		for player in settings.players:
			if newRect.colliderect(player.rect):
				self.turnAround()
				self.path = self.generatePath(self.direction)
				return

		self.rect.topleft = newRect.topleft

	def update(self):
		Tank.update(self)
		if self.state == self.STATE_ALIVE:
			self.move()

	def generatePath(self, hasDirection=False, fixDirection=False):
		allDirections = [settings.DIR_UP, settings.DIR_RIGHT, settings.DIR_DOWN, settings.DIR_LEFT]

		if self.direction in [settings.DIR_UP, settings.DIR_RIGHT]:
			oppositeDirection = self.direction + 2
		else:
			oppositeDirection = self.direction - 2

		directions = allDirections
		random.shuffle(directions)
		directions.remove(oppositeDirection)
		directions.append(oppositeDirection)

		if hasDirection:
			directions.remove(self.direction)
			directions.insert(0, self.direction)

		# convert into units
		x = int(round(self.rect.left / 16))
		y = int(round(self.rect.top / 16))

		newDirection = None

		for direction in directions:
			if direction == settings.DIR_UP and y > 1:
				newPosRect = self.rect.move(0, -8)
				newDirection = direction
				break
			elif direction == settings.DIR_RIGHT and x < 24: 
			#The max width and height here should be 26, 2 units is the width and height of tank itself
				newPosRect = self.rect.move(8, 0)
				newDirection = direction
				break
			elif direction == settings.DIR_DOWN and y < 24:
				newPosRect = self.rect.move(0, 8)
				newDirection = direction
				break
			elif direction == settings.DIR_LEFT and x > 1:
				newPosRect = self.rect.move(-8, 0)
				newDirection = direction
				break

		if newDirection == None:
			newDirection = oppositeDirection
			print("nav izejas. griezhamies")
		"""This should never happen. Can only happen if the enemy is born in an area where 
		surroundings are all obstacles.
		Why do I print this sentence? Because it sounds cool and seems every other battle city
		python program is printing this in this situation  -Lance                """

		if newDirection != self.direction:
			self.rotate(newDirection, fixDirection)

		positions = []

		x = self.rect.left
		y = self.rect.top

		pixels = self.nearest(random.randint(1, 12) * 32, 32) + 3

		if newDirection == settings.DIR_UP:
			for px in range(0, pixels, self.speed):
				positions.append([x, y-px])
		elif newDirection == settings.DIR_RIGHT:
			for px in range(0, pixels, self.speed):
				positions.append([x+px, y])
		elif newDirection == settings.DIR_DOWN:
			for px in range(0, pixels, self.speed):
				positions.append([x, y+px])
		elif newDirection == settings.DIR_LEFT:
			for px in range(0, pixels, self.speed):
				positions.append([x-px, y])

		return iter(positions)