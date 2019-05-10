import pygame
from Tiles import BLOCK_SIZE, TRANSCOLOUR, ITEMTRANSCOLOUR

class Hud:
	heartImages = []
	def __init__(self, player, all_sprites_list):
		self.player = player
		# Load heart sprites
		self.heartImages.append(pygame.image.load("./Assets/transparent.png").convert())
		self.heartImages.append(pygame.image.load("./Assets/HUD/hud_heartEmpty.png").convert())
		self.heartImages.append(pygame.image.load("./Assets/HUD/hud_heartHalf.png").convert())
		self.heartImages.append(pygame.image.load("./Assets/HUD/hud_heartFull.png").convert())

		life1 = Lives(BLOCK_SIZE*10, 20, 1, self)
		all_sprites_list.add(life1)
		life2 = Lives(BLOCK_SIZE*10+55, 20, 2, self)
		all_sprites_list.add(life2)
		life3 = Lives(BLOCK_SIZE*10+110, 20, 3, self)
		all_sprites_list.add(life3)

	def addKey(self, all_sprites_list):
		self.key = Key()
		all_sprites_list.add(self.key)

	def removeKey(self):
		self.key.kill()

class Key(pygame.sprite.Sprite):
	def __init__(self):
		# Call the parent class (Sprite) constructor
		super().__init__()
		self.image = pygame.image.load("./Assets/Items/keyYellow.png").convert()
		self.image.set_colorkey(ITEMTRANSCOLOUR)
		self.rect = self.image.get_rect()
		self.rect.x = (BLOCK_SIZE*9)
		self.rect.y = (20)

class Lives(pygame.sprite.Sprite):
	
	lifenumber = 0
	updateDelay = 30

	def __init__(self, x, y, lifenumber, hud):
		# Call the parent class (Sprite) constructor
		super().__init__()

		self.lifenumber = lifenumber
		self.hud = hud

		self.image = self.hud.heartImages[3]
		# Set our transparent color
		self.image.set_colorkey(TRANSCOLOUR)
		
		# Update the position of this object by setting the values
		# of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.x = (x)
		self.rect.y = (y)

	def update(self, sounds):
		self.updateDelay = self.updateDelay - 1
		if self.updateDelay == 0:
			self.updateDelay = 30

			lives = self.hud.player.lives
			energy = self.hud.player.energy

			if lives < self.lifenumber:
				self.image = self.hud.heartImages[0]
			elif lives == self.lifenumber:
				self.image = self.hud.heartImages[energy]
				self.image.set_colorkey(TRANSCOLOUR)
