class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def display(self):
        print(str(self.value) + ' ' + self.color)
