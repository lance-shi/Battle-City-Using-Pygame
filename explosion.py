import pygame
import settings

class Explosion:
	def __init__(self, position, tankType=True):
		if tankType:
			self.position = [position[0]-16, position[1]-16]
			images = [
				settings.sprites.subsurface(0, 80*2, 32*2, 32*2),
				settings.sprites.subsurface(32*2, 80*2, 32*2, 32*2),
				settings.sprites.subsurface(64*2, 80*2, 32*2, 32*2)
			]
		else:
			self.position = [position[0]-29, position[1]-29]
			images = [
				settings.sprites.subsurface(0, 80*2, 32*2, 32*2),
				settings.sprites.subsurface(32*2, 80*2, 32*2, 32*2),
			]
		self.active = True
		interval = 100

		self.images = iter(images)
		self.image = next(self.images)
		settings.gtimer.add(interval, lambda :self.update(), len(images) + 1)

	def draw(self):
		settings.screen.blit(self.image, self.position)

	def update(self):
		try:
			self.image = next(self.images)
		except StopIteration:
			self.active = False