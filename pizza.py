import random
from typing import Callable

POSSIBLE_SIZES = {'L', 'XL', 'M'}


class Pizza:
    def __init__(self, size: str = 'L'):
        self.validate_pizza_size(size)
        self.size = size

    def __str__(self) -> str:
        return 'One of the Best Pizzas in the World!'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Pizza):
            raise TypeError("You must provide a Class object of Pizza\
                            on the right-hand side of the '=' operator")
        return self.ingredients == other.ingredients

    @staticmethod
    def validate_pizza_size(size) -> bool:
        if size not in POSSIBLE_SIZES:
            raise Exception('Wrong Pizza Size. Must be XL, L or M')

    def dict(self):
        """Returns the name of pizza and its ingredients."""
        return f'{self.name}: {self.ingredients}'


class Margherita(Pizza):
    ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
    name = '🧀 Margherita'

    def __init__(self, size='L'):
        super().__init__(size)

    def __str__(self) -> str:
        return 'Margherita'


class Pepperoni(Pizza):
    ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
    name = '🍕 Pepperoni'

    def __init__(self, size='L'):
        super().__init__(size)

    def __str__(self) -> str:
        return 'Pepperoni'


class Hawaiian(Pizza):
    ingredients = ['tomato sauce', 'mozzarella',
                   'chicken', 'pineapples']
    name = '🍍 Hawaiian'

    def __init__(self, size='L'):
        super().__init__(size)

    def __str__(self) -> str:
        return 'Hawaiian'
