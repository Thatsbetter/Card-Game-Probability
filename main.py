from deck import Deck, Player, Card
import random


def simulate_hokm_game(num_simulations):
    total_trump_cards_player1 = 0
    total_trump_cards_player2 = 0

    for _ in range(num_simulations):
        player1, player2 = Player(), Player()
        deck = Deck()

        hokm_suit = random.choice(["Clubs", "Hearts", "Diamonds", "Spades"])  # Randomly choosing hokm suit

        try:
            # Each player has 13 chances to draw 2 cards and choose 1
            for _ in range(13):
                draw_and_choose(player1, deck, hokm_suit)
                draw_and_choose(player2, deck, hokm_suit)
        except Exception as e:
            print(str(e))

        # Counting trump cards
        trump_cards_player1 = player1.count_trump_cards(hokm_suit)
        trump_cards_player2 = player2.count_trump_cards(hokm_suit)

        total_trump_cards_player1 += trump_cards_player1
        total_trump_cards_player2 += trump_cards_player2

    # Calculating averages
    average_trump_cards_player1 = total_trump_cards_player1 / num_simulations
    average_trump_cards_player2 = total_trump_cards_player2 / num_simulations

    print(f"Average trump cards for Player 1 over {num_simulations} games: {average_trump_cards_player1:.2f}")
    print(f"Average trump cards for Player 2 over {num_simulations} games: {average_trump_cards_player2:.2f}")


def draw_and_choose(player, deck, hokm_suit):
    # Draw two cards
    if len(deck.cards) < 2:
        raise Exception("Not enough cards to continue drawing.")
    card1, card2 = deck.draw_card(), deck.draw_card()

    if card1.suit == hokm_suit or card1.number == "Ace":
       player.draw(card1)
    else:
       player.draw(card2)


if __name__ == '__main__':
    num_simulations = 100000
    simulate_hokm_game(num_simulations)