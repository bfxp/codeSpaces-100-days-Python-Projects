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

#main
shuffle()
cards_dealt = deal(2)
card = cards_dealt[0]
rank = card[1]

#Assigning the values of the rank
if rank == "A":
    value = 11
elif rank == "J" or rank == "Q" or rank == "K":
    value = 10
else:
    value = rank

#Key value
rank_dict = {"rank": rank, "value": value}
print(rank_dict["rank"], rank_dict["value"])
