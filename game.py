class Game():
	def check(self, coinFlip, diceRoll, cardPick):
		#Win condigiton is a 6 die roll, heads coing flip, and card is either J of spades or A of Diamonds
		if 	coinFlip == "heads" and \
			diceRoll == 6 and \
			(cardPick == "J of spades" or \
			cardPick == "A of diamonds"): 
			return "Win"
		else:
			return "Lose"