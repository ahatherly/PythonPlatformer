import pygame
from Tiles import WHITE, BLACK, TRANSCOLOUR

class Menus:

	exited = False

	def __init__(self, screen):
		self.hugefont = pygame.font.Font("./Assets/NemoyBold.ttf", 100)
		self.bigfont = pygame.font.Font("./Assets/NemoyBold.ttf", 100)
		self.font = pygame.font.Font("./Assets/NemoyBold.ttf", 60)
		self.screen = screen
	
	def startMenu(self):
		started = False
		screen = self.screen
		clock = pygame.time.Clock()
		backGround = Background()
		text = self.bigfont.render("Alien Escape!", True, (0, 128, 0))
		text2 = self.font.render("Press Space to start!", True, (0, 128, 0))

		alien = Alien()
		all_sprites_list = pygame.sprite.Group()
		all_sprites_list.add(alien)

		while not self.exited and not started:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.exited = True

			if pygame.key.get_pressed()[pygame.K_ESCAPE]:
				self.exited = True
			elif pygame.key.get_pressed()[pygame.K_SPACE]:
				started = True

			####### Paint the screen ###########
			screen.fill(WHITE)
			screen.blit(backGround.image, backGround.rect)
			all_sprites_list.update()
			all_sprites_list.draw(screen)
			screen.blit(text,(220, 200))
			screen.blit(text2,(220, 320))

			pygame.display.flip()

			# Limit to 30 frames per second
			clock.tick(30)

	def messageScreen(self, message):
		started = False
		screen = self.screen
		clock = pygame.time.Clock()
		text = self.hugefont.render(message, True, (0, 128, 0))
		text2 = self.font.render("Press Space", True, (0, 128, 0))
		textScale = 0.0
		textGrowthRate = 0.02

		while not self.exited and not started:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.exited = True

			if pygame.key.get_pressed()[pygame.K_ESCAPE]:
				self.exited = True
			elif pygame.key.get_pressed()[pygame.K_SPACE]:
				started = True

			####### Paint the screen ###########
			screen.fill(BLACK)
			
			if textScale < 1:
				textScale = textScale + textGrowthRate
				if textScale > 1:
					textScale = 1

			scaledText = pygame.transform.rotozoom(text, 0, textScale)

			x_offset = (text.get_width() - scaledText.get_width()) / 2
			y_offset = (text.get_height() - scaledText.get_height()) / 2

			screen.blit(scaledText,(200+x_offset, 200+y_offset))
			
			if textScale == 1:
				screen.blit(text2,(320, 320))

			pygame.display.flip()

			# Limit to 30 frames per second
			clock.tick(30)

class Background(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
		self.image = pygame.image.load("./Assets/earth-resized.png")
		self.rect = self.image.get_rect()
		self.rect.left = 0
		self.rect.top = 0

class Alien(pygame.sprite.Sprite):
	rotation = 0
	size = 1.0
	growing = True
	clockwise = True

	def __init__(self):
		# Call the parent class (Sprite) constructor
		super().__init__()
		# Load walk sprites
		self.alien = pygame.image.load("./Assets/Player/p1_stand.png")
		self.image = self.alien
		self.image.set_colorkey(TRANSCOLOUR)
		self.rect = self.image.get_rect()
		self.x = 80
		self.y = 250
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect.x = self.x
		self.rect.y = self.y

	def update(self):
		if self.growing:
			if self.size < 1.2:
				self.size = self.size + 0.01
			else:
				self.growing = False
		else:
			if self.size > 0.8:
				self.size = self.size - 0.01
			else:
				self.growing = True

		if self.clockwise:
			if self.rotation < 25:
				self.rotation = self.rotation + 1
			else:
				self.clockwise = False
		else:
			if self.rotation > -25:
				self.rotation = self.rotation - 1
			else:
				self.clockwise = True

		self.image = pygame.transform.rotozoom(self.alien, self.rotation, self.size)
		self.image.set_colorkey(TRANSCOLOUR)
		
		width = self.image.get_width()
		self.rect.x = self.x + ((self.width - width) / 2)
		height = self.image.get_height()
		self.rect.y = self.y + ((self.height - height) / 2)