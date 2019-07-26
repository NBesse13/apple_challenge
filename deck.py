import random

suits = ['clubs', 'hearts', 'spades', 'diamonds']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10' ,'J', 'Q', 'K']
# values = ['A', 'J']

class Card:
	def __init__(self,suit,value):
		self.suit = suit
		self.value = value

	def show(self):
		return ("{} of {}".format(self.value, self.suit))

class Deck(Card):
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for suit in suits:
			for value in values:
				self.cards.append(Card(suit,value))

	def show(self):
		for card in self.cards:
			card.show()

	def shuffle(self):
		cards = random.shuffle(self.cards)

	def pickFirst(self):
		return self.cards.pop(0)

	def returnCard(self, pick):
		return self.cards.append(pick)