from dataclasses import dataclass, field
from dataclasses import make_dataclass
from collections import namedtuple
from math import radians, sin, cos, asin, sqrt

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


@dataclass
class DataClassCard:
    rank: str
    suit: str

def make_french_deck():
    return [DataClassCard(r, s) for s in SUITS for r in RANKS]

@dataclass
class Deck:
    cards: list[DataClassCard] = field(default_factory=make_french_deck)



@dataclass
class Position:
    name: str
    longitude: float = 0.0
    latitude: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.longitude), radians(other.longitude)
        phi_1, phi_2 = radians(self.latitude), radians(other.latitude)
        h = (sin((phi_2 - phi_1) / 2) ** 2 + cos(phi_1) * cos(phi_2)
             * sin((lam_2 - lam_1) / 2) ** 2)
        return 2 * r * asin(sqrt(h))




if __name__=='__main__':
    position = Position('Oslo', 'fignja', 59.9)
    print(position)
    print(position.latitude)

    position = Position('Moscow')
    print(position)
    print(position.latitude)

    Car = make_dataclass('Car', ['model', 'color', 'year'])
    car = Car('mersedes', 'blue', 1990)
    print(Car)
    print(car)
    print(car.model, car.color, car.year)

    Car2 = namedtuple('Car2', ['model2', 'color2', 'year2'])
    car2 = Car2('audi', 'red', 2010)
    print(Car2)
    print(car2)
    print(car2.model2, car2.color2, car2[2])

    print("============")
    oslo = Position('Oslo', 10.8, 59.9)
    vancouver = Position('Vancouver', -123.1, 49.3)
    distans = oslo.distance_to(vancouver)
    print('Расстояние от Осло до Ванкувера', distans)

    one_deck = Deck()
    print("Hello", one_deck.cards)
    queen_of_hearts = DataClassCard('Q', 'Hearts')
    ace_of_spades = DataClassCard('A', 'Spades')
    two_cards = Deck([queen_of_hearts, ace_of_spades])
    print(two_cards)
    for card in make_french_deck():
        print(card)