import sys

from deck import Deck
from player import Player
from turn import Turn

class Game:
    def __init__(self, baseCash):
        self.baseCash = baseCash
        self.globalPot= 0

        self.deck = Deck()
        self.deck.fill()
        self.deck.shuffle()

        self.initPlayers()
        self.board = []
        # to be changed
        self.smallBlind = 10
        self.bigBlind = 20

    def initPlayers(self):
        self.players = []
        self.players.append(Player('Serge Karamazov', self.baseCash))
        self.players.append(Player('Odile Deray', self.baseCash))
        self.players.append(Player('Simon Jérémi', self.baseCash))
        self.players.append(Player('Patrick Bialès', self.baseCash))

    def run(self):
        # Preflop
        self.globalPot += Turn(self.players, self.board, self.smallBlind, self.bigBlind).run()
        self.emptyPlayersPots()
        self.dealBoardCard(3)
        # Flop
        self.globalPot += Turn(self.players, self.board, self.smallBlind, self.bigBlind).run()
        self.emptyPlayersPots()

        #Turn
        self.globalPot += Turn(self.players, self.board, self.smallBlind, self.bigBlind).run()
        self.emptyPlayersPots()

        #River
        self.globalPot += Turn(self.players, self.board, self.smallBlind, self.bigBlind).run()
        self.emptyPlayersPots()

    def displayPlayers(self):
        for player in self.players:
            player.display()

    def emptyPlayersPots(self):
        for player in self.players:
            player.pot = 0

    def dealBoardCard(self, number):
        for i in range(number):
            self.board.append(self.deck.dealCard())
