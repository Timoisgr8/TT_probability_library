import random


class Coin:
    def __init__(self, head_p=0.5, tracker=None):
        self.head_p = head_p
        self.tracker = tracker

    def flip(self):
        """Flip the coin and return 'Heads' or 'Tails'."""
        result = 'Heads' if random.random() <= self.head_p else 'Tails'
        if self.tracker:
            # Notify Tracker of the coin flip result
            self.tracker.track(result)
        return result
