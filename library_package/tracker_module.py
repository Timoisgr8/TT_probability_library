from library_package.card_deck_module import Card
from collections import Counter


class Tracker:
    def __init__(self):
        self.results = []
        self.tracking_items = []
        self.silent = True

    def add_result(self, value):
        """Add a result to the tracker and check if it's being tracked."""
        self.results.append(value)

        for item, count in self.tracking_items:
            if value == item:
                self.found_item(item, count + 1)
                if not self.silent:
                    print(f"{value} has been found at index {len(self.results)}")

    def found_item(self, item, count):
        """Update the count of found items."""
        for i in range(len(self.tracking_items)):
            if self.tracking_items[i][0] == item:
                self.tracking_items[i][1] = count
                return

    def reset(self):
        """Reset the tracker results."""
        self.results = []
        self.tracking_items = []

    def print_results(self):
        """Print the tracked results with unique item counts."""
        print("Results:", self.results)

        unique_counts = Counter(self.results)
        print("Unique Item Counts:", dict(unique_counts))

    def look_for(self, items):
        """Set items to look for in tracked results."""
        self.tracking_items = [[item, 0] for item in items]

    def set_silent(self, silent):
        """Enable or disable silent mode."""
        self.silent = silent

    def matches_any(self, card, item):
        """
        Check if the card or item matches the item based on the rank and/or suit.

        :param card: The card or value to check.
        :param item: The item to compare, which can be a tuple of (rank, suit) for cards or a single value for coins.
        :return: True if the card matches the item based on the rank and/or suit, or if it's a simple value match.
        """
        if isinstance(card, tuple):  # For Card objects (rank, suit tuples)
            # Compare rank, allowing 'Any' to match any rank
            rank_match = (item[0] == 'Any' or card[0] == item[0])
            # Compare suit, allowing 'Any' to match any suit
            suit_match = (item[1] == 'Any' or card[1] == item[1])
            return rank_match and suit_match
        else:  # For non-Card objects (like strings for coin results)
            return item == 'Any' or card == item

    def contains(self, sequence, consecutive=False, ordered=False):
        """
        Check if a given sequence exists in the tracked results.

        :param sequence: List of values to check for in results.
        :param consecutive: If True, requires the sequence to appear consecutively.
        :param ordered: If True, requires the sequence to appear in order but allows gaps.
        :return: True if the sequence is found according to the given conditions, otherwise False.
        """
        if not sequence:
            return False

        results = self.results
        seq_len = len(sequence)

        # If sequence length is greater than results length, return False
        if seq_len > len(results):
            return False

        # Default check (unordered, not consecutive)
        if not consecutive and not ordered:
            # Check if all items in sequence exist in results, disregarding order
            result_count = Counter(results)
            sequence_count = Counter(sequence)
            for item in sequence:
                # Check if the item matches any of the results
                matches = False
                for res in results:
                    if self.matches_any(res, item):
                        matches = True
                        break  # Break once a match is found
                if not matches:
                    return False  # Return False if a match is not found for any item
            return True

        # Ordered but not consecutive (find indices in order)
        if ordered and not consecutive:
            index = 0
            for res in results:
                if index < seq_len and self.matches_any(res, sequence[index]):
                    index += 1
                if index == seq_len:
                    return True
            return False

        # Consecutive but not ordered check
        if consecutive and not ordered:
            for i in range(len(results) - seq_len + 1):
                # Create a window of the same length as the sequence
                window = results[i:i + seq_len]
                # Check if the window has the same items, irrespective of order
                if all(self.matches_any(res, item) for res, item in zip(window, sequence)):
                    return True
            return False

        # Consecutive check (sliding window search)
        if consecutive:
            for i in range(len(results) - seq_len + 1):
                if all(self.matches_any(res, item) for res, item in zip(results[i:i + seq_len], sequence)):
                    return True
            return False

        return False
