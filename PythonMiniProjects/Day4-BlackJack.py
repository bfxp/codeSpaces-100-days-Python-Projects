##Bryan Xaysanavongphet 11/18
##Black Jack Game

import random

#Drawing cards for the face value
def drawCards():
    return random.randint(1,13)
        
#Dealer cards. Will have to draw cards until 17 or higher.
def dealer():
    card1 = drawCards()
    card2 = drawCards()
    
    totalcard = card1 + card2
    #displayCard = cardresult1 + cardresult2
    print(f"The Dealer's cards are {card1} and {card2}. The total is: {totalcard}")
    #print(displayCard)
    while True:
        if totalcard < 17:
            print("The dealers cards are lower than 17. Pulling another card...")
            card3 = drawCards()
            totalcard = totalcard + card3
            print(f"The dealers cards are now: {totalcard}")
        elif totalcard == 21:
            print("The dealer got 21! You lose.")
        elif totalcard > 21:
            print("The dealer busted. You win!")
        else:
            return
        
    
#Main game play. User will either keep drawing cards until 21 or stand if they like their number.
#def play():


#Rules to explain to the user how to play.
def rules():
    print("Welcome to Black Jack.")
    print("If you have not played before, the rules are simple.")
    print("You are given two cards, and they must total to the amount of 21.")
    print("Aces are considered either the amount of 1 or 11.")
    print("Your goal is to get to 21 or achieve a higher number than the opponent(dealer)")
    print("If you go over 21, you automatically bust and lose.")
    print("If the opponent(dealer) get's a higher number than you, then you will lose as well.")
    print("Good luck! Have fun playing.")
    

#Main
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
            dealer()
        elif (userChoice == "2"):
            rules()
        elif (userChoice == "3"):
            print("Thank you for playing!")
            break
        else:
            print("Invalid selection. Please try again.")
        