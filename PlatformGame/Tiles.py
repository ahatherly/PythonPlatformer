import pygame

class Block(pygame.sprite.Sprite):
    """
    This class represents a sprite on the screen.
    """

    x = 0
    y = 0

    def __init__(self, code, x, y): 

        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.x = x
        self.y = y

        #self.image = pygame.image.load("./Assets/Tiles/box.png").convert()
        t = TILELIST[code]
        self.image = t.load_sprite()
        self.tileDef = t
        transColor = TRANSCOLOUR
        if code == "d":
            transColor = ITEMTRANSCOLOUR
        self.image.set_colorkey(transColor)
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

class Tiles:

	filePath = "./Assets/"
	code = " "
	filename = ""
	deadly = False
	obstacle = True
	climbable = False
	enemy = False
	item = False

	def __init__(self, code, filename, deadly = False, obstacle = True, climbable = False):
		self.code = code
		self.filename = filename
		self.deadly = deadly
		self.obstacle = obstacle
		self.climable = climbable

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
ITEMTRANSCOLOUR = (255, 255, 255, 255)
BLOCK_SIZE = 70
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TILELIST = {}
TILELIST["T"] = Tiles("T", "Tiles/tochLit.png", False, False)
TILELIST["="] = Tiles("=", "Tiles/grassMid.png")
TILELIST["w"] = Tiles("w", "Tiles/liquidWaterTop.png", True)
TILELIST["W"] = Tiles("W", "Tiles/liquidWater.png", True)
TILELIST["r"] = Tiles("r", "Tiles/grassCliffRight.png")
TILELIST["\\"] = Tiles("\\", "Tiles/grassCliffLeft.png")
TILELIST["b"] = Tiles("b", "Tiles/bridgeLogsFlipped.png")
TILELIST["#"] = Tiles("#", "Tiles/grassCenter.png")
TILELIST["("] = Tiles("(", "Tiles/grassLeft.png")
TILELIST[")"] = Tiles(")", "Tiles/grassRight.png")
TILELIST["<"] = Tiles("<", "Tiles/signLeft.png", False, False)
TILELIST["e"] = Tiles("e", "Tiles/signExit.png", False, False)
TILELIST[">"] = Tiles(">", "Tiles/signRight.png", False, False)
#TILELIST["/"] = Tiles("/", "Tiles/grassHillLeft.png")
#TILELIST["\\"] = Tiles("\\", "Tiles/grassHillRight.png")
TILELIST["|"] = Tiles("|", "Tiles/ladder_mid.png", False, False, True)
TILELIST["^"] = Tiles("^", "Tiles/ladder_top.png", False, False, True)
TILELIST["D"] = Tiles("D", "Tiles/door_openMid.png", False, False)
TILELIST["d"] = Tiles("d", "Tiles/door_openTop.png", False, False)
