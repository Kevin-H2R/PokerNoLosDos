import sys

from deckTest import DeckTest
from gameTest import GameTest
from handEvaluatorTest import HandEvaluatorTest

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
# tests.append(DeckTest())
# tests.append(GameTest())
tests.append(HandEvaluatorTest())
for test in tests:
    executeTest(test)
    if test.hasFailed:
        returnValue = -1
# executeTest(DeckTest())
# executeTest(GameTest())
print('\n--------------------------------------\n')
print(str(count) + '  tests executed')
<<<<<<< 52efcd479db027644d17a2439315a8c52ba6e43e
sys.exit(returnValue)
=======
sys.exit(-1)
>>>>>>> Test if tests fail when returning -1
