import random
import os

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "B"
        if card == 12:card = "V"
        if card == 13:card = "K"
        hand.append(card)
    return hand

