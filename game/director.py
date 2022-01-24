import copy
import time
from game.cards import Cards

class Director:
    
    def __init__(self):
        self.cards=[]
        self.is_playing=True
        self.option=''
        #The player starts the game with 300 points.( -Augusto-)
        #This is the magic Score: )
        self.total_score=300
        self.lose_points= 75
        self.earn_points=100

        #initialize two cards
        for i in range(2):
            card = Cards()
            self.cards.append(card)
    
    def startgame(self):
        #startgame module Initialize the game.
        while self.is_playing:
            print()
            print("The Card is:", self.cards[0].number)
            self.option = input("Higher or Lower? [h/l] ")
            
            #create next card different than the first
            while self.cards[1].number == self.cards[0].number:
                self.cards[1].get_card_num()

            print("Next Card was:", self.cards[1].number)

            if self.cards[0].number < self.cards[1].number and self.option == 'h' or self.cards[0].number > self.cards[1].number and self.option == 'l':
                self.total_score+=self.earn_points
            else:
                self.total_score-=self.lose_points
            
            #no negative scores 
            if self.total_score <= 0:
                self.total_score = 0

            print("Your Score is:", self.total_score)
            if self.total_score <= 0:
                self.check_if_lost("You lost!")

            #move next card to current card
            self.cards[0] = copy.deepcopy(self.cards[1])
            continue_option = input("Play again? [y/n] ")
            if continue_option == "n":
                self.check_if_lost("Thanks for playing!")


    #create function to check if the user loses
    def check_if_lost(self, message):
        print()
        print(message)
        time.sleep(3)
        self.is_playing = False
        exit()