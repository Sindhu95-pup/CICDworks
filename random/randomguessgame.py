import random

class Player:
    def __init__(self, number):
        self.number = number

    def start_game(self):
        randnum = random.randrange(1,10);
        guess = self.number;
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10");
        elif guess == randnum:
            print("Wow that is amazing, you guessed it right!");
        else:
            print("Better luck next time, the random number was: %i " % randnum);


print("Hi, welcome to the randome guess game!");
P1 =  Player(8)
P1.start_game()
