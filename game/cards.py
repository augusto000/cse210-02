import random

class Cards:
    def __init__(self):
        self.total_score=300
        self.lost_points= 75
        self.earn_points=100
        self.previusNumber = 0
        self.currentNumber = 0
        self.numner = 0
    
    def get_card_num(self):
        # this function each time that is called return a 
        # random number(1 to 13)#
        self.number = random.randint(1, 13)
        return self.number   

    def player_choice(self):
        #The player guesses if the next one will be higher or lower. (Julia)
        print("The Card is : ",self.get_card_num())
        opt = input("Higher or Lower [h/l] ? :")
        self.currentNumber = self.get_card_num()
        print("Next Card was : ",self.currentNumber)
        
        if  self.currentNumber > self.previusNumber and opt == "h":
            self.total_score += self.earn_points
            print("You wins!")
            print("Your Score is : ", self.total_score)
        elif  self.currentNumber > self.previusNumber and opt == "l":
            self.total_score -= self.lost_points
            print("You lose!")
            print("Your Score is : ", self.total_score)
        elif  self.currentNumber < self.previusNumber and opt == "l":
            self.total_score += self.earn_points
            print("You wins!")
            print("Your Score is : ", self.total_score)
        elif  self.currentNumber < self.previusNumber and opt == "h":
            self.total_score -= self.lost_points
            print("You lose!")
            print("Your Score is : ", self.total_score)
        else:
             print("Your Score is : ", self.total_score) 

'''
import random

class Cards:
    def __init__(self):
        self.totalScore=300
        self.lost_points= 75
        self.win_points=100
        self.previusNumber = 0
        self.currentNumber = 0

    def getTotalScore(self):
        return self.totalScore    
        
    def getPreviusCardNumber(self):
        # this function each time that is called return a 
        # random number(1 to 13)#
        self.previusNumber = random.randint(1, 13)
        return self.previusNumber

    def getCurrentCardNumber(self):
        # this function each time that is called return a 
        # random number(1 to 13)
        self.currentNumber = random.randint(1, 13)
        return self.currentNumber

    def getReadyPlayer(self):
        return self.player  

    def player_choice(self):

        #The player guesses if the next one will be higher or lower. (Julia)
        print("The Card is : ",card.getPreviusCardNumber())
        opt = input("Higher or Lower [h/l] ? :")
        self.currentNumber = card.getCurrentCardNumber()
        print("Next Card was : ",self.currentNumber)
        
        if  self.currentNumber > self.previusNumber and opt == "h":
            self.totalScore += self.win_points
            print("You wins !!")
            print("Your Score is : ", self.totalScore)
        else:
            print("You lost !!")
            self.totalScore -= self.lost_points
            print("Your Score is : ", self.totalScore)                   
print()
card = Cards()
card.player_choice()          
'''
