from shufflers import *


def distance_traveled(shuffled_cards, card):
    new_position = shuffled_cards.index(card)
    num_cards = len(shuffled_cards)
    return min((new_position - card) % num_cards, (card - new_position) % num_cards)


def evaluate(shuffler, num_cards):
    cards = list(range(num_cards))
    shuffled_cards = shuffler.shuffle(cards)
    distances_traveled = list(map(lambda i: distance_traveled(shuffled_cards, i), range(num_cards)))
    avg_distance_traveled = sum(distances_traveled) / num_cards
    variance = sum(map(lambda i: (distances_traveled[i] - avg_distance_traveled) ** 2, range(num_cards))) / num_cards
    return variance


if __name__ == '__main__':
    shufflers = [
        ('Fisher-Yates', FisherYatesShuffler()),
        ('Random', RandomShuffler()),

        ('2-Pile', NPileShuffler(2)),

        ('3-Pile', NPileShuffler(3)),

        ('4-Pile', NPileShuffler(4)),

        ('2-Pile -> 3-Pile', CascadingShuffler([NPileShuffler(2), NPileShuffler(3)])),
        ('2-Pile -> 4-Pile', CascadingShuffler([NPileShuffler(2), NPileShuffler(4)])),
        ('3-Pile -> 4-Pile', CascadingShuffler([NPileShuffler(3), NPileShuffler(4)])),
    ]

    num_cards = 30

    scores = []
    for name, shuffler in shufflers:
        score = evaluate(shuffler, num_cards)
        scores.append((name, score))

        for i in range(2, 5):
            i_times_shuffler = NTimesShuffler(i, shuffler)
            score = evaluate(i_times_shuffler, num_cards)
            scores.append(('{} x {}'.format(name, i), score))

    for name, score in sorted(scores, key=lambda pair: pair[1], reverse=True):
        print('{:<30}\t{}'.format(name, score))
