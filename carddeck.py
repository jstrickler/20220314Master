import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):  # human-friendly
        return f"{self.rank}-{self.suit}"

    def __repr__(self):  # code-friendly
        return f"Card('{self.rank}', '{self.suit}')"


class CardDeck:  # inherits from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'clubs diamonds hearts spades'.split()


    def __init__(self, dealer):
        print("initializing...")
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    @property  # public variable
    def dealer(self):  # public property getter
        return self._dealer.upper()   # private data

    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer   # self._dealer is private variable
        else:
            raise TypeError("Dealer must be a string")


if __name__ == '__main__':
    c = Card('A', 'spades')
    print(str(c))
    print(repr(c))
