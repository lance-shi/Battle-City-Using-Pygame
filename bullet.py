import pygame
import settings

from explosion import *

class Bullet:
	(STATE_REMOVED, STATE_ACTIVE, STATE_EXPLODING) = range(3)

	def __init__(self, x, y, direction, side=None, damage=100, speed=5):
		self.direction = direction
		if side == None:
			side = settings.SIDE_PLAYER
		self.side = side
		self.speed = speed
		self.damage = damage
		self.ownerTank = None
		self.state = self.STATE_ACTIVE
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
		if self.state == self.STATE_EXPLODING:
			if not self.explosion.active:
				self.destroy()
				del self.explosion

		if self.state != self.STATE_ACTIVE:
			return

		if self.direction == settings.DIR_UP:
			self.rect.top -= self.speed
		if self.direction == settings.DIR_LEFT:
			self.rect.left -= self.speed
		if self.direction == settings.DIR_RIGHT:
			self.rect.left += self.speed
		if self.direction == settings.DIR_DOWN:
			self.rect.top += self.speed

		if self.rect.top < 0 or self.rect.left < 0 or self.rect.right > 416 or self.rect.bottom > 416:
			if self.side == settings.SIDE_PLAYER:
				settings.sounds["steel"].play()

			self.explode()
			return

		for bullet in settings.bullets:
			if self.state == self.STATE_ACTIVE and bullet.side != self.side and self.rect.colliderect(bullet.rect):
				self.destroy()
				return

		for player in settings.players:
			if player.state == player.STATE_ALIVE and self.rect.colliderect(player.rect):
				if player.bulletImpact(self.side == settings.SIDE_PLAYER, self.damage, self.ownerTank):
					self.destroy()
					return

		# check for collisions with enemies
		for enemy in settings.enemies:
			if enemy.state == enemy.STATE_ALIVE and self.rect.colliderect(enemy.rect):
				if enemy.bulletImpact(self.side == settings.SIDE_ENEMY, self.damage, self.ownerTank):
					self.destroy()
					return

	def draw(self):
		if self.state == self.STATE_ACTIVE:
			settings.screen.blit(self.image, self.rect.topleft)
		elif self.state == self.STATE_EXPLODING:
			self.explosion.draw()

	def explode(self):
		if self.state != self.STATE_REMOVED:
			self.state = self.STATE_EXPLODING
			self.explosion = Explosion(self.rect.topleft, False)

	def destroy(self):
		self.state = self.STATE_REMOVED