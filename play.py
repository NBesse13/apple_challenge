from dice import Dice
from coin import Coin
from deck import Deck, Card
from game import Game
from file import File
import time 
import json

#Initializing class instances required and try counter, useful for debugging and statistic calculations
i=1
coin = Coin()
dice = Dice()
deck = Deck()
game = Game()
file = File()

outcome = "Lose"
#Keep playing until win
while outcome == "Lose":
	try:
		#Retrieving coin flip and dice roll value
		coinFlip = coin.flip()
		diceRoll = dice.roll()

		#Shuffling the deck and picking the first card
		deck.shuffle()
		cardPick = deck.pickFirst()

		#Passing the values to the game class for checking outcome
		outcome = game.check(coinFlip,diceRoll, cardPick.show())

		#Building the JSON object to write to output file
		file.buildJSON(i,coinFlip,diceRoll, cardPick.show(),outcome)

		#Returning the top card to the bottom of the pile
		deck.returnCard(cardPick)
		i+=1
		time.sleep(1)
	except KeyboardInterrupt:
		file.keyboardInterrupt(i)
		file.write()
		raise 


#Writing the full JSON object to the file
file.write()