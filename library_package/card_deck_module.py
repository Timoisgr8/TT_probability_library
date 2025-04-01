import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_suit(self):
        """Return the suit of the card."""
        return self.suit

    def get_rank(self):
        """Return the rank of the card."""
        return self.rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return self.__str__()

    def equals(self, other):
        """Check if two cards are the same."""
        return self.rank == other.rank and self.suit == other.suit


class CardDeck:
    def __init__(self, suits=None, ranks=None, tracker=None, custom_deck=None):
        if suits is None:
            suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        if ranks is None:
            ranks = ['2', '3', '4', '5', '6', '7',
                     '8', '9', '10', 'J', 'Q', 'K', 'A']

        self.suits = suits
        self.ranks = ranks
        self.tracker = tracker

        if custom_deck:
            # Save the original custom deck for later reset
            self.original_custom_deck = custom_deck
            self.cards = [Card(rank, suit) for rank, suit in custom_deck]
        else:
            self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

        self.size = len(self.cards)  # Track the size of the deck
        self.shuffle()

    def set_custom_deck(self, custom_deck):
        """Set a custom deck using a 2D array of (rank, suit)."""
        self.original_custom_deck = custom_deck  # Save the original custom deck
        self.cards = [Card(rank, suit) for rank, suit in custom_deck]
        self.size = len(self.cards)
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw(self, n=1):
        """Draw n cards from the deck."""
        if n > self.size:
            n = self.size  # Ensure not drawing more than available

        drawn_cards = [self.cards.pop() for _ in range(n)]
        self.size -= n  # Update the deck size

        # Add the drawn cards to the tracker as tuples (rank, suit)
        if self.tracker:
            for card in drawn_cards:
                self.tracker.add_result((card.rank, card.suit))  # Store as (rank, suit) tuple
        
        return drawn_cards

    def reset_deck(self):
        """Reset the deck to its custom state and shuffle."""
        if hasattr(self, 'original_custom_deck') and self.original_custom_deck:
            # Reset to the original custom deck state
            self.cards = [Card(rank, suit)
                          for rank, suit in self.original_custom_deck]
        else:
            # If no custom deck, reset to the standard 52-card deck
            self.cards = [Card(rank, suit)
                          for suit in self.suits for rank in self.ranks]

        self.size = len(self.cards)  # Reset deck size
        self.shuffle()
