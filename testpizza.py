import unittest
from main import order
from pizza import Margherita, Pepperoni, Hawaiian
from click.testing import CliRunner


class TestPizzaFunctions(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_order_invalid_pizza(self):
        result = self.runner.invoke(order, ['WrongPizza'])
        self.assertIn('Invalid pizza type: WrongPizza\n', result.output)

    def test_order_valid_pizza_no_delivery(self):
        result = self.runner.invoke(order, ['Margherita'])
        self.assertIn('🍳 Приготовили Margherita за', result.output)
        self.assertNotIn('🛵 Доставили', result.output)

    def test_order_valid_pizza_with_delivery(self):
        result = self.runner.invoke(order, ['--delivery', 'Pepperoni'])
        self.assertIn('🍳 Приготовили Pepperoni за', result.output)
        self.assertIn('🛵 Доставили Pepperoni за', result.output)


class TestPizzaClasses(unittest.TestCase):

    def test_margherita_creation(self):
        margherita = Margherita(size='XL')
        self.assertEqual(margherita.size, 'XL')

    def test_pepperoni_creation(self):
        pepperoni = Pepperoni()
        self.assertEqual(pepperoni.size, 'L')

    def test_hawaiian_creation(self):
        hawaiian = Hawaiian(size='M')
        self.assertEqual(hawaiian.size, 'M')
    
    def test_wrong_size_creation(self):
        # self.assertEqual(hawaiian.size, 'M')
        with self.assertRaises(Exception):
            Margherita(size='wrongsize')


if __name__ == '__main__':
    unittest.main()
