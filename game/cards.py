import random

class Cards:
    def __init__(self):
        self.number = 0
        self.shuffle()
    
    def shuffle(self):
        self.number = random.randint(1, 13)