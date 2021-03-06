from card import Card

class Player:
    def __init__(self, name, cash):
        self.name = name
        self.card1 = None
        self.card2 = None
        self.cash = cash
        self.pot = 0

    def bet(self, value):
        # We put back what's in pot to cash
        self.cash += self.pot
        diff = self.cash - value
        if diff > 0:
            self.cash = diff
            self.pot = value
        else:
            self.cash = 0
            self.pot = value + diff

    def decide(self, board, lastBet):
        # -1 = flop
        # lastBet = call
        # > lastBet = raise
        return lastBet

    def display(self):
        print(self.name + ': cash = ' + str(self.cash) + ', pot = ' + str(self.pot))

    def addCard(self, card):
        if self.card1 == None:
            self.card1 = card
        else:
            self.card2 = card

    def displayCards(self):
        text1 = self.card1.toString() if self.card1 != None else 'NONE'
        text2 = self.card2.toString() if self.card2 != None else 'NONE'
        print(text1 + ' - ' + text2)
