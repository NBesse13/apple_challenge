winning_flip = "heads"
winning_roll = 6
winning_cards = ["J of spades", "A of diamonds"]
class Game():
	def check(self, coinFlip, diceRoll, cardPick):
		#Win conditon is a 6 die roll, heads coing flip, and card is either J of spades or A of Diamonds
		if 	coinFlip == winning_flip and \
			diceRoll == winning_roll and \
			(cardPick in winning_cards): 
			return "Win"
		else:
			return "Lose"