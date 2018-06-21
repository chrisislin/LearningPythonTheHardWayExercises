from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print"Default scene"
		exit(1)

class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	def play(self):
		current_scene = self.scene_map.opening_scene()
		while True:
			print "\n-----"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
	death = [
		"You died",
		"Yep, you are indeed dead"
		]
	def enter(self):
		print Death.death[randint(0,len(self.death)-1)]
		exit(1)

class CentralCorridor(Scene):
	def enter(self):
		print "You see a guy pointing a gun"
		action = raw_input("> ")
		if action == "shoot!":
			print "you killed him, jk he ate you first"
			return 'death'

		elif action == "dodge!":
			print "You didn't learn how to dodge."
			return 'death'
		elif action == "tell a joke":
			print "He laughs till he dies."
			return 'laser_weapon_armory'
		else:
			print "Pick an action"
			return 'central_corridor'
class LaserWeaponArmory(Scene):
	def enter(self):
		print "Wahwowewah"
		code = "%d%d%d" %(1,2,3)
		#(randint(1,9),randint(1,9),randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print "BZZ"
			guesses += 1
			guess = raw_input("[keypad]> ")

		if guess == code:
			print"open"
			return 'the_bridge'
		else:
			print "Explodes"
			return 'death'

class TheBridge(Scene):
	def enter(self):
		print "Enter"
		action = raw_input("> ")

		if action == "throw bomb":
			print "lol"
			return 'death'

		elif action == "slow bomb":
			print "Ya"
			return 'escape_pod'
		else:
			print "Uh-oh"
			return 'the_bridge'


class EscapePod(Scene):
	def enter(self):
		print "exit"
		good_pod = 1
		#randint(1,5)
		guess = raw_input("[pod #]> ")
		if int(guess) != good_pod:
			return 'death'
		else:
			return 'finished'

class Map(object):
	scenes = {
	'central_corridor': CentralCorridor(),
	'laser_weapon_armory': LaserWeaponArmory(),
	'the_bridge': TheBridge(),
	'escape_pod': EscapePod(),
	'death': Death()
	}
	def __init__(self, start_scene):
		self.start_scene = start_scene
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()