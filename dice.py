import random
#Considering initing the dice with a vlaue and having the roll reassign
class Dice():
	# def __init__(self):
	# 	self.value = value

	def roll(self):
		roll = random.randint(1,6)
		return roll