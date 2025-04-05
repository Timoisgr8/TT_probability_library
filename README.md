My python library:

pip install TT-probability-package

This library has a few common items used in probabilistic settings. This includes:
 - Deck of Cards
 - Dice
 - Coin

Additionally the package is equip with an analyser module with useful functions.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

analyser_module:

Defines an Analyser class that has useful functions for analysis.

print_results(self, your_results):
Print the tracked results with unique item counts.

matches_any(self, card, pattern):
Check if the card matches a pattern using regular expressions.

count(self, your_results, items):
Count the occurrences of each item in the provided list within `your_results`, allowing regex patterns.
:param your_results: List of observed results.
:param items: List of items (or patterns) to count in `your_results`.
:return: A list of counts corresponding to each item in `items`.

has(self, your_results, sequence, consecutive=False, ordered=False):
Check if a given sequence exists in the your results.
:param sequence: List of values to check for in results.
:param consecutive: If True, requires the sequence to appear consecutively.
:param ordered: If True, requires the sequence to appear in order but allows gaps.
:return: True if the sequence is found according to the given conditions, otherwise False.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


card_deck_module:

Defines a CardDeck class to simulate a standard 52 Deck of Cards.The deck can be customised if provided a list of cards e.g. ['AH', '2H', '3H'] representing a deck containing 3 cards (Ace of Hearts, 2 of Hearts, 3 of Hearts).

__init__(self, suits=None, ranks=None, custom_deck=None):
Initialises a deck of cards. Can be provided a custom deck on initialisation.

set_custom_deck(self, custom_deck):
Set a custom deck using a list of strings in the format 'RankSuit'
:param custom_deck: List of cards for custom deck.

shuffle(self):
Shuffle the deck.

draw(self, n=1):
Draw n cards from the deck

reset_deck(self):
Reset the deck to its original state (custom if specified) otherwise a regular 52 deck and shuffle.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

coin_module.py

Defines an Coin class that can flip.

__init__(self, head_p=0.5):
Creates a standard fair coin. The probability of a heads changed be changed by editting a head_p value.

flip(self):
Flip the coin and return 'H' or 'T'.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

dice_module.py

Defines a Dice class that can be rolled. It can have n sides and the weights of each face can be altered. 

class Dice:
__init__(self, n_faces=6, face_values=None, fair=True, relative_weights=None):
Initialise the Dice object.

:param n_faces: Number of faces on the die.
:param face_values: List of face values. If None, generates [1, 2, ..., n_faces].
:param fair: If True, assigns equal probability to each face.
:param relative_weights: List of weights for each face (used if fair=False).


def roll(self):
Roll the dice and return the result.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

game_simulation_module

Defines a GameSimulation class that can be provided a result_func that will be run by default 10000 times.

def __init__(self, result_func, variable_names, trials=10000):
Initialise the simulation environment for tracking event probabilities.

:param result_func: Function that simulates the game or event, returning a dictionary of results.
:param variable_names: List of variable names to track (e.g., event counts).
:param trials: Number of trials to run the simulation (default: 10,000).

       
update_plot(self):
Update the plot with the current values of the simulation.

run_result_func(self):
Run the result function in parallel to simulate trials.

def run(self):
Start both threads for running result_func and updating the plot
