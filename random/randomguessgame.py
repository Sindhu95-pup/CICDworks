import random

def start_game():
    
    print("Hi, welcome to the randome guess game!");
    name = input("What's your name:");
    print("Hey %s Would you like to play the game?" % name);
    response = input( "Answer Yes or no:");
    if(response.lower() == 'yes'):
        randnum = random.randrange(1,10);
        print("Guess a number between 1 and 10");
        guess = int(input("Enter the number you guessed:"));
        if guess < 1 and guess > 10:
            print("Please enter a number between 1 and 10");
        elif guess == randnum:
            print("Wow that is amazing, you guessed it right!");
        else:
            print("Better luck next time, the randome number was" %randnum);
    else:
        print("That's fine, Enjoy your day!!");

start_game();

