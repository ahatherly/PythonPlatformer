import pygame
from Tiles import TRANSCOLOUR, BLOCK_SIZE

class Player(pygame.sprite.Sprite):
	x = 0
	y = 0
	animation_state = 0
	animation_delay = 3
	animation_delay_count = 0
	walking = True
	speed = 1

	walkImages = []

	def __init__(self, x, y):
		# Call the parent class (Sprite) constructor
		super().__init__()

		self.x = x
		self.y = y

		# Load walk sprites
		self.walkImages.append(pygame.image.load("./Assets/Player/p1_walk/PNG/p1_walk01.png").convert())
		self.walkImages.append(pygame.image.load("./Assets/Player/p1_walk/PNG/p1_walk02.png").convert())
		self.walkImages.append(pygame.image.load("./Assets/Player/p1_walk/PNG/p1_walk03.png").convert())
		self.walkImages.append(pygame.image.load("./Assets/Player/p1_walk/PNG/p1_walk04.png").convert())
		self.walkImages.append(pygame.image.load("./Assets/Player/p1_walk/PNG/p1_walk05.png").convert())
		self.walkImages.append(pygame.image.load("./Assets/Player/p1_walk/PNG/p1_walk06.png").convert())
		self.walkImages.append(pygame.image.load("./Assets/Player/p1_walk/PNG/p1_walk07.png").convert())
		self.walkImages.append(pygame.image.load("./Assets/Player/p1_walk/PNG/p1_walk08.png").convert())
		self.walkImages.append(pygame.image.load("./Assets/Player/p1_walk/PNG/p1_walk09.png").convert())
		self.walkImages.append(pygame.image.load("./Assets/Player/p1_walk/PNG/p1_walk10.png").convert())
		self.walkImages.append(pygame.image.load("./Assets/Player/p1_walk/PNG/p1_walk11.png").convert())

		self.image = self.walkImages[self.animation_state]
		# Set our transparent color
		self.image.set_colorkey(TRANSCOLOUR)
		
		# Update the position of this object by setting the values
        # of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.x = (self.x*BLOCK_SIZE)
		self.rect.y = (self.y*BLOCK_SIZE-25)

	def update(self):
		if self.walking:
			if self.animation_delay_count == self.animation_delay:
				self.animation_delay_count = 0
				self.animation_state = self.animation_state + 1
				if self.animation_state > 10:
					self.animation_state = 0;
				self.image = self.walkImages[self.animation_state]
				# Set our transparent color
				self.image.set_colorkey(TRANSCOLOUR)
			else:
				self.animation_delay_count = self.animation_delay_count + 1
		else:
			self.animation_state = 0;
			self.image = self.walkImages[self.animation_state]
			# Set our transparent color
			self.image.set_colorkey(TRANSCOLOUR)

	def right(self):
		player.walking = True
		self.x = self.x + self.speed
	
	def left(self):
		player.walking = True
		self.x = self.x - self.speed
