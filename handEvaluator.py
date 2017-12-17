from card import Card
from colors import Colors

class HandEvaluator:

    def __init__(self):
        self.cards = []

    def evaluate(self, card1, card2, board):
        self.cards = self.allCardsToArray(card1, card2, board)

    def isRoyalFlush(self):
        foundAce = None
        for card in self.cards:
            if card.value == 1:
                foundAce = card.color
                break
        if foundAce is  None:
            return False
        for i in range(10, 14):
            if Card(i, foundAce) not in self.cards:
                return False
        return True

    def allCardsToArray(self, card1, card2, board):
        board.append(card1)
        board.append(card2)
        return board
