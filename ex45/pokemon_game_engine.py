class Engine(object):
	
	def __init__(self, scenes):
		self.scenes = scenes
	
	def play(self, player):
		while player["Game Over"] == False:
			for scene in self.scenes:
				gym = scene
				player = gym.start(player)
				player = gym.conclude(player)