import random
import click
from typing import Callable, Any
import time


def log(text: str) -> Callable:
    """
    Это обертка над декоратором, которая позволяет в декаратор
    дополнительные аргументы передавать. Например текст, как в
    данной задачке
    """
# for pull request
    def decorator(fun: Callable) -> Callable:
        """
        Декоратор, который печатает время выполнения готовки/доставки
        """

        def wrapper(*args, **kwargs) -> Any:
            result = fun(*args, **kwargs)
            print(text.format(random.randint(1, 10)))
            return result

        return wrapper

    return decorator


class Pizza_Recipes:
    """
    Класс, который показывает пользователю актуальное меню.
    Предоставляет пользователю информацию об ингридиентах пиццы и ее размере
    """

    def __init__(self):
        """
        Это конструктор, который задаает основные переменные для класса
        """
        self.pizza_types = ['Margherita', 'Pepperoni', 'Hawaiian']
        self.pizza_size = ['L', 'XL']
        self._pizza_type = random.choice(self.pizza_types)
        self.recipes = {
            'Margherita': ['tomato sauce', 'mozzarella', 'tomatoes'],
            'Pepperoni': ['tomato sauce', 'mozzarella', 'pepperoni'],
            'Hawaiian': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        }
        self._pizza_size = random.choice(self.pizza_size)

    def dict(self, pizza_type: str) -> dict:
        """
        Метод принимает на вход название пиццы и выводит для нее ингридиенты

        >>> Pizza_Recipes().dict('Pepperoni')
        ['tomato sauce', 'mozzarella', 'pepperoni']
        >>> Pizza_Recipes().dict('Hawaiian')
        ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        >>> Pizza_Recipes().dict('Wrong_Key')
        Traceback (most recent call last):
        ...
        KeyError: 'Wrong_Key'
        """
        return self.recipes[pizza_type]

    def pizza_menu(self):
        """
        Метод выводит приветствие и актуальное меню
        """
        print(
            '\nПривет! Этот класс поможет тебе определиться'
            ', какую пиццу скушать сегодня.\nВ меню есть три разных пиццы:\n'
            '\n•Margherita(Маргарита) \n•Pepperoni(Пепперони) '
            '\n•Hawaiian(Ананас)'
            '\n\nДля того, чтобы получить рецепт пиццы, выбери, какую пиццу'
            ' ты рассмотришь. Подробные рецепты пицц представлены ниже:\n'
        )
        recipe_str = []
        pizza_emojis = {
            'Margherita': ' 🧀',
            'Pepperoni': ' 🍕',
            'Hawaiian': ' 🍍',
        }
        for pz_name, pz_ingr in self.recipes.items():
            recipe_str.append('-- ' + pz_name + pizza_emojis[pz_name] + ' : '
                              + ', '.join(pz_ingr) + '\n')
        return ''.join(recipe_str)

    def __eq__(self, other_object) -> bool:
        if all([self._pizza_type == other_object._pizza_type,
                self._pizza_size == other_object._pizza_size]):
            return True
        else:
            return False


@click.group()
def cli():
    """
    обработчик команд
    """
    pass


@cli.command()
def menu():
    """
    Выводит меню
    """
    print(pizza_recipe.pizza_menu())
    return


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """
    Готовит и доставляет пиццу
    """
    pizza = pizza.title()
    to_bake(pizza)
    if delivery:
        to_deliver(pizza)
    else:
        to_pickup(pizza)
    return


@log('🍽 Приготовили за {}с!')
def to_bake(pizza):
    """
    Готовит пиццу
    """
    print(
        'Готовим {} из {}'.format(pizza, ', '.join(pizza_recipe.dict(pizza))))
    return


@log('🏍 Доставили за {}с!')
def to_deliver(pizza):
    """
    Доставляем пиццу

    >>> to_deliver('Pizza_name')
    Ищем курьера...
    Курьеру передана пицца Pizza_name...
    Курьер в пути...
    >>> to_deliver(123)
    Ищем курьера...
    Курьеру передана пицца 123...
    Курьер в пути...
    """
    print('Ищем курьера...')
    time.sleep(2 * random.random())
    print('Курьеру передана пицца {}...'.format(pizza))
    time.sleep(2 * random.random())
    print('Курьер в пути...')
    return


@log('🏠 Забрали за {}с!')
def to_pickup(pizza):
    """
    Самовывоз пиццы

    >>> to_pickup('Pizza_name')
    Пицца Pizza_name готова
    Можно забирать
    >>> to_pickup(123)
    Пицца 123 готова
    Можно забирать
    """
    time.sleep(2 * random.random())
    print('Пицца {} готова\nМожно забирать'.format(pizza))
    return


if __name__ == '__main__':
    pizza_recipe = Pizza_Recipes()
    cli()

    pizza_recipe_second = Pizza_Recipes()
    print(pizza_recipe_second == pizza_recipe)
