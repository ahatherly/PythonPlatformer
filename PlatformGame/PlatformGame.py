import pygame
import random
from Sounds import Sounds
from Menus import Menus
from GameLoop import GameLoop

# Initialize Pygame
sounds = Sounds()
pygame.init()
pygame.display.set_caption("Alien Escape!")


# Set the height and width of the screen
screen_width = 1100
screen_height = 770
screen = pygame.display.set_mode([screen_width, screen_height])
exited = False

menus = Menus(screen)

while not exited:
	# Start page
	menus.startMenu()

	# Game
	if not menus.exited:
		game = GameLoop()
		game.runLevel1(screen, sounds)

		if game.died:
			sounds.gameover()
			menus.messageScreen("Game Over!")
		elif game.won:
			sounds.won()
			menus.messageScreen("You Won!!!")

		del game

	if menus.exited:
		exited = True

pygame.quit()