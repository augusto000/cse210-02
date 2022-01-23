import random

class Cards:
    def __init__(self):
        self.total_score=300
        self.lose_points= 75
        self.earn_points=100
        self.previous_number = 0
        self.current_number = 0
        self.number = 0
    
    def get_card_num(self):
        # this function each time that is called return a 
        # random number(1 to 13)#
        self.number = random.randint(1, 13)
        return self.number   

    def player_choice(self):
        #The player guesses if the next one will be higher or lower. (Julia)
        self.previous_number = self.get_card_num()
        print("The Card is: ", self.previous_number)
        opt = input("Higher or Lower? [h/l] ")
        self.current_number = self.get_card_num()
        print("Next Card was: ",self.current_number)
        
        if  self.current_number > self.previous_number and opt == "h":
            self.total_score += self.earn_points
            print("You win!")
            print("Your Score is: ", self.total_score)
        elif  self.current_number > self.previous_number and opt == "l":
            self.total_score -= self.lose_points
            print("You lose!")
            print("Your Score is: ", self.total_score)
        elif  self.current_number < self.previous_number and opt == "l":
            self.total_score += self.earn_points
            print("You win!")
            print("Your Score is: ", self.total_score)
        elif  self.current_number < self.previous_number and opt == "h":
            self.total_score -= self.lose_points
            print("You lose!")
            print("Your Score is: ", self.total_score)
        else:
             print("Your Score is: ", self.total_score)
                       
print()
card = Cards()
for i in range (4):
    card.player_choice()
