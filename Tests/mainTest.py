from deckTest import DeckTest

deckTest = DeckTest()
for name in dir(deckTest):
    if name.startswith('test'):
        method = getattr(deckTest, name)
        method()
