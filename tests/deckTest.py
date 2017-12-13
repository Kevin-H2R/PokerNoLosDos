import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from test import Test
from deck import Deck
from player import Player

class DeckTest(Test):

    def __init__(self):
        self.deck = Deck()
        self.player = Player('Test Tset', 5000)

    def testDeckShouldDealCardToPlayerCorrectly(self):
        self.deck.fill()
        self.player.addCard(self.deck.dealCard())
        self.assertEqual(self.player.card1.toString(), '13 CLUB' )
        self.assertNone(self.player.card2)
