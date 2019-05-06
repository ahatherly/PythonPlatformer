
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
gravity = 5

level = Levels()
level.loadLevel("Level1.txt")
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for y in range(0,level.getHeight()):
	for x in range(0,level.getWidth()):
		code = level.getTile(x, y)
		if code != " ":
			# This represents a block
			block = Block(code)
			block.rect.x = (x*BLOCK_SIZE)
			block.rect.y = (y*BLOCK_SIZE)

			# Add the block to the list of objects
			block_list.add(block)
			all_sprites_list.add(block)
 
# Add the player
player = Player(1,7)
all_sprites_list.add(player)

# And the background
backGround = Background()

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    touched_deadly = False
 
	####### Check keyboard input ############
    if pygame.key.get_pressed()[pygame.K_a]:
        player.left()
    elif pygame.key.get_pressed()[pygame.K_d]:
        player.right()

    elif pygame.key.get_pressed()[pygame.K_w]:
        player.rect.y = player.rect.y - 10
    elif pygame.key.get_pressed()[pygame.K_s]:
        player.rect.y = player.rect.y + 2
    elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
        done = True
    else:
        player.walking = False;

    #### Gravity ##########
    down_collision_rect = pygame.Rect(player.rect.x+21, player.rect.y+85, 32, 10)
    touching_floor = False
    for t in block_list:
        if down_collision_rect.colliderect(t.rect):
            td = t.tileDef
            if td.obstacle:
                touching_floor = True
            if td.deadly:
                touched_deadly = True

    if touching_floor == False:
       player.rect.y = player.rect.y + gravity

	#### Check for deadly items ########
    if touched_deadly:
        player.reset(1, 7)
        print("DEAD!")

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
 
    # Update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()