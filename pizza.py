import random
from typing import Callable


class Pizza:
    def __init__(self, size: str = 'L'):
        self.size = size

    def __str__(self) -> str:
        return 'One of the Best Pizzas in the World!'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Pizza):
            raise TypeError("You must provide a Class object of Pizza\
                            on the right-hand side of the '=' operator")
        return self.ingredients == other.ingredients

    def dict(self):
        """Returns the name of pizza and its ingredients."""
        return f'{self.name}: {self.ingredients}'


class Margherita(Pizza):
    ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
    name = '🧀 Margherita'

    def __init__(self, size='L'):
        super().__init__(size)


class Pepperoni(Pizza):
    ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
    name = '🍕 Pepperoni'

    def __init__(self, size='L'):
        super().__init__(size)


class Hawaiian(Pizza):
    ingredients = ['tomato sauce', 'mozzarella',
                   'chicken', 'pineapples']
    name = '🍍 Hawaiian'

    def __init__(self, size='L'):
        super().__init__(size)

if __name__ == '__main__':

    print(Margherita().ingredients)
    # print(Margherita() == Pepperoni())
    # print(isinstance(Margherita(), Pizza))
    # print(delivery(Margherita()))