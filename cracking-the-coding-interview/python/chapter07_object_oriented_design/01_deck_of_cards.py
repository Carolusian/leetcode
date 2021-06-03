# Design a deck of cards
import random
from typing import List

class CardDeck():
    def __init__(self, cards: List[Card]):
        if cards:
            self.cards = cards
        else:
            self.cards = []

    def shuffle(self):
        for i in range(len(self.cards)):
            o = random.randint(0, i)
            self.cards[i], self.cards[o] = self.cards[o], self.cards[i]

    def draw_card(self):
        return self.cards.pop()


class Card():
    def __init__(self, number, suit):
        self.number, self.suit = number, suit
