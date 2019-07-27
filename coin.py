import random

class Coin():
	#Random heads/tails output
	def flip(self):
		Outcomes = {
		'1': "heads",
		'2': "tails",
		}
		outcomeInt = random.randint(1,2)
		outcome = Outcomes.get(str(outcomeInt))
		return outcome