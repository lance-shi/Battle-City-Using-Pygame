import pygame
import settings

from bullet import *
from level import *
from explosion import *

class Tank:
	MAX_LENGTH = 416
	(STATE_SPAWNING, STATE_DEAD, STATE_ALIVE, STATE_EXPLODING) = range(4)

	def __init__(self, level, position, type = 0, direction=None, speed=2):
		self.direction = direction if direction != None else settings.DIR_UP
		self.speed = speed
		self.rect = pygame.Rect(position, (26, 26))
		self.type = type
		self.health = 100

		self.image = settings.sprites.subsurface(settings.tankImages[self.side][self.type])
		self.imageUp = self.image;
		self.imageLeft = pygame.transform.rotate(self.image, 90)
		self.imageDown = pygame.transform.rotate(self.image, 180)
		self.imageRight = pygame.transform.rotate(self.image, 270)
		self.state = self.STATE_SPAWNING

		self.spawnImages = [
			settings.sprites.subsurface(32*2, 48*2, 16*2, 16*2),
			settings.sprites.subsurface(48*2, 48*2, 16*2, 16*2)
		]
		self.spawnImage = self.spawnImages[0]
		self.spawnIndex = 0

		self.timerUuidSpawn = settings.gtimer.add(100, lambda :self.toggleSpawnImage())
		self.timerUuidSpawnEnd = settings.gtimer.add(1000, lambda :self.endSpawning())

		self.rotate(self.direction, False)

	def rotate(self, direction, fixPosition = True):
		""" Rotate tank
		rotate, update image and correct position
		"""
		self.direction = direction

		if direction == settings.DIR_UP:
			self.image = self.imageUp
		elif direction == settings.DIR_RIGHT:
			self.image = self.imageRight
		elif direction == settings.DIR_DOWN:
			self.image = self.imageDown
		elif direction == settings.DIR_LEFT:
			self.image = self.imageLeft

		if fixPosition:
			new_x = self.nearest(self.rect.left, 8) + 3
			new_y = self.nearest(self.rect.top, 8) + 3

			if (abs(self.rect.left - new_x) < 5):
				self.rect.left = new_x

			if (abs(self.rect.top - new_y) < 5):
				self.rect.top = new_y

	def nearest(self, num, base):
		""" Round number to nearest divisible """
		return int(round(num / (base * 1.0)) * base)

	def turnAround(self):
		""" Turn tank into opposite direction """
		if self.direction in (settings.DIR_UP, settings.DIR_RIGHT):
			self.rotate(self.direction + 2, False)
		else:
			self.rotate(self.direction - 2, False)

	def fire(self):
		if self.state != self.STATE_ALIVE:
			settings.gtimer.destroy(self.timerUuidFire)
			return 

		newBullet = Bullet(self.rect.left, self.rect.top, self.direction, self.side)
		newBullet.ownerTank = self
		settings.bullets.append(newBullet)

	def update(self):
		if self.state == self.STATE_EXPLODING:
			if not self.explosion.active:
				self.state = self.STATE_DEAD
				del self.explosion

	def draw(self):
		if self.state == self.STATE_ALIVE:
			settings.screen.blit(self.image, self.rect.topleft)
		elif self.state == self.STATE_EXPLODING:
			self.explosion.draw()
		elif self.state == self.STATE_SPAWNING:
			settings.screen.blit(self.spawnImage, self.rect.topleft)

	def explode(self):
		if self.state != self.STATE_DEAD:
			self.state = self.STATE_EXPLODING
			self.explosion = Explosion(self.rect.topleft)

	def bulletImpact(self, friendlyFire=False, damage=100, ownerTank=None):
		if not friendlyFire:
			self.health -= damage
			if self.health < 1:
				if self.side == settings.SIDE_ENEMY:
					settings.sounds["explosion"].play()
				self.explode()
			else:
				if self.side == settings.SIDE_ENEMY:
					settings.sounds["steel"].play()
			return True

		if self.side == settings.SIDE_ENEMY:
			return False
		else:
			return True

	def endSpawning(self):
		self.state = self.STATE_ALIVE
		settings.gtimer.destroy(self.timerUuidSpawnEnd)

	def toggleSpawnImage(self):
		if self.state != self.STATE_SPAWNING:
			settings.gtimer.destroy(self.timerUuidSpawn)
			return

		self.spawnIndex += 1
		if self.spawnIndex >= len(self.spawnImages):
			self.spawnIndex = 0
		self.spawnImage = self.spawnImages[self.spawnIndex]
	
