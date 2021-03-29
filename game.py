import pygame

class Game:
	def __init__(self):
		size = self.width, self.height = 480, 416

		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption("Battle City")
		self.clock = pygame.time.Clock()
		self.sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
		
		self.player = self.sprites.subsurface(0, 0, 13*2, 13*2)
		pygame.display.set_icon(self.player)
		self.mainLoop()

	def mainLoop(self):
		run = True
		playerRect = pygame.Rect(100, 300, 13*2, 13*2)
		while run:
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_a] and playerRect.x - 5 > 0:
				playerRect.x -= 5
			if keys_pressed[pygame.K_s] and playerRect.y + playerRect.height + 5 < self.height:
				playerRect.y += 5
			if keys_pressed[pygame.K_d] and playerRect.x + playerRect.width + 5 < self.width:
				playerRect.x += 5
			if keys_pressed[pygame.K_w] and playerRect.y - 5 > 0:
				playerRect.y -= 5
			self.draw(playerRect)

		pygame.quit()

	def draw(self, playerRect):
		self.screen.fill([0, 0, 0])
		self.screen.blit(self.player, (playerRect.x, playerRect.y))
		pygame.display.update()