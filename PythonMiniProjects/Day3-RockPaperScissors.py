## Bryan Xaysanavongphet 11/18/24
##Rock Paper Scissors

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
    
def RPSAlgo():
    
   

def game():
    while True:
        print("Time to play! Please choose an option below.")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        
        guess = input("Please enter your selection: ")
        
        
    
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