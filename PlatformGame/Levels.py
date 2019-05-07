class Levels:

	levelTiles = []
	level_width = 0
	level_height = 0
	start_level_x_offset = -160
	level_x_offset = -160

	def __init__(self):
		pass

	def loadLevel(self, filename):
		file = open(filename, "r")
		for line in file:
			self.levelTiles.append(line)
			if len(line) > self.level_width:
				self.level_width = len(line)
		self.level_height = len(self.levelTiles)
		self.level_x_offset = self.start_level_x_offset

	def getTile(self, x, y):
		if y > len(self.levelTiles)-1:
			return " "
		line = self.levelTiles[y]
		if x > len(line)-1:
			return " "
		code = line[x]
		if code == "\n":
			return " "
		return code

	def getWidth(self):
		return self.level_width

	def getHeight(self):
		return self.level_height
