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
        if card == 14:card = "A"
        hand.append(card)
    return hand

def total(hand):
    total = 0
    for card in hand:
        if card is "B" or card is "V" or card is "K":
            total += 10
        elif card is "A":
            if total >= 10:
                total += 1
            else: total += 11
        else: total += card
    return total