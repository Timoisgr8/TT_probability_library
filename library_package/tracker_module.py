import random
from .dice_module import Dice
from .coin_module import Coin


class Tracker:
    def __init__(self):
        self.results = []
        self.tracking_items = []
        self.silent = True

    def track(self, result):
        """Track the result of a dice roll or coin flip."""
        self.add_result(result)

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
        """Print the tracked results."""
        print(self.results)

    def look_for(self, items):
        """Set items to look for in tracked results."""
        self.tracking_items = [[item, 0] for item in items]

    def set_silent(self, silent):
        """Enable or disable silent mode."""
        self.silent = silent

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

        # Default check (unordered, not consecutive)
        if not consecutive and not ordered:
            return all(item in results for item in sequence)

        # Ordered but not consecutive (find indices in order)
        if ordered and not consecutive:
            index = 0
            for res in results:
                if index < seq_len and res == sequence[index]:
                    index += 1
                if index == seq_len:
                    return True
            return False

        # Consecutive check (sliding window search)
        if consecutive:
            for i in range(len(results) - seq_len + 1):
                if results[i:i + seq_len] == sequence:
                    return True
            return False

        return False