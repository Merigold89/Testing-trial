import unittest
import calculator_upgrade
# aby uruchomić: linia komend: python -m unittest test_calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """
        Is executed before every test method.
        """
        self.calc = calculator_upgrade.Calculator(5, 1)
        print('setUp method')

    def tearDown(self):
        """
        Is executed after every test method.
        """
        print('tearDown method')

    def test_add(self):
        """
        Tests for the add() function.
        """
        self.assertEqual(self.calc.add(), 6)
        self.calc.first = 8
        self.calc.second = 2
        self.assertEqual(self.calc.add(), 10)
        print('test_add method')

    def test_subtract(self):
        """
        Tests for the subtract() function.
        """
        self.assertEqual(self.calc.subtract(), 4)
        self.calc.first = 8
        self.calc.second = 2
        self.assertEqual(self.calc.subtract(), 6)
        print('test_subtract method')


if __name__ == "__main__":
    unittest.main()
