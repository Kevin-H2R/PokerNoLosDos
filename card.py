class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def display(self):
        print(self.toString())

    def toString(self):
        return (str(self.value) + ' ' + self.color.name)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return (self.color, self.value) < (other.color, other.value)
        return NotImplemented
