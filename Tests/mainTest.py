from deckTest import DeckTest
from gameTest import GameTest

def executeTest(test):
    for name in dir(test):
        if name.startswith('test'):
            method = getattr(test, name)
            method()

executeTest(DeckTest())
executeTest(GameTest())
