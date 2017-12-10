from card import Card
from random import shuffle
from player import Player
from colors import Colors

class Deck:
    def __init__(self):
        self.cards = []


    def fill(self):
        for color in Colors:
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

    def length(self):
        return len(self.cards)
