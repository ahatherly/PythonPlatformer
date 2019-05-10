import pygame
from Tiles import TRANSCOLOUR, BLOCK_SIZE

class Player(pygame.sprite.Sprite):
	x = 0
	y = 0
	animation_state = 0
	animation_delay = 2
	animation_delay_count = 0
	walking = True
	facingRight = True
	speed = 5
	pushing_speed = 2
	lives = 3
	energy = 3
	invulnerable = 0
	total_invulnerable = 120
	flash_delay = 10
	total_flash_delay = 10
	has_key = False

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
		self.transparentImage = pygame.image.load("./Assets/transparent.png").convert()
		self.standing = pygame.image.load("./Assets/Player/p1_stand.png").convert()

		self.image = self.standing
		# Set our transparent color
		self.image.set_colorkey(TRANSCOLOUR)
		
		# Update the position of this object by setting the values
        # of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.x = (self.x*BLOCK_SIZE)
		self.rect.y = (self.y*BLOCK_SIZE-25)

	def reset(self, x, y):
		self.rect.x = (self.x*BLOCK_SIZE)
		self.rect.y = (self.y*BLOCK_SIZE-25)

	def update(self, sounds, block_list):
		if self.walking:
			if self.animation_delay_count == self.animation_delay:
				self.animation_delay_count = 0
				self.animation_state = self.animation_state + 1
				if self.animation_state % 2 == 0:
				    sounds.walk()
				if self.animation_state > 10:
					self.animation_state = 0;
				# Set the sprite image
				if self.facingRight:
					self.image = self.walkImages[self.animation_state]
				else:
					self.image = pygame.transform.flip(self.walkImages[self.animation_state], True, False)
				# Set our transparent color
				self.image.set_colorkey(TRANSCOLOUR)
			else:
				self.animation_delay_count = self.animation_delay_count + 1
		else:
			self.animation_state = 0;
			if self.facingRight:
				self.image = self.standing
			else:
				self.image = pygame.transform.flip(self.standing, True, False)
			# Set our transparent color
			self.image.set_colorkey(TRANSCOLOUR)
		# Temporarily invulnerable - flash on and off
		if self.invulnerable > 0:
			self.invulnerable = self.invulnerable - 1
			self.flash_delay = self.flash_delay - 1
			if self.flash_delay == 0:
				self.flash_delay = self.total_flash_delay
			if self.flash_delay < (self.total_flash_delay / 2):
				self.image = self.transparentImage
				# Set our transparent color
				self.image.set_colorkey(TRANSCOLOUR)

	def right(self):
		self.walking = True
		self.facingRight = True
		#self.rect.x = self.rect.x + self.speed
	
	def left(self):
		self.walking = True
		self.facingRight = False
		#self.rect.x = self.rect.x - self.speed

	def dead(self, sounds, level):
		sounds.dead()
		self.lives = self.lives - 1
		self.energy = 3
		self.reset(5, 7)
		level.level_x_offset = level.start_level_x_offset

	def energyDown(self, sounds, level):
		self.energy = self.energy - 1
		if self.energy == 0:
			self.invulnerable = 10
			self.dead(sounds, level)
		else:
			sounds.damage()
			self.invulnerable = self.total_invulnerable