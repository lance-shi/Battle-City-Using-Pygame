import pygame
import settings

from bullet import *
from tank import *

class Player(Tank):
	def __init__(self, x, y, type = 0, direction=None, speed=2):
		self.side = settings.SIDE_PLAYER
		Tank.__init__(self, x, y, type, direction, speed)