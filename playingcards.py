

def create_deck(dealer):
    return {'dealer': dealer, 'cards': []}

def deal(deck):
    return deck.pop()

def shuffle(deck):
    print("shuffling")

if __name__ == '__main__':
    d = create_deck("Millie")
    print(d['dealer'])
    shuffle(d['cards'])
    card = deal(d['cards'])

#  d = CardDeck("Millie")
#  print(d.dealer)
#  d.shuffle()
#  card = d.deal()
