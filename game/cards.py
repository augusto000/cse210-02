import random

class Cards:
    def _init_(self):
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
        self.previusNumber = self.get_card_num()
        print("The Card is : ", self.previusNumber)
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
                       
print()
card = Cards()
for i in range (4):
    card.player_choice()
