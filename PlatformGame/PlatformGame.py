
"""

"""
import pygame
import random
from Tiles import Tiles, Block, Background, TILELIST, TRANSCOLOUR, BLOCK_SIZE, WHITE, BLACK
from Levels import Levels
from Player import Player
from Sounds import Sounds
from Hud import Hud
from Enemies import Enemy

# Initialize Pygame
sounds = Sounds()
pygame.init()


# Set the height and width of the screen
screen_width = 1100
screen_height = 770
screen = pygame.display.set_mode([screen_width, screen_height])
gravity = 7

level = Levels()
level.loadLevel("Level1.txt")
 
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
			if code == "s":
				enemy = Enemy(code, x*BLOCK_SIZE, y*BLOCK_SIZE)
				enemy.rect.x = (x*BLOCK_SIZE) + level.level_x_offset
				enemy.rect.y = (y*BLOCK_SIZE) + 44
				enemies_list.add(enemy)
				all_sprites_list.add(enemy)
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
all_sprites_list.add(player)

# Add the HUD
hud = Hud(player, all_sprites_list)

# And the background
backGround = Background()

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
jumping = 0
falling = False

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    touched_deadly = False
    touching_floor = False
    touching_left = False
    touching_right = False
    touching_ladder = False
    touching_enemy = False

    #### Jump ####
    if jumping > 0:
        player.rect.y = player.rect.y - jumping
        jumping = jumping - 1


    #### Collision Detection ####
    down_collision_rect = pygame.Rect(player.rect.x+21, player.rect.y+85, 32, 10)
    ladder_collision_rect = pygame.Rect(player.rect.x+31, player.rect.y+85, 12, 10)
    left_collision_rect = pygame.Rect(player.rect.x+5, player.rect.y+12, 10, 70)
    right_collision_rect = pygame.Rect(player.rect.x+58, player.rect.y+12, 10, 70)
    
    # Blocks
    for t in block_list:
        if down_collision_rect.colliderect(t.rect):
            td = t.tileDef
            if td.obstacle:
                if falling == True:
                    sounds.land()
                touching_floor = True
                falling = False
            if td.deadly:
                touched_deadly = True
        if left_collision_rect.colliderect(t.rect):
            td = t.tileDef
            if td.obstacle:
                touching_left = True
            if td.deadly:
                touched_deadly = True
        if right_collision_rect.colliderect(t.rect):
            td = t.tileDef
            if td.obstacle:
                touching_right = True
            if td.deadly:
                touched_deadly = True
        if ladder_collision_rect.colliderect(t.rect):
            td = t.tileDef
            if td.climable:
                touching_ladder = True

	# Enemies
    for e in enemies_list:
        if down_collision_rect.colliderect(e.rect):
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
        level.level_x_offset = level.level_x_offset + player.speed
    # Right
    elif pygame.key.get_pressed()[pygame.K_d] and touching_right == False:
        player.right()
        level.level_x_offset = level.level_x_offset - player.speed
    else:
        player.walking = False;

    # Up
    if pygame.key.get_pressed()[pygame.K_w]:
        if touching_ladder:
            player.rect.y = player.rect.y - 5
        elif touching_floor:
            jumping = 20
            sounds.jump()

    # Down
    if pygame.key.get_pressed()[pygame.K_s]:
        if touching_ladder and not touching_floor:
            player.rect.y = player.rect.y + 5

    # Exit
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        done = True

    #### Move the level sprites (blocks and enemies)###
    for t in block_list:
        t.rect.x = t.start_x + level.level_x_offset
    for e in enemies_list:
        e.rect.x = e.start_x + level.level_x_offset

	#### Check for deadly items ########
    if touched_deadly:
        player.dead(sounds, level)

	####### Paint the screen ###########
    # Clear the screen
    screen.fill(WHITE)
    # Add the background
    screen.blit(backGround.image, backGround.rect)
    # Draw all the spites
    all_sprites_list.update(sounds)
    all_sprites_list.draw(screen)
    # Draw collision detectors (troubleshooting)
    #pygame.draw.rect(screen, BLACK, down_collision_rect)
    #pygame.draw.rect(screen, BLACK, left_collision_rect)
    #pygame.draw.rect(screen, BLACK, right_collision_rect)
    #pygame.draw.rect(screen, BLACK, ladder_collision_rect)
 
    # Update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()