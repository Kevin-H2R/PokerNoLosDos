from deck import Deck
from player import Player
from preflop import Preflop

class Game:
    def __init__(self, baseCash):
        self.baseCash = baseCash
        self.globalPot= 0

        self.deck = Deck()
        self.deck.fill()
        self.deck.shuffle()

        self.initPlayers()

        # to be changed
        self.smallBlind = 10
        self.bigBlind = 20

        self.preflop = Preflop(self.players, self.smallBlind, self.bigBlind)

    def initPlayers(self):
        self.players = []
        self.players.append(Player('Serge Karamazov', self.baseCash))
        self.players.append(Player('Odile Deray', self.baseCash))
        self.players.append(Player('Simon Jérémi', self.baseCash))
        self.players.append(Player('Patrick Bialès', self.baseCash))

    def run(self):
        self.globalPot += self.preflop.run()
        self.emptyPlayersPots()

    def displayPlayers(self):
        for player in self.players:
            player.display()

    def emptyPlayersPots(self):
        for player in self.players:
            player.pot = 0
