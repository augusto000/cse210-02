from game.cards import Cards
class Director:
    
    def __init__(self):
        self.cards=[]
        self.isPlaying=True

        for i in range(13):
            cards = Cards()
            self.cards.append(cards)
        #print("dentro del init de la Clase Director")
           ### #print(f"Espacio en memoria  para la {i}° carta  ",self.cards[i])
    
    def startgame(self):
        while self.isPlaying:
            card = Cards()
            print("------------------------------")
            print()
            print()
            print("The card is : ", card.player_choice())

            p = input("Do you Play  y / n ?")          
            if p.lower() != "y":
                self.isPlaying = False
                print(" Game is Over ")
                print("Thank you and cameback soon!") 

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
