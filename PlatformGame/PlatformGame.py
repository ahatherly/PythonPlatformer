
"""

"""
import pygame
import random
from Tiles import Tiles, Block, Background, TILELIST, TRANSCOLOUR, BLOCK_SIZE, WHITE, BLACK
from Levels import Levels
from Player import Player

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 1100
screen_height = 770
screen = pygame.display.set_mode([screen_width, screen_height])
gravity = 7
start_level_x_offset = -160
level_x_offset = -160

level = Levels()
level.loadLevel("Level1.txt")
 
block_list = pygame.sprite.Group()
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for y in range(0,level.getHeight()):
	for x in range(0,level.getWidth()):
		code = level.getTile(x, y)
		if code != " ":
			# This represents a block
			block = Block(code, x*BLOCK_SIZE, y*BLOCK_SIZE)
			block.rect.x = (x*BLOCK_SIZE) + level_x_offset
			block.rect.y = (y*BLOCK_SIZE)
			# Add the block to the list of objects
			block_list.add(block)
			all_sprites_list.add(block)
 
# Add the player
player = Player(5,7)
all_sprites_list.add(player)

# And the background
backGround = Background()

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
jumping = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    touched_deadly = False
    touching_floor = False
    touching_left = False
    touching_right = False

    #### Jump ####
    if jumping > 0:
        player.rect.y = player.rect.y - jumping
        jumping = jumping - 1


    #### Collision Detection ####
    down_collision_rect = pygame.Rect(player.rect.x+21, player.rect.y+85, 32, 10)
    left_collision_rect = pygame.Rect(player.rect.x+5, player.rect.y+12, 10, 70)
    right_collision_rect = pygame.Rect(player.rect.x+58, player.rect.y+12, 10, 70)
    for t in block_list:
        if down_collision_rect.colliderect(t.rect):
            td = t.tileDef
            if td.obstacle:
                touching_floor = True
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

    #### Gravity ##########
    if touching_floor == False:
       player.rect.y = player.rect.y + gravity

	####### Check keyboard input ############
    if pygame.key.get_pressed()[pygame.K_a] and touching_left == False:
        player.left()
        level_x_offset = level_x_offset + player.speed
    elif pygame.key.get_pressed()[pygame.K_d] and touching_right == False:
        player.right()
        level_x_offset = level_x_offset - player.speed
    else:
        player.walking = False;

    if pygame.key.get_pressed()[pygame.K_w]:
        if touching_floor:
            jumping = 20
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        done = True
    

    #### Move the level sprites ###
    for t in block_list:
        t.rect.x = t.start_x + level_x_offset

	#### Check for deadly items ########
    if touched_deadly:
        player.reset(5, 7)
        level_x_offset = start_level_x_offset

	####### Paint the screen ###########
    # Clear the screen
    screen.fill(WHITE)
    # Add the background
    screen.blit(backGround.image, backGround.rect)
    # Draw all the spites
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    # Draw collision detectors (troubleshooting)
    #pygame.draw.rect(screen, BLACK, down_collision_rect)
    #pygame.draw.rect(screen, BLACK, left_collision_rect)
    #pygame.draw.rect(screen, BLACK, right_collision_rect)
 
    # Update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()