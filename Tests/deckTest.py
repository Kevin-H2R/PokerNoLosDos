import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from test import Test
from deck import Deck
from player import Player
import inspect

class DeckTest(Test):

    def __init__(self):
        self.deck = Deck()
        self.player = Player('Test Tset', 5000)

    def testDeckShouldDealCardToPlayerCorrectly(self):
        self.deck.fill()
        self.player.addCard(self.deck.dealCard())
        self.assertEqual(self.player.card1.toString(), '13 C' , inspect.stack()[0][3])
        self.assertNone(self.player.card2, inspect.stack()[0][3])
