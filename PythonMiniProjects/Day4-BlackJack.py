##Bryan Xaysanavongphet 11/18
##Black Jack Game

import random

def drawCards():
    return random.cards(["A","2","3","4","5","6","7","8","9","10","Jack","Queen","King",])

def drawCardType():
    return random.cardType(["Spades", "Diamonds", "Heart", "Club"])

def cardResult():
    print(f"{drawCards()} of {drawCardType()}'s")

def play():

def win():

def rules():
    print("Welcome to Black Jack.")
    print("If you have not played before, the rules are simple.")
    print("You are given two cards, and they must total to the amount of 21.")
    print("Aces are considered either the amount of 1 or 11.")
    print("Your goal is to get to 21 or achieve a higher number than the opponent(dealer)")
    print("If you go over 21, you automatically bust and lose.")
    print("If the opponent(dealer) get's a higher number than you, then you will lose as well.")
    print("Good luck! Have fun playing.")
    

if __name__ == "__main__":
    while True:
        print("----------------------------")
        print("Welcome to BlackJack!")
        print("Please select an option below.")
        print("1. Play BlackJack")
        print("2. Rules")
        print("3. Quit")

        userChoice = input("Please choose an option: ")
        
        if(userChoice ==  "1"):
            play()
        elif (userChoice == "2"):
            rules()
        elif (userChoice == "3"):
            print("Thank you for playing!")
            break
        else:
            print("Invalid selection. Please try again.")
        