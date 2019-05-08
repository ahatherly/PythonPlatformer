import pygame
from Tiles import TRANSCOLOUR, ITEMTRANSCOLOUR, BLOCK_SIZE

ITEM_CODES = ["c", "k", "l"]

class Item(pygame.sprite.Sprite):
	
	x = 0
	y = 0

	def __init__(self, code, x, y):
		# Call the parent class (Sprite) constructor
		super().__init__()

		self.code = code
		self.x = x
		self.y = y
		# Set our transparent color
		transColor = TRANSCOLOUR

		if code == "c":
			self.image = pygame.image.load("./Assets/Tiles/box.png").convert()
		elif code == "l":
			self.image = pygame.image.load("./Assets/Tiles/lock_yellow.png").convert()
		else:
			self.image = pygame.image.load("./Assets/Items/keyYellow.png").convert()
			transColor = ITEMTRANSCOLOUR

		self.tileDef = Attributes()

		self.image.set_colorkey(transColor)
		self.rect = self.image.get_rect()

	def touched(self, hud, all_sprites_list, sounds):
		if self.code == "k":
			# Got the key
			hud.addKey(all_sprites_list)
			self.kill()
	
	def update(self, sounds):
		pass

class Attributes:
	deadly = False
	obstacle = True
	climable = False
	enemy = False
	item = True