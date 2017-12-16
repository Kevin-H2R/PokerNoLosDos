from test import Test
from handEvaluator import HandEvaluator
from card import Card
from colors import Colors

class CardTest(Test):

    def __init__(self):
        Test.__init__(self)
        self.handEvaluator = HandEvaluator()

    def testCardComparison(self):
        actual = [
            Card(6, Colors.CLUB),
            Card(4, Colors.DIAMOND),
            Card(1, Colors.CLUB),
            Card(10, Colors.DIAMOND)
        ]

        expected = [
            Card(4, Colors.DIAMOND),
            Card(10, Colors.DIAMOND),
            Card(1, Colors.CLUB),
            Card(6, Colors.CLUB)
        ]

        actual.sort()
        self.assertEqual(actual, expected)
