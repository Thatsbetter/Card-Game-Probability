from random import randint

from random import shuffle

class Deck:
    """Represents a deck of playing cards with functionalities to draw cards."""
    def __init__(self):
        self.cards = []
        self.initialize_deck()

    def initialize_deck(self):
        """Populates a standard deck of cards and shuffles them."""
        suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
        values = list(range(2, 11)) + ["J", "Q", "K", "Ace"]
        self.cards = [Card(str(value), suit) for suit in suits for value in values]
        shuffle(self.cards)  # Shuffle deck on initialization

    def draw_card(self):
        """Draws a card from the deck if available; otherwise, raises an exception."""
        if not self.cards:
            raise Exception("No more cards in the deck.")
        return self.cards.pop()

class Card:
    """Represents a single playing card with a number and suit."""
    def __init__(self, number=None, suit=None):
        self.number = number
        self.suit = suit

    def value(self):
        """Returns the value of the card for some games based on its number."""
        if isinstance(self.number, int):
            return self.number
        elif self.number == "Ace":
            return 11
        else:
            return 10

    def __str__(self):
        return f"{self.number} of {self.suit}"

class Cards:
    """Collection of playing cards."""
    def __init__(self):
        self.list = []
        self.suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
        self.initialize_deck()

    def initialize_deck(self):
        """Populates a standard deck of cards."""
        for suit in self.suits:
            for i in range(2, 11):
                self.list.append(Card(i, suit))
            for j in ["J", "Q", "K", "Ace"]:
                self.list.append(Card(j, suit))

class Player:
    """Represents a player in the game, capable of drawing and holding cards."""
    def __init__(self):
        self.drawn = []

    def draw(self, card):
        """Adds a card to the player's current hand."""
        self.drawn.append(card)

    def sum(self):
        """Calculates and returns the sum of values of drawn cards."""
        return sum(card.value() for card in self.drawn)

    def reset(self):
        """Resets the player's hand to empty."""
        self.drawn = []

    def show_hand(self):
        """Displays the hand of the player."""
        return ', '.join(str(card) for card in self.drawn)

    def count_trump_cards(self, trump_suit):
        """Counts how many trump suit cards the player has."""
        return sum(1 for card in self.drawn if card.suit == trump_suit)

