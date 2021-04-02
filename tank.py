import pygame
import settings

from bullet import *
from level import *

class Tank:
	MAX_LENGTH = 416

	def __init__(self, level, position, type = 0, direction=None, speed=2):
		self.direction = direction if direction != None else settings.DIR_UP
		self.speed = speed
		self.rect = pygame.Rect(position, (26, 26))
		self.type = type

		self.image = settings.sprites.subsurface(settings.tankImages[self.side][self.type])
		self.image_up = self.image;
		self.image_left = pygame.transform.rotate(self.image, 90)
		self.image_down = pygame.transform.rotate(self.image, 180)
		self.image_right = pygame.transform.rotate(self.image, 270)

		self.rotate(self.direction, False)

	def move(self, direction):
		if self.direction != direction:
			self.rotate(direction)

		if direction == settings.DIR_UP:
			new_position = [self.rect.left, self.rect.top - self.speed]
			if new_position[1] < 0:
				return
		elif direction == settings.DIR_RIGHT:
			new_position = [self.rect.left + self.speed, self.rect.top]
			if new_position[0] > (416 - 26):
				return
		elif direction == settings.DIR_DOWN:
			new_position = [self.rect.left, self.rect.top + self.speed]
			if new_position[1] > (416 - 26):
				return
		elif direction == settings.DIR_LEFT:
			new_position = [self.rect.left - self.speed, self.rect.top]
			if new_position[0] < 0:
				return

		player_rect = pygame.Rect(new_position, [26, 26])
		self.rect.topleft = (new_position[0], new_position[1])

	def rotate(self, direction, fix_position = True):
		""" Rotate tank
		rotate, update image and correct position
		"""
		self.direction = direction

		if direction == settings.DIR_UP:
			self.image = self.image_up
		elif direction == settings.DIR_RIGHT:
			self.image = self.image_right
		elif direction == settings.DIR_DOWN:
			self.image = self.image_down
		elif direction == settings.DIR_LEFT:
			self.image = self.image_left

		if fix_position:
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
		if self.direction in (self.DIR_UP, self.DIR_RIGHT):
			self.rotate(self.direction + 2, False)
		else:
			self.rotate(self.direction - 2, False)

	def fire(self):
		newBullet = Bullet(self.rect.left, self.rect.top, self.direction, self.side)
		settings.bullets.append(newBullet)

	def draw(self):
		settings.screen.blit(self.image, self.rect.topleft)