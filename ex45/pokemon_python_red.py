from pokemon_game_engine import Engine
from pokemon import *

player = {
	"Name" : " ",
	"Rival's Name": " ",
	"Party": [],
	"Party Fainted": False,
	"Game Over": False}
	

class Scene(object):
	
	def __init__(self):
		pass

	def start(self, player):
		pass

	def conclude(self, player):
		pass


class IntroductionGen1(Scene):

	def start(self, player):
		print "\nHello there! Welcome to the world of Pokemon! My name is Oak!"
		print "People call me the Pokemon Professor!"
		print "This world is inhabitated by creatures called Pokemon! For some"
		print "people, Pokemon are pets. Others use them for fights. Myself..."
		print "I study Pokemon as a profession.\n"
		name = raw_input("First, what is your name? ")
		print "Right! So your name is %s!" % name
		print "\nThis is my grandson. He's been your rival since you were a baby."
		rival_name = raw_input("...Erm, what is his name again? ")
		print "That's right! I remember now! His name is %s!\n" % rival_name
		print "%s! Your very own Pokemon legend is about to unfold! A world of" % name
		print "dreams and adventures with Pokemon awaits! Let's go!\n"
		player["Name"] = name
		player["Rival's Name"] = rival_name
		return player
		
	def conclude(self, player):
		starter = ""
		print "Here, %s! There are 3 Pokemon here! Haha! They are inside the" % player["Name"]
		print "pokeballs. When I was young, I was a serious Pokemon trainer."
		print "In my old age, I have only 3 left, but you can have one! Choose!\n"
		print "Now, %s, which Pokemon do you want?" % player["Name"]
		while starter != "Bulbasaur" and starter != "Charmander" and starter != "Squirtle":
			starter = raw_input("Bulbasaur, Charmander, or Squirtle? ")
		print "You picked %s!" % starter
		print "Congratulations! Your first Pokemon is %s!\n" % starter
		print "Your journey begins! You must defeat Kanto's 8 gym leaders in order"
		print "to face the Elite 4! Become a champion!\n"
		player["Party"].append(starter.upper())
		return player

		
class BlackOut(Scene):
	
	def start(self, player):
		print "%s blacked out!" % player["Name"]
		return player
	
	def conclude(self, player):
		print "Game Over"
		return player

		
class PewterCityGym(Scene):
	
	def __init__(self):
		self.leader = {
			"Name": "Brock",
			"Party": ["GEODUDE", "ONIX"],
			"Party Fainted": False}
		
	def start(self, player):
		print "I'm Brock! I'm Pewter's gym leader! I believe in rock hard"
		print "defense and determination! That's why my Pokemon are all the"
		print "rock-type! Do you still want to challenge me? Fine then!"
		print "Show me your best!\n"
		
		print "***BEAT GYM LEADER IN A BATTLE***\n"
		
		return player
	
	def conclude(self, player):
		print "I took you for granted. As proof of your victory, here's the"
		print "Boulder Badge! That's an official Pokemon League badge!"
		print "Its bearer's Pokemon become more powerful!"
		print "There are all kinds of trainers in the world! You appear to be"
		print "very gifted as a Pokemon trainer! Go to the gym in Cerulean and"
		print "test your abilities!\n"
		return player

		
class CeruleanCityGym(Scene):

	def __init__(self):
		self.leader = {
			"Name": "Misty",
			"Party": ["STARYU", "STARMIE"],
			"Party Fainted": False}
	
	def start(self, player):
		print "Hi, you're a new face! Trainers who want to turn pro have to"
		print "have a policy about Pokemon! What is your approach when you"
		print "catch Pokemon? My policy is an all-out offensive with water-type"
		print "Pokemon!\n"
		
		print "***BEAT GYM LEADER IN A BATTLE***\n"
		
		return player
		
	def conclude(self, player):
		print "Wow! You're too much! All right! You can have the Cascade Badge"
		print "to show you beat me!\n"
		return player

		
class VermillionCityGym(Scene):

	def __init__(self):
		self.leader = "Lt. Surge"
		self.team = {
					"Voltorb": ["Tackle", "Screech", "Sonicboom"],
					"Pikachu": ["Thundershock", "Thunder Wave", "Growl", "Quick Attack"],
					"Raichu": ["Thunderbolt", "Thundershock", "Thunder Wave", "Growl"]}
	
	def start(self, player):
		print "Hey, kid! What do you think you're doing here? You won't live"
		print "long in combat! That's for sure! I tell you kid, electric Pokemon"
		print "saved me during the war! They zapped my enemies into paralysis!"
		print "The same as I'll do to you!\n"
		
		print "***BEAT GYM LEADER IN A BATTLE***\n"
		
		return player
		
	def conclude(self, player):
		print "Whoa! You're the real deal, kid! Fine then, take the"
		print "Thunder Badge!"
		print "A little word of advice, kid! Electricity is sure powerful!"
		print "But, it's useless against ground-type Pokemon!\n"
		return player

		
class CeladonCityGym(Scene):

	def __init__(self):
		self.leader = "Erika"
		self.team = {
					"Victreebel": ["Wrap", "Poisonpowder", "Sleep Powder", "Razer Leaf"],
					"Tangela": ["Bind", "Constrict"],
					"Vileplume": ["Poisonpowder", "Mega Drain", "Sleep Powder", "Petal Dance"]}
	
	def start(self, player):
		print "Hello. Lovely weather isn't it? It's so pleasant."
		print "...Oh dear... I must have dozed off. Welcome. My name is Erika."
		print "I am the leader of Celadon Gym. I teach the art of flower"
		print "arranging. My Pokemon are of the grass-type."
		print "Oh, I'm sorry, I had no idea that you wished to challenge me."
		print "Very well, but I shall not lose.\n"
		
		print "***BEAT GYM LEADER IN A BATTLE***\n"
		
		return player
	
	def conclude(self, player):
		print "Oh! I concede defeat. You are remarkably strong. I must confer"
		print "you the Rainbow Badge."
		print "You are cataloging Pokemon? I must say I'm impressed. I would"
		print "never collect Pokemon if they were unattractive.\n"
		return player
		

class FuchsiaCityGym(Scene):

	def __init__(self):
		self.leader = "Koga"
		self.team = {
					"Koffing": ["Tackle", "Smog", "Sludge", "Smokescreen"],
					"Muk": ["Disable", "Poison Gas", "Minimize", "Sludge"],
					"Koffing": ["Tackle", "Smog", "Sludge", "Smokescreen"],
					"Weezing": ["Smog", "Sludge", "Toxic", "Selfdestruct"]}
	
	def start(self, player):
		print "Fwahahaha! A mere child like you dares to challenge me?"
		print "Very well, I shall show you true terror as a ninja master!"
		print "You shall feel the despair of poison and sleep techniques!\n"
		
		print "***BEAT GYM LEADER IN A BATTLE***\n"
		
		return player
	
	def conclude(self, player):
		print "Humph! You have proven your worth! Here! Take the Soul Badge!\n"
		return player


class SaffronCityGym(Scene):

	def __init__(self):
		self.leader = "Sabrina"
		self.team = {
					"Kadabra": ["Disable", "Psybeam", "Recover", "Psychic"],
					"Mr. Mime": ["Confusion", "Barrier", "Light Screen", "Doubleslap"],
					"Venemoth": ["Poisonpowder", "Leech Life", "Stun Spore", "Psybeam"],
					"Alakazam": ["Psybeam", "Recover", "Psywave", "Reflect"]}
	
	def start(self, player):
		print "I had a vision of your arrival! I have had psychic powers since"
		print "I was a child. I first learned to bend spoons with my mind."
		print "I dislike fighting, but if you wish, I will show you my powers!\n"
		
		print "***BEAT GYM LEADER IN A BATTLE***\n"
		
		return player
	
	def conclude(self, player):
		print "I'm shocked! But, a loss is a loss. I admit I didn't work hard"
		print "enough to win! You earned the Marsh Badge!"
		print "Everyone has psychic power! People just don't realize it!\n"
		return player
		

class CinnabarIslandGym(Scene):

	def __init__(self):
		self.leader = "Blaine"
		self.team = {
					"Growlithe": ["Ember", "Leer", "Take Down", "Agility"],
					"Ponyta": ["Tail Whip", "Stomp", "Growl", "Fire Spin"],
					"Rapidash": ["Tail Whip", "Stomp", "Growl", "Fire Spin"],
					"Arcanine": ["Roar", "Ember", "Take Down", "Fire Blast"]}
					
	def start(self, player):
		print "Hah! I am Blaine! I am the leader of Cinnabar Gym! My fiery"
		print "Pokemon will incinerate all challengers! Hah! You better have"
		print "Burn Heal!\n"
		
		print "***BEAT GYM LEADER IN A BATTLE***\n"
		
		return player
	
	def conclude(self, player):
		print "I have burnt out! You have earned the Volcano Badge!\n"
		return player
		
		
class ViridianCityGym(Scene):

	def __init__(self):
		self.leader = "Giovanni"
		self.team = {
					"Rhyhorn": ["Stomp", "Tail Whip", "Fury Attack", "Horn Attack"],
					"Dugtrio": ["Growl", "Dig", "Sand Attack", "Slash"],
					"Nidoqueen": ["Scratch", "Tail Whip", "Poison Sting", "Body Slam"],
					"Nidoking": ["Tackle", "Horn Attack", "Poison Sting", "Thrash"],
					"Rhydon": ["Stomp", "Tail Whip", "Fissure", "Horn Drill"]}
	
	def start(self, player):
		print "Fwahahaha! This is my hideout! I planned to resurrect Team Rocket"
		print "here! But, you have caught me again! So be it! This time, I'm"
		print "not holding back! Once more, you shall face Giovanni, the greatest"
		print "trainer!\n"
		
		print "***BEAT GYM LEADER IN A BATTLE***\n"
		
		return player
		
	def conclude(self, player):
		print "Ha! That was a truly intense fight! You have won! As proof,"
		print "here is the Earth Badge!"
		print "Having lost, I cannot face my underlings! Team Rocket is"
		print "finished forever! I will dedicate my life to the study of Pokemon!"
		print "Let us meet again some day! Farewell!\n"
		player["Game Over"] = True
		return player

		
scenes = [
	IntroductionGen1(),
	PewterCityGym(),
	CeruleanCityGym(),
	VermillionCityGym(),
	CeladonCityGym(),
	FuchsiaCityGym(),
	SaffronCityGym(),
	CinnabarIslandGym(),
	ViridianCityGym()]


game = Engine(scenes)
game.play(player)