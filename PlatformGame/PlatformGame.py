
"""

"""
import pygame
import random
from Tiles import Tiles, Background, TILELIST, TRANSCOLOUR, BLOCK_SIZE, WHITE
from Levels import Levels
from Player import Player

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, code): 

        # Call the parent class (Sprite) constructor
        super().__init__()
 
        #self.image = pygame.image.load("./Assets/Tiles/box.png").convert()
        t = TILELIST[code]
        self.image = t.load_sprite()
        
		# Set our transparent color
        self.image.set_colorkey(TRANSCOLOUR)
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 1100
screen_height = 770
screen = pygame.display.set_mode([screen_width, screen_height])

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
player = Player(1,8)
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
 
	# Check keyboard input
    if pygame.key.get_pressed()[pygame.K_a]:
        player.left()
    elif pygame.key.get_pressed()[pygame.K_d]:
        player.right()
    else:
        player.walking = False;

    # Clear the screen
    screen.fill(WHITE)
    # Add the background
    screen.blit(backGround.image, backGround.rect)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    # pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    # player.rect.x = pos[0]
    # player.rect.y = pos[1]

 
    # See if the player block has collided with anything.
    # blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    # Check the list of collisions.
    #for block in blocks_hit_list:
    #    score += 1
    #    print(score)
 
    # Draw all the spites
    all_sprites_list.update()
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()