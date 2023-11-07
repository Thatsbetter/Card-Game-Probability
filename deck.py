from random import randint


class Deck:
    def __init__(self):
        self.new_cards()

    def new_cards(self):
        self.cards = Cards()

    def get_card(self):
        # if len(self.cards.list) < 2:
        #     self.new_cards()
        #     print("new deck of cards")
        if len(self.cards.list) < 1:
            raise Exception("cards finished")
        random_int = randint(0, len(self.cards.list) - 1)
        random_card = self.cards.list.__getitem__(random_int)
        self.cards.list.pop(random_int)
        return random_card


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def value(self):
        if isinstance(self.number, int):
            return self.number
        elif self.number == "Ace":
            return 11
        else:
            return 10

    def __str__(self):
        return (f"{self.number} {self.suit}")

    def __add__(self, other):
        return self.value() + other.value()



class Cards:
    def __init__(self):
        self.list = []
        self.suits = ["♣ Clubs", "♥ Hearts", "♦ Diamonds", "♠ Spades"]
        for suit in self.suits:
            for i in range(2, 11):
                self.list.append(Card(i, suit))
            for j in ["J", "Q", "K", "Ace"]:
                self.list.append(Card(j, suit))


class Player:
    def __init__(self):
        self.drawn = []

    def draw(self, card: Card):
        self.drawn.append(card)

    def sum(self):
        sum = 0
        for i in self.drawn:
            sum = i.value() + sum
        print(sum)
        return sum

    def reset(self):
        self.drawn = []


class Hand:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def result(self):
        if self.player1.sum() > self.player2.sum():
            if self.player1.sum() <= 21:
                print("player 1 wins")
        elif self.player1.sum() < self.player2.sum():
            if self.player2.sum() <= 21:
                print("player 2 wins")
        else:
            print("draw")

        self.player1.reset()
        self.player2.reset()

