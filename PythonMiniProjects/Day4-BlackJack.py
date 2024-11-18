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
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    

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
        