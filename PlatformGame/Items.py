import pygame
from Tiles import TRANSCOLOUR, ITEMTRANSCOLOUR, BLOCK_SIZE, BLACK

ITEM_CODES = ["c", "k", "l"]
CRATE = "c"
KEY = "k"
LOCK = "l"

class Item(pygame.sprite.Sprite):
	
	x = 0
	y = 0
	fall_speed = 10
	falling = False

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
		self.tileDef.code = code

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

	def update(self, sounds, block_list, screen):
		if self.code == CRATE:
			# Check for falling
			#### Collision Detection ####
			self.down_collision_rect = pygame.Rect(self.rect.x+2, self.rect.y+70, 66, 1)
			self.down_collision_rect_large = pygame.Rect(self.rect.x+2, self.rect.y+70, 66, self.fall_speed)
			falling = True
			fall_speed = self.fall_speed
			# Blocks
			for t in block_list:
				if self.down_collision_rect.colliderect(t.rect):
					td = t.tileDef
					if td.obstacle:
						falling = False
				if self.down_collision_rect_large.colliderect(t.rect):
					# Check for imminent impact to avoid falling partly into the floor
					td = t.tileDef
					if td.obstacle:
						distance = (t.rect.y) - (self.rect.y+70)
						if distance < fall_speed:
							fall_speed = distance
			if self.falling:
				self.y = self.y + fall_speed
				self.rect.y = self.rect.y + fall_speed
			self.falling = falling

class Attributes:
	deadly = False
	obstacle = False
	climable = False
	enemy = False
	item = True
	code = ""