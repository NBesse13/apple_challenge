import random

class Coin():
	#Random heads/tails output
	def flip(self):
		Outcomes = ["heads", "tails"]
		outcome = Outcomes[random.randint(0,1)]
		return outcome