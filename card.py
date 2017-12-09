class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def display(self):
        print(self.toString())

    def toString(self):
        return (str(self.value) + ' ' + self.color)
