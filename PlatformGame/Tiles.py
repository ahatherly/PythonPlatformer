import pygame

class Block(pygame.sprite.Sprite):
    """
    This class represents a sprite on the screen.
    """

    start_x = 0
    start_y = 0

    def __init__(self, code, x, y): 

        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.start_x = x
        self.start_y = y

        #self.image = pygame.image.load("./Assets/Tiles/box.png").convert()
        t = TILELIST[code]
        self.image = t.load_sprite()
        self.tileDef = t
        
		# Set our transparent color
        self.image.set_colorkey(TRANSCOLOUR)
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

class Tiles:

	filePath = "./Assets/Tiles/"
	code = " "
	filename = ""
	deadly = False
	obstacle = True

	def __init__(self, code, filename, deadly = False, obstacle = True):
		self.code = code
		self.filename = filename
		self.deadly = deadly
		self.obstacle = obstacle

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
BLACK = (0, 0, 0)

TILELIST = {}
TILELIST["T"] = Tiles("T", "tochLit.png", False, False)
TILELIST["="] = Tiles("=", "grassMid.png")
TILELIST["w"] = Tiles("w", "liquidWaterTop.png", True)
TILELIST["W"] = Tiles("W", "liquidWater.png", True)
TILELIST["r"] = Tiles("r", "grassCliffRight.png")
TILELIST["¬"] = Tiles("¬", "grassCliffLeft.png")
TILELIST["b"] = Tiles("b", "bridgeLogsFlipped.png")
TILELIST["#"] = Tiles("#", "grassCenter.png")
TILELIST["("] = Tiles("(", "grassLeft.png")
TILELIST[")"] = Tiles(")", "grassRight.png")
TILELIST["<"] = Tiles("<", "signLeft.png", False, False)
TILELIST[">"] = Tiles(">", "signRight.png", False, False)
TILELIST["/"] = Tiles("/", "grassHillLeft.png")
TILELIST["\\"] = Tiles("\\", "grassHillRight.png")