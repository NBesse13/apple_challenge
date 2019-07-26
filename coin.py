import random
#Considering initing with a value and flipping reassigns a random value

class Coin():
	def flip(self):
		Outcomes = {
		'1': "heads",
		'2': "tails",
		}
		outcomeInt = random.randint(1,2)
		outcome = Outcomes.get(str(outcomeInt))
		return outcome