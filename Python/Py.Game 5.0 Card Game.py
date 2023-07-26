from enum import Enum
from enum import IntEnum
from random import *

full_deck = []
partial_deck = []
player1_cards = []
player2_cards = []
# player3_cards = []
# player4_cards = []

# Card enum for playing cards
class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

# Suit enum for playing cards
class Suit(Enum):
    SPADES = "spades"
    CLUBS = "clubs"
    HEARTS = "hearts"
    DIAMONDS = "diamonds"

# class to hold card info per card
class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

# Function to deal full deck of cards
def create_deck():
    for suit in Suit:
        for card in Card:
         full_deck.append(PlayingCard(Card(card), Suit(suit)))
    return full_deck

# Draw single card from "deck"
def draw_card(deck):
    rand_card = randint(0, len(deck) -1)
    return deck.pop(rand_card)

# ************** change BELOW this part for different card game ***************

# This Card Game Is Only For War
def deal_war():
    while(len(partial_deck) > 0):
        player1_cards.append(draw_card(partial_deck))
        player2_cards.append(draw_card(partial_deck))

# ************** change ABOVE this part for different card game ***************


create_deck()
partial_deck = list(full_deck)

# ************** change BELOW this part for different card game ***************

deal_war()

for i in range(0, len(player1_cards)):
    if (player1_cards[i].card > player2_cards[i].card ):
        print("Player 1 Wins \(^0^)/ with: ", player1_cards[i].card)
        print("Player 2 Loses with: ", player2_cards[i].card)
    if (player1_cards[i].card < player2_cards[i].card ):
        print("\(^0^)/ Player 2 Wins with: ", player2_cards[i].card)
        print("Player 1 Loses with: ", player1_cards[i].card)

    else:
        print("ITSSS TIME FOR WARRRR")



# ************** change ABOVE this part for different card game ***************


#for i in range(0, len(full_deck)):
 #   print("Card: ", full_deck [i].card)
  #  print("Suit: ", full_deck[i].suit)
