from dice import Dice
from coin import Coin
from deck import Deck, Card
from game import Game
import json

coin = Coin()
dice = Dice()
deck = Deck()
game = Game()

iterations = 10000

open("test_results.txt","a+")
open("card_results.txt","a+")

coinFlips = {
	'heads': 0,
	'tails': 0
}

diceRolls = {
	'1': 0,
	'2': 0,
	'3': 0,
	'4': 0,
	'5': 0,
	'6': 0
}
cardPicks = {}

for card in deck.cards:
	cardPicks[card.show()] = 0

#Running through the outcomes 10 x 10k
for x in range(0,10):
	for i in range(0,iterations):
		coinFlip = coin.flip()
		coinFlips[coinFlip] += 1

		diceRoll = dice.roll()
		diceRolls[str(diceRoll)] += 1

		deck.shuffle()
		cardPick = deck.pickFirst()
		cardPicks[cardPick.show()] += 1
		deck.returnCard(cardPick)

	with open('test_results.txt',"a") as result_file:
		result_file.write('Run ' + str(x+1) + str(coinFlips) +' '+ str(diceRolls) +'\n')
	with open('card_results.txt',"a") as card_results_file:
		card_results_file.write('Run '+ str(x+1) + str(cardPicks))

	#Resetting the count of outcomes
	coinFlips = {
	'heads': 0,
	'tails': 0
	}

	diceRolls = {
	'1': 0,
	'2': 0,
	'3': 0,
	'4': 0,
	'5': 0,
	'6': 0
	}
	for card in deck.cards:
		cardPicks[card.show()] = 0