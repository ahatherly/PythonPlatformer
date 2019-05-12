import pygame
import random
from Tiles import Tiles, Block, Background, TILELIST, TRANSCOLOUR, BLOCK_SIZE, WHITE, BLACK
from Levels import Levels
from Player import Player
from Sounds import Sounds
from Hud import Hud
from Enemies import Enemy
from Items import Item, ITEM_CODES

class GameLoop(object):

	won = False
	died = False
	exited = False

	def runLevel1(self, screen, sounds):
		gravity = 7
		enemies = {}
		level = Levels()
		level.loadLevel("Level1.txt", enemies)
 
		block_list = pygame.sprite.Group()
		# This is a list of every sprite. 
		# All blocks and the player block as well.
		all_sprites_list = pygame.sprite.Group()
		enemies_list = pygame.sprite.Group()

		# Initialise the level
		for y in range(0,level.getHeight()):
			for x in range(0,level.getWidth()):
				code = level.getTile(x, y)
				if code != " ":
					if code.isdigit():
						# Enemy
						enemies[code].create(x*BLOCK_SIZE, y*BLOCK_SIZE)
						enemies[code].rect.x = enemies[code].x + level.level_x_offset
						enemies[code].rect.y = enemies[code].y
						enemies_list.add(enemies[code])
					elif code in ITEM_CODES:
						item = Item(code, x*BLOCK_SIZE, y*BLOCK_SIZE)
						item.rect.x = (x*BLOCK_SIZE) + level.level_x_offset
						item.rect.y = (y*BLOCK_SIZE)
						# Add the block to the list of objects
						block_list.add(item)
						all_sprites_list.add(item)
					else:
						# This represents a block
						block = Block(code, x*BLOCK_SIZE, y*BLOCK_SIZE)
						block.rect.x = (x*BLOCK_SIZE) + level.level_x_offset
						block.rect.y = (y*BLOCK_SIZE)
						# Add the block to the list of objects
						block_list.add(block)
						all_sprites_list.add(block)

		# Add the player
		player = Player(5,7)
		#player = Player(5,2)
		#level.level_x_offset = -3000
		all_sprites_list.add(player)
		all_sprites_list.add(enemies_list.sprites())

		# Add the HUD
		hud = Hud(player, all_sprites_list)

		# And the background
		backGround = Background()

		# Used to manage how fast the screen updates
		clock = pygame.time.Clock()
 
		score = 0
		jumping = 0
		falling = False

		# -------- Main Program Loop -----------
		while not self.exited and not self.won and not self.died:
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT: 
					self.exited = True

			touched_deadly = False
			touching_floor = False
			touching_ceiling = False
			touching_left = False
			touching_right = False
			touching_ladder = False
			touching_exit = False
			touching_enemy = False
			crate_touching_left = None
			crate_touching_right = None

			#### Collision Detection ####
			down_collision_rect = pygame.Rect(player.rect.x+21, player.rect.y+85, 32, 10)
			central_collision_rect = pygame.Rect(player.rect.x+31, player.rect.y+85, 12, 10)
			left_collision_rect = pygame.Rect(player.rect.x+5, player.rect.y+12, 10, 70)
			right_collision_rect = pygame.Rect(player.rect.x+58, player.rect.y+12, 10, 70)
			up_collision_rect = pygame.Rect(player.rect.x+21, player.rect.y, 32, 10)
    
			# Blocks
			checked = 0
			for t in pygame.sprite.spritecollide(player, block_list, False):
				checked = checked + 1
				if down_collision_rect.colliderect(t.rect):
					td = t.tileDef
					if td.obstacle:
						if falling == True:
							sounds.land()
						touching_floor = True
						falling = False
					if td.deadly:
						touched_deadly = True
					if td.item:
						t.touched(hud, all_sprites_list, sounds, player)
						if t.code == "c":
							touching_floor = True
				if up_collision_rect.colliderect(t.rect):
					td = t.tileDef
					if td.obstacle:
						touching_ceiling = True
						jumping = 0
					if td.deadly:
						touched_deadly = True
					if td.item:
						t.touched(hud, all_sprites_list, sounds, player)
						if t.code == "c":
							touching_ceiling = True
				if left_collision_rect.colliderect(t.rect):
					td = t.tileDef
					if td.obstacle:
						touching_left = True
					if td.deadly:
						touched_deadly = True
					if td.item:
						t.touched(hud, all_sprites_list, sounds, player)
						if t.code == "c":
							crate_touching_left = t
				if right_collision_rect.colliderect(t.rect):
					td = t.tileDef
					if td.obstacle:
						touching_right = True
					if td.deadly:
						touched_deadly = True
					if td.item:
						t.touched(hud, all_sprites_list, sounds, player)
						if t.code == "c":
							crate_touching_right = t
				if central_collision_rect.colliderect(t.rect):
					td = t.tileDef
					if td.climable:
						touching_ladder = True
						jumping = 0
					if td.code == "D":
						touching_exit = True

			#### Jump ####
			if jumping > 0:
				player.rect.y = player.rect.y - jumping
				jumping = jumping - 1

			# Enemies
			for e in enemies_list:
				if player.rect.colliderect(e.rect):
					touching_enemy = True

			if touching_enemy:
				if player.invulnerable == 0:
					player.energyDown(sounds, level)

			#### Gravity ##########
			if not touching_floor and not touching_ladder:
			   player.rect.y = player.rect.y + gravity
			   falling = True

			####### Check keyboard input ############
    
			# Left
			if pygame.key.get_pressed()[pygame.K_a] and touching_left == False:
				player.left()
				speed = player.speed
				if crate_touching_left != None:
					if not crate_touching_left.falling:
						speed = player.pushing_speed
						crate_touching_left.left(speed)
						level.level_x_offset = level.level_x_offset + speed
				else:
					level.level_x_offset = level.level_x_offset + speed
			# Right
			elif pygame.key.get_pressed()[pygame.K_d] and touching_right == False:
				player.right()
				speed = player.speed
				if crate_touching_right != None:
					if not crate_touching_right.falling:
						speed = player.pushing_speed
						crate_touching_right.right(speed)
						level.level_x_offset = level.level_x_offset - speed
				else:
					level.level_x_offset = level.level_x_offset - speed
			else:
				player.walking = False;

			# Up
			if pygame.key.get_pressed()[pygame.K_w]:
				if touching_ladder:
					player.rect.y = player.rect.y - 5
				elif touching_floor and jumping == 0:
					jumping = 20
					sounds.jump()
				if touching_exit:
					self.won = True

			# Down
			if pygame.key.get_pressed()[pygame.K_s]:
				if touching_ladder and not touching_floor:
					player.rect.y = player.rect.y + 5

			# Exit
			if pygame.key.get_pressed()[pygame.K_ESCAPE]:
				self.exited = True

			#### Move the level sprites (blocks and enemies)###
			for t in block_list:
				t.rect.x = t.x + level.level_x_offset
			for e in enemies_list:
				e.rect.x = e.x + level.level_x_offset

			#### Check for deadly items ########
			if touched_deadly:
				player.dead(sounds, level)

			# Check for player death
			if player.is_dead:
				self.died = True

			####### Paint the screen ###########
			# Clear the screen
			screen.fill(WHITE)
			# Add the background
			screen.blit(backGround.image, backGround.rect)
			# Update sprites (animate)
			all_sprites_list.update(sounds, block_list, screen)
			# Draw all the sprites
			all_sprites_list.draw(screen)

			# Draw collision detectors (troubleshooting)
			#pygame.draw.rect(screen, BLACK, down_collision_rect)
			#pygame.draw.rect(screen, BLACK, up_collision_rect)
			#pygame.draw.rect(screen, BLACK, left_collision_rect)
			#pygame.draw.rect(screen, BLACK, right_collision_rect)
			#pygame.draw.rect(screen, BLACK, central_collision_rect)
			#for t in block_list:
			#    if t.tileDef.item:
			#        if t.code == "c":
			#            pygame.draw.rect(screen, BLACK, t.down_collision_rect)
			#            pygame.draw.rect(screen, BLACK, t.down_collision_rect_large)

			# Update the screen with what we've drawn.
			pygame.display.flip()
 
			# Limit to 60 frames per second
			clock.tick(60)
