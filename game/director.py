from game.cards import Cards
import time
import copy

class Director:
    
    def __init__(self):
        self.cards=[]
        self.is_playing=True

        self.option=''
        self.total_score=300
        self.lose_points=75
        self.earn_points=100

        #initialize two cards
        for i in range(2):
            card = Cards()
            self.cards.append(card)

    def startgame(self):
        while self.is_playing:
            self.get_user_input()
            self.do_updates()

    def get_user_input(self):
        print()
        print("The Card is:", self.cards[0].number)
        self.option = input("Higher or Lower? [h/l] ")

    def do_updates(self):
        #create next card different than the first
        while self.cards[1].number == self.cards[0].number:
            self.cards[1].shuffle()

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
            self.finish_game("You lost!")

        #move next card to current card
        self.cards[0] = copy.deepcopy(self.cards[1])

        continue_option = input("Play again? [y/n] ")
        if continue_option == "n":
            self.finish_game("Thanks for playing!")
    
    def finish_game (self, message):
        print()
        print(message)
        time.sleep(3)
        self.is_playing = False
        exit()