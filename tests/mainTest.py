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
<<<<<<< abd728a114f02ad5a9df5cc16b0e4ef90d960764
tests = []
# tests.append(DeckTest())
# tests.append(GameTest())
tests.append(HandEvaluatorTest())
=======
tests = [DeckTest(), GameTest()]
>>>>>>> Adds return value to test
for test in tests:
    executeTest(test)
    if test.hasFailed:
        returnValue = -1
<<<<<<< eefaba40db34fb4c2f7b2b4d7816b14bc26c637e
<<<<<<< abd728a114f02ad5a9df5cc16b0e4ef90d960764
# executeTest(DeckTest())
# executeTest(GameTest())
print('\n--------------------------------------\n')
print(str(count) + '  tests executed')
<<<<<<< 52efcd479db027644d17a2439315a8c52ba6e43e
sys.exit(returnValue)
=======
sys.exit(-1)
>>>>>>> Test if tests fail when returning -1
=======
executeTest(DeckTest())
executeTest(GameTest())
=======
# executeTest(DeckTest())
# executeTest(GameTest())
>>>>>>> Fixes unit tests
print('\n--------------------------------------\n')
print(str(count) + '  tests executed')
sys.exit(returnValue)
>>>>>>> Adds return value to test
