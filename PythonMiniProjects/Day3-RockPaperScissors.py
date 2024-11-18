## Bryan Xaysanavongphet 11/18/24
## Rock Paper Scissors

import random

#Random function for the opponent
def RPS():
    return random.choice(["Rock", "Paper", "Scissors"])

def rules():
    print("The rules are simple.")
    print("Rock beats Scissors")
    print("Paper beats Rock")
    print("Scissors beats Paper")
    print("Simple enough? I hope so!")
    

def game():
    while True:
        print("--------------------------------------------")
        print("Time to play! Please choose an option below.")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        
        guess = input("Please enter your selection: ")
        opponent = RPS()
        
        if (guess == "1" and opponent == "Rock"):
            print("They were both rock! Please try again.")
        elif (guess == "1" and opponent == "Paper"):
            print("You lose! It was paper.")
        elif (guess == "1" and opponent == "Scissors"):
            print("You win! It was scissors.")
        elif (guess == "2" and opponent == "Rock"):
            print("You win! It was Rock.")
        elif (guess == "2" and opponent == "Paper"):
            print("They were both Paper! Please try again.")
        elif (guess == "2" and opponent == "Scissors"):
            print("It was Scissors! You lose!")
        elif (guess == "3" and opponent == "Rock"):
            print("You lose! It was rock")
        elif (guess == "3" and opponent == "Papers"):
            print("You win! It was paper.")
        elif (guess == "3" and opponent == "Scissors"):
            print("They were both Scissors! Please try again.")
        elif (guess == "4"):
            print("Thank you for playing!")
            break
        else:
            print("Invalid selection. Please select another option.")
    
#Main Function
if __name__ == "__main__":
    while True:
        print("-----------------------------")
        print("Welcome to Rock Paper Scissors!")
        print("Please select an option below.")
        print("1. Play")
        print("2. Rules")
        print("3. Quit")
        print("-----------------------------")
        menu = input("Please select an option: ")
        
        if menu == "1":
            game()
        elif menu =="2":
            rules()
        elif menu == "3":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")