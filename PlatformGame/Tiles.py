import pygame

class Tiles:

	filePath = "./Assets/Tiles/"
	code = " "
	filename = ""

	def __init__(self, code, filename):
		self.code = code
		self.filename = filename

	def load_sprite(self):
		return pygame.image.load(self.filePath + self.filename).convert()

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("./Assets/sky2.png")
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0

TRANSCOLOUR = (0, 0, 0, 255)
BLOCK_SIZE = 70
WHITE = (255, 255, 255)

TILELIST = {}
TILELIST["T"] = Tiles("T", "tochLit.png")
TILELIST["="] = Tiles("=", "grassMid.png")
TILELIST["w"] = Tiles("w", "liquidWaterTop.png")
TILELIST["W"] = Tiles("W", "liquidWater.png")
TILELIST["r"] = Tiles("r", "grassCliffRight.png")
TILELIST["¬"] = Tiles("¬", "grassCliffLeft.png")
TILELIST["b"] = Tiles("b", "bridgeLogsFlipped.png")
