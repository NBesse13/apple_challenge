import random

outcomes = ["heads", "tails"]

class Coin():
	#Random heads/tails output
	def flip(self):
		outcome = outcomes[random.randint(0,1)]
		return outcome