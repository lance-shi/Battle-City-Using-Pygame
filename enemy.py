import pygame
import settings

from bullet import *
from tank import *

class Enemy(Tank):
	def __init__(self, level, position=None, type = 0, direction=None, speed=2):
		self.side = settings.SIDE_ENEMY
		direction = settings.DIR_DOWN
		if position == None:
			position = (0, 0)
		Tank.__init__(self, level, position, type, direction, speed)