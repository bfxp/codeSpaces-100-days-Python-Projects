#Bryan Xaysanavongphet
#11/19/24
#Going off of https://www.youtube.com/watch?v=aryte85bt_M

import random

cards = []
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K",]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])
        
#Function for shuffling the cards.
def shuffle():
    random.shuffle(cards)

#Deal function to deal one card. Creating the deal function to accept an argument within the parameters.
def deal(number):
    #Creating a cards dealt array
    cards_dealt = []
    #This will add a card into the deck for each card that has been dealt.
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()
cards_dealt = deal(2)
print(cards_dealt)
