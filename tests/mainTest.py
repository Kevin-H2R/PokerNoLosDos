import sys

from deckTest import DeckTest
from gameTest import GameTest
from handEvaluatorTest import HandEvaluatorTest
from cardTest import CardTest

count = 0
def executeTest(test):
    global count
    for name in dir(test):
        if name.startswith('test'):
            count += 1
            method = getattr(test, name)
            method()

returnValue = 0
tests = []
tests.append(DeckTest())
tests.append(GameTest())
tests.append(HandEvaluatorTest())
tests.append(CardTest())
for test in tests:
    executeTest(test)
    if test.hasFailed:
        returnValue = -1
print('\n--------------------------------------\n')
print(str(count) + '  tests executed')
sys.exit(returnValue)
