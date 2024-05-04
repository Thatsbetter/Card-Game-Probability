

# Hokm Card Game Simulation

This repository contains a Python script designed to simulate multiple instances of the card game "Hokm" (also known as "Court Piece"). Hokm is a popular card game originating from Iran, played with a standard deck of 52 cards. The script simulates the game's variation where players have to choose between two drawn cards under specific conditions.

## Overview

The simulation is crafted for educational and experimental purposes to understand the impact of strategic choices in drawing cards under a designated trump suit and explores the factors influencing the game's outcomes, such as the frequency of trump cards in each player's hand.

## Features

- Trump Suit Selection: At the start of each game, a trump suit is randomly selected from the four card suits.
- Card Drawing Mechanism: Players draw two cards per turn and decide which one to keep. The decision algorithm implemented prefers a card of the trump suit or an Ace from any suit.
- Simulation Loop: The script can simulate the game multiple times to gather statistical data on the outcomes.
- Statistics Calculation: After completing the specified number of simulations, the script calculates and displays the average number of trump cards each player has.

## Usage

To run the simulation, ensure you have Python 3 installed on your system. Clone this repository and execute the script from the command line:

bash
python hokm_simulation.py


You can adjust the number of simulations by modifying the `num_simulations` variable in the script.

## Project Structure

The script makes use of three primary classes defined in the `deck.py` (which needs to be correctly set up for this script to function):

- `Deck`: Manages the deck of cards, including shuffling and drawing.
- `Player`: Manages a player's cards and counts the number of trump cards.
- `Card`: Defines the attributes of a playing card, such as its suit and number.

## How It Works

The simulation process is as follows:

1. Randomly determine a trump suit.
2. Each player draws two cards in their turn.
3. Players select one card, preferably a trump suit card or an Ace.
4. This process repeats until each player has made 13 choices.
5. The game calculates the number of trump cards for each player.

At the end of the simulations, the average number of trump cards each player accumulated is computed. 

## Example Output

After simulating 100,000 games, the output may look like this:

Average trump cards for Player 1 over 100000 games: 5.55
Average trump cards for Player 2 over 100000 games: 5.55


## Future Improvements

- Interactive Player Decisions: Implement a system to allow real-time decisions by users during card drawing.
- Expanded Strategy Logic: Enhance card decision-making logic to incorporate more complex strategies.
- Full Game Engine: Incorporate a full game engine to simulate actual gameplay including scoring and other Hokm rules.

## License

This project is under the MIT License 