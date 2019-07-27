import random
class Dice():
	#only ever need a random value from a Dice
	def roll(self):
		roll = random.randint(1,6)
		return roll