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

executeTest(DeckTest())
executeTest(GameTest())
print('\n--------------------------------------\n')
print(str(count) + '  tests executed')
