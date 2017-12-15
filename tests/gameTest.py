from test import Test
from game import Game
class GameTest(Test):

    def __init__(self):
        Test.__init__(self)
        self.game = Game(5000)

    def testBoardCardAreDealtCorrectly(self):
        self.game.dealBoardCard(3)
        self.assertEqual(3, len(self.game.board))
        self.assertEqual(49, self.game.deck.length())
        for card in self.game.board:
            self.assertNotIn(card, self.game.deck.cards)
