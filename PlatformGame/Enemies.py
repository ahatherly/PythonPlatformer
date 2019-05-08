import pygame
from Tiles import TRANSCOLOUR, BLOCK_SIZE

class Enemy(pygame.sprite.Sprite):
	
	x = 0
	y = 0
	animation_state = 0
	originalUpdateDelay = 30
	leftMovementExtent = 0
	rightMovementExtent = 0
	movingRight = False
	speed = 2
	enemySpriteType = "a"

	def __init__(self, code, leftMovementExtent, rightMovementExtent, speed, enemySpriteType):
		self.leftMovementExtent = leftMovementExtent
		self.rightMovementExtent = rightMovementExtent
		self.code = code
		self.speed = speed
		self.enemySpriteType = enemySpriteType
		self.spriteImages = []
		if enemySpriteType == "a":
			# Slime
			self.spriteImages.append(pygame.image.load("./Assets/Enemies/slimeWalk1.png").convert())
			self.spriteImages.append(pygame.image.load("./Assets/Enemies/slimeWalk2.png").convert())
		else:
			# Fly
			self.spriteImages.append(pygame.image.load("./Assets/Enemies/flyFly1.png").convert())
			self.spriteImages.append(pygame.image.load("./Assets/Enemies/flyFly2.png").convert())
			self.originalUpdateDelay = 5
		self.updateDelay = self.originalUpdateDelay

	def create(self, x, y):
		
		# Call the parent class (Sprite) constructor
		super().__init__()

		self.x = x
		self.y = y

		# Update left and right movement extent to be relative to starting x and y position
		self.leftMovementExtent = self.x - (self.leftMovementExtent * BLOCK_SIZE)
		self.rightMovementExtent = self.x + (self.rightMovementExtent * BLOCK_SIZE)

		# Shift the enemy sprite down a bit depending on sprite type
		if self.enemySpriteType == "a":
			# Slime
			self.y = self.y + 48
		else:
			# Fly
			self.y = self.y + 20
		
		self.image = self.spriteImages[0]
		self.tileDef = Attributes()
		# Set our transparent color
		transColor = TRANSCOLOUR

		self.image.set_colorkey(transColor)
		self.rect = self.image.get_rect()

	
	def update(self, sounds):
		if self.movingRight:
			if self.x < self.rightMovementExtent:
				self.x = self.x + self.speed
			else:
				self.movingRight = False
				self.updateDelay = 1
		else:
			if self.x > self.leftMovementExtent:
				self.x = self.x - self.speed
			else:
				self.movingRight = True
				self.updateDelay = 1

		self.updateDelay = self.updateDelay - 1
		if self.updateDelay == 0:
			self.updateDelay = self.originalUpdateDelay

			self.animation_state = self.animation_state + 1
			if self.animation_state == 2:
				self.animation_state = 0

			if self.movingRight:
				self.image = pygame.transform.flip(self.spriteImages[self.animation_state], True, False)
				self.image.set_colorkey(TRANSCOLOUR)
			else:
				self.image = self.spriteImages[self.animation_state]
				self.image.set_colorkey(TRANSCOLOUR)

class Attributes:
	deadly = False
	obstacle = False
	climable = False
	enemy = True
	item = False