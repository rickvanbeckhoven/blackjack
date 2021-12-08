import random
import os
import sys


dealer_cards = []
player_cards = []

while len(dealer_cards) != 2:
	dealer_cards.append(random.randint(1, 11))
	if len(dealer_cards) == 2:
		print("Dealer heeft: ", dealer_cards)

while len(player_cards) != 2:
	player_cards.append(random.randint(1, 11))
	if len(player_cards) == 2:
		print("Jij hebt: ", player_cards)

dealer_sum = dealer_cards[0] + dealer_cards[1]
player_sum = player_cards[0] + player_cards[1]

if dealer_sum == 21:
	print("Dealer heeft gewonnen")

if dealer_sum > 21:
	print("Dealer is kapot, jij wint!")

while player_sum < 21:
	action = str(input("Wil je doorgaan of stoppen?"))
	if action == "doorgaan":
		player_cards.append(random.randint(1, 11))
		player_sum += player_cards[2]
		print("Je hebt: ", player_cards, "oftewel", sum(player_cards))
	else:
		print("De dealer heeft", dealer_sum)
		print("Je hebt: ", player_cards, "oftewel", sum(player_cards))
		if dealer_sum > player_sum:
			print("Verloren!")
			break
		else:
			print("Jij wint!")
			break
if sum(player_cards) > 21:
	print("Busted!")
	

if sum(player_cards) == 21:
	print("BLACKJACK!")
	
if sum(player_cards) < 21 and sum(dealer_cards) > 21:
	print("Gewonnen!")
	