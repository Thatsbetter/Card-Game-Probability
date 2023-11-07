# from deck import *
#
# deck = Deck()
# command = ""
# player1 = Player()
# player2 = Player()
# hand = Hand(player1,player2)
# while command != "exit":
#
#     command = input()
#     if command == "+":
#         player1.draw(deck.get_card())
#
#     if command == "/":
#         hand.result()

from deck import *
import random
total_hokm1 = []
total_hokm2 = []
for j_ in range(0, 10):
    player1 = Player()
    player2 = Player()
    deck = Deck()
    hokm = deck.cards.suits.__getitem__(randint(0, 3))
    hand_hokm1 = 0
    hand_hokm2 = 0
    dummy_card = Card("","")
    while dummy_card.suit !=hokm:
        dummy_card = random.choice(deck.cards.list)
    player1.draw(dummy_card)

    for k in range(0, 13):
        if k > 0:
            first_option = deck.get_card()
            if first_option.suit == hokm or first_option.number in ["K", "Ace"]:
                player1.draw(first_option)
                deck.get_card()
            else:
                player1.draw(deck.get_card())

        first_option = deck.get_card()
        if first_option.suit == hokm or first_option.number in ["K", "Ace"]:
            player2.draw(first_option)
            deck.get_card()
        else:
            player2.draw(deck.get_card())
    for l_ in player1.drawn:
        if (l_.suit == hokm):
            hand_hokm1 = hand_hokm1 + 1
    for k_ in player2.drawn:
        if (k_.suit == hokm):
            hand_hokm2 = hand_hokm2 + 1
    total_hokm1.append(hand_hokm1)
    total_hokm2.append(hand_hokm2)

print(sum(total_hokm1) / len(total_hokm1))
print(sum(total_hokm2) / len(total_hokm2))
