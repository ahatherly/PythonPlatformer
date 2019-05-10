import pygame
from Tiles import TRANSCOLOUR, ITEMTRANSCOLOUR, BLOCK_SIZE

ITEM_CODES = ["c", "k", "l"]
CRATE = "c"
KEY = "k"
LOCK = "l"

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

		if code == CRATE:
			self.image = pygame.image.load("./Assets/Tiles/box.png").convert()
		elif code == LOCK:
			self.image = pygame.image.load("./Assets/Tiles/lock_yellow.png").convert()
		else:
			self.image = pygame.image.load("./Assets/Items/keyYellow.png").convert()
			transColor = ITEMTRANSCOLOUR

		self.tileDef = Attributes()

		self.image.set_colorkey(transColor)
		self.rect = self.image.get_rect()

	def touched(self, hud, all_sprites_list, sounds, player):
		if self.code == KEY:
			# Got the key
			sounds.key()
			hud.addKey(all_sprites_list)
			player.has_key = True
			self.kill()
		elif self.code == LOCK and player.has_key:
			# Unlock
			sounds.unlock()
			hud.removeKey()
			player.has_key = False
			self.kill()
	
	def left(self, amount):
		self.x = self.x - amount
	
	def right(self, amount):
		self.x = self.x + amount

	def update(self, sounds):
		pass

class Attributes:
	deadly = False
	obstacle = False
	climable = False
	enemy = False
	item = True