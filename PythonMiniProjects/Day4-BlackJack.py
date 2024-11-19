##Bryan Xaysanavongphet 11/18
##Black Jack Game

import random

#Drawing cards for the face value
def drawCards():
    return random.randint(1,13)

#Drawing for the type of cards
def drawCardType():
    return random.cardType(["Spades", "Diamonds", "Heart", "Club"])

#Putting the face value and card type together into a string for the user to read.
def cardResult():
    print(f"{drawCards()} of {drawCardType()}'s")
    
#Function for adding up the totals of the cards.
# def cardTotal():
#     Card = 1
#     AceCard = "Ace"
#     JackCard = "Jack"
#     QueenCard = "Queen"
#     KingCard = "King"
    
#     drawCards()
    
#     while True:
#         if drawCards() == 1:
#             Card = 1
#         elif drawCards() == 2:
#             Card = 2
#         elif drawCards() == 3:
#             Card = 3
#         elif drawCards() == 4:
#             Card = 4
#         elif drawCards() == 5:
#             Card = 5
#         elif drawCards() == 6:
#             Card = 6
#         elif drawCards() == 7:
#             Card = 7
#         elif drawCards() == 8:
#             Card = 8
#         elif drawCards() == 9:
#             Card = 9
#         elif drawCards() == 10:
#             Card = 10
#         elif drawCards() == 11:
#             Card = 11
#             JackCard
#         elif drawCards() == 12:
#             Card = 12
#             QueenCard
#         elif drawCards() == 13:
#             Card = 13
#             KingCard
#         else:
#             break
        
        
#Dealer cards. Will have to draw cards until 17 or higher.
def dealer():
    card1 = drawCards()
    card2 = drawCards()
    #cardtype1 = drawCardType()
    #cardtype2 = drawCardType()
    #cardresult1 = cardResult()
    #cardresult2 = cardResult()
    
    totalcard = card1 + card2
    #displayCard = cardresult1 + cardresult2
    print(f"The Dealer's cards are {card1} and {card2}. The total is: {totalcard}")
    #print(displayCard)
    
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
        