from test import Test
from handEvaluator import HandEvaluator
from card import Card
from colors import Colors

class HandEvaluatorTest(Test):

    def __init__(self):
        Test.__init__(self)
        self.handEvaluator = HandEvaluator()

    def testRoyalFlushIsEvaluatedCorrectly(self):
        self.handEvaluator.cards = [
        Card(1, Colors.CLUB),
        Card(13, Colors.CLUB),
        Card(12, Colors.CLUB),
        Card(11, Colors.CLUB),
        Card(10, Colors.CLUB),
        ]
        self.assertTrue(self.handEvaluator.isRoyalFlush())

        self.handEvaluator.cards = [
        Card(1, Colors.CLUB),
        Card(13, Colors.DIAMOND),
        Card(12, Colors.CLUB),
        Card(11, Colors.CLUB),
        Card(10, Colors.CLUB),
        ]
        self.assertFalse(self.handEvaluator.isRoyalFlush())
