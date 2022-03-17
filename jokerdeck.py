from carddeck import CardDeck, Card

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()  # call _make_deck() in parent (i.e., CardDeck)
        for joker_number in '1', '2':
            card = Card(joker_number, '** JOKER **')
            self._cards.append(card)
