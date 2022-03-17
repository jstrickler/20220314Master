from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Nellie")
print(d1)

d2 = CardDeck("Andy")
print(d2)

print(d1.dealer)
print(d2.dealer)

d1.dealer = "Little Bear"
print(d1.dealer)

try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards)

print()
print("Dealing:")
for i in range(5):
    print(d1.draw())
print()

j = JokerDeck("Jimmy")
print(j)
j.shuffle()
for i in range(5):
    print(j.draw())
print()
print(j.cards)




