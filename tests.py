from unittest import TestCase
from evaluation import distance_traveled


class DistanceTraveledTestCase(TestCase):
    def test_unshuffled_cards(self):
        unshuffled_cards = range(5)
        for i in range(5):
            self.assertTrue(distance_traveled(unshuffled_cards, i) == 0)

    def test_shifted_cards(self):
        for shift in range(3):
            cards = range(6)
            forward_shifted_cards = list(map(lambda i: cards[(i - shift) % 6], cards))
            backward_shifted_cards = list(map(lambda i: cards[(i + shift) % 6], cards))
            for i in range(6):
                self.assertTrue(distance_traveled(forward_shifted_cards, i) == shift)
                self.assertTrue(distance_traveled(backward_shifted_cards, i) == shift)
