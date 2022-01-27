import copy
import time
from game.card import Card

class CardsDeck:
    """Deck of Cards 
    This class holds several Card elements.

    Attributes:
        number (int):       Value of the card instance.
        get_card_number():  Assign random number to the card instance. 
    """
    def __init__(self, amount):
        self.cards = []

        #initialize cards
        for i in range(amount):
            self.cards.append(Card())
    
    def first_card(self):
        return self.cards[0]

    def second_card(self):
        return self.cards[1]

    def check_different(self):
        while self.second_card().number == self.first_card().number:
            self.second_card().get_card_num()

    def is_higher(self):
        if self.second_card().number > self.first_card().number: return True
    
    def move_card(self):
        self.cards[0] = copy.deepcopy(self.cards[1])