#Bryan Xaysanavongphet
#11/19/24
#Going off of https://www.youtube.com/watch?v=aryte85bt_M

import random

cards = []
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

ranks = [
        {"rank": "A", "value": 11},
        {"rank": "2", "value": 2},
        {"rank": "3", "value": 3},
        {"rank": "4", "value": 4},
        {"rank": "5", "value": 5},
        {"rank": "6", "value": 6},
        {"rank": "7", "value": 7},
        {"rank": "8", "value": 8},
        {"rank": "9", "value": 9},
        {"rank": "10", "value": 10},
        {"rank": "J", "value": 10},
        {"rank": "Q", "value": 10},
        {"rank": "K", "value": 10},
    ]

#for lop to add the suit and rank
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

#main
shuffle()

card = deal(1)[0]
print(card)