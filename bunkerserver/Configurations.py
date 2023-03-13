from json import loads, dumps



class Configurations:
	
	CONFIG_PATH = "config/config.json"

	def __init__(self):
		with open(self.CONFIG_PATH, "r") as conf:
			self.configs = loads(conf.read())
			
	

		
