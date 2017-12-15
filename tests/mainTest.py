import sys

from deckTest import DeckTest
from gameTest import GameTest

count = 0
def executeTest(test):
    global count
    for name in dir(test):
        if name.startswith('test'):
            count += 1
            method = getattr(test, name)
            method()

returnValue = 0
tests = [DeckTest(), GameTest()]
for test in tests:
    executeTest(test)
    if test.hasFailed:
        returnValue = -1
executeTest(DeckTest())
executeTest(GameTest())
print('\n--------------------------------------\n')
print(str(count) + '  tests executed')
sys.exit(returnValue)
