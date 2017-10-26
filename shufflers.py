import random
from abc import abstractmethod


class Shuffler:
    @abstractmethod
    def shuffle(self, cards):
        pass


class RandomShuffler(Shuffler):
    def shuffle(self, cards):
        shuffled_cards = cards.copy()
        random.shuffle(shuffled_cards)
        return shuffled_cards


class CascadingShuffler(Shuffler):
    def __init__(self, shufflers):
        self.shufflers = shufflers

    def shuffle(self, cards):
        shuffled_cards = cards.copy()
        for shuffler in self.shufflers:
            shuffled_cards = shuffler.shuffle(shuffled_cards)
        return shuffled_cards


class NTimesShuffler(Shuffler):
    def __init__(self, n, shuffler):
        self.n = n
        self.shuffler = shuffler

    def shuffle(self, cards):
        shuffled_cards = cards.copy()
        for i in range(self.n):
            shuffled_cards = self.shuffler.shuffle(shuffled_cards)
        return shuffled_cards


class NPileShuffler(Shuffler):
    def __init__(self, num_piles):
        self.num_piles = num_piles

    def shuffle(self, cards):
        piles = []
        for i in range(self.num_piles):
            piles.append([])

        next_pile = 0
        for card in cards:
            piles[next_pile].append(card)
            next_pile = (next_pile + 1) % self.num_piles

        shuffled_cards = []
        for pile in piles:
            for card in pile:
                shuffled_cards.append(card)

        return shuffled_cards


class FisherYatesShuffler(Shuffler):
    def shuffle(self, cards):
        shuffled_cards = cards.copy()
        num_cards = len(cards)

        for i in range(num_cards - 1):
            j = random.randrange(i, num_cards)
            t = shuffled_cards[i]
            shuffled_cards[i] = shuffled_cards[j]
            shuffled_cards[j] = t

        return shuffled_cards
