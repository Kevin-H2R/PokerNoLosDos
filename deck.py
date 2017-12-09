from card import Card
from random import shuffle
from player import Player

class Deck:
    def __init__(self):
        self.cards = []


    def fill(self):
        for color in ['H', 'D', 'S', 'C']:
            for value in range(1, 14):
                self.cards.append(Card(value, color))

    def display(self):
        for card in self.cards:
            card.display()

    def shuffle(self):
        shuffle(self.cards)

    def dealCard(self):
        card = self.cards.pop()
        return card
