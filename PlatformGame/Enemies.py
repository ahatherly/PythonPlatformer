import pygame
from Tiles import TRANSCOLOUR

class Enemy(pygame.sprite.Sprite):
	
	start_x = 0
	start_y = 0

	slimeImages = []
	animation_state = 0
	updateDelay = 30

	def __init__(self, code, x, y):
		
		# Call the parent class (Sprite) constructor
		super().__init__()

		self.start_x = x
		self.start_y = y

		self.slimeImages.append(pygame.image.load("./Assets/Enemies/slimeWalk1.png").convert())
		self.slimeImages.append(pygame.image.load("./Assets/Enemies/slimeWalk2.png").convert())
		
		self.image = self.slimeImages[0]
		self.tileDef = Attributes()
		# Set our transparent color
		transColor = TRANSCOLOUR

		self.image.set_colorkey(transColor)
		self.rect = self.image.get_rect()
	
	def update(self, sounds):
		self.updateDelay = self.updateDelay - 1
		if self.updateDelay == 0:
			self.updateDelay = 30

			self.animation_state = self.animation_state + 1
			if self.animation_state == 2:
				self.animation_state = 0

			self.image = self.slimeImages[self.animation_state]
			self.image.set_colorkey(TRANSCOLOUR)

class Attributes:
	deadly = False
	obstacle = False
	climable = False
	enemy = True