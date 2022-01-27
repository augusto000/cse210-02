import time
from game.cardsDeck import CardsDeck

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[Card]):     A list of Card instances.
        is_playing (boolean):   Whether or not the game is being played.
        self.option=''
        total_score (int):      Initial score user starts with.
        lose_points (int):      Points deducted when user misguess.
        earn_points (int):      Points added when user guesses correctly.
    """
    def __init__(self):
        self.cards= CardsDeck(2)
        self.is_playing=True
        self.option=''
        
        #The player starts the game with 300 points.( -Augusto-)
        #This is the magic Score: )
        self.total_score=300
        self.lose_points= 75
        self.earn_points=100
    
    """startgame()
    Initiate the loop which mantains the game running 
    """
    def startgame(self):
        #startgame module Initialize the game.
        while self.is_playing:
            print()
            print("The Card is:", self.cards.first_card().number)
            self.option = input("Higher or Lower? [h/l] ")
            
            #create next card different than the first
            self.cards.check_different()

            print("Next Card was:", self.cards.second_card().number)

            if self.cards.is_higher() and self.option == 'h' or self.cards.is_higher() == False and self.option == 'l':
                self.total_score+=self.earn_points
            else:
                self.total_score-=self.lose_points

            #no negative scores 
            self.no_negative_score()

            print("Your Score is:", self.total_score)
            if self.total_score <= 0:
                self.end_game("You lost!")

            #move next card to current card
            self.cards.move_card()

            continue_option = input("Play again? [y/n] ")
            if continue_option == "n":
                self.end_game("Thanks for playing!")

    """check_if_lost(string)
    Display a message and end game 
    """
    def end_game(self, message):
        print()
        print(message)
        time.sleep(3)
        self.is_playing = False
        exit()

    """no_negative_score()
    Avoid score going below zero 
    """
    def no_negative_score(self):
        if self.total_score <= 0:
            self.total_score = 0