from game.cards import Cards
#class Director 
class Director:
    
    def __init__(self):
        self.cards=[]
        self.is_playing=True
        #This loop is just in case it is needed and as an example. it loads rooms for a card object .
        #for i in range(13):
        #    cards = Cards()
        #    self.cards.append(cards)
        #print("dentro del init de la Clase Director")
        ####print(f"Espacio en memoria  para la {i}° carta  ",self.cards[i])
    
    def startgame(self):
        #startgame module Initialize the game.
        while self.is_playing:

            card = Cards()
            print("------------------------------")
            print()
            print()
            #card.player_choice look for the choice of the player.
            print("The card is : ", card.player_choice())

            #Run check_if_lost function and see if game ends
            if self.check_if_lost(self) is True:
                break

            p = input("Do want to play? [y/n] ")          
            if p.lower() != "n":
                self.is_playing = False
                print("The game is over.")
                print("Thank you and came back soon!")

    #create function to check if the user loses
    def check_if_lost(self):
        if self.cards.total_score <= 0:
            print('You no longer have enough score to play.')
            print("The game is over.")
            print("Thank you and came back soon!")
            return True
        else: 
            return False

'''
from game.cards import Cards
class Director:
    
    def __init__(self):
        self.cards=[]
        self.isPlaying=True

        for i in range(13):
            cards = Cards()
            self.cards.append(cards)
        print("dentro del init de la Clase Director")
           ### #print(f"Espacio en memoria  para la {i}° carta  ",self.cards[i])
    
    def startgame(self):
        while self.isPlaying:
            card = Cards()
            print("------------------------------")
            print()
            print()
            #print("The card is : ", card.player_choice())
            

            p = input("Do you Play  y / n ?")          
            if p.lower() != "y":
                self.isPlaying = False
                print(" Game is Over ")
                print("Thank you and cameback soon!")    

'''
