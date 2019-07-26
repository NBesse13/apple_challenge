from dice import Dice
from coin import Coin
from deck import Deck, Card
from game import Game
from file import File
import json

i=1
coin = Coin()
dice = Dice()
deck = Deck()
game = Game()
file = File()

#There's a better way to enter the while loop, for sure
#Need to keep running until a win condition is reached
outcome = "Lose"

while outcome == "Lose":

	coinFlip = coin.flip()
	diceRoll = dice.roll()

	deck.shuffle()
	cardPick = deck.pickFirst()
	outcome = game.check(coinFlip,diceRoll, cardPick.show())

	file.buildJSON(i,coinFlip,diceRoll, cardPick.show(),outcome)

	deck.returnCard(cardPick)
	i+=1

file.write()