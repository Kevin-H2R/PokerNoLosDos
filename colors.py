from enum import Enum

class Colors(Enum):
    SPADE = 1
    HEART = 2
    DIAMOND = 3
    CLUB = 4

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented