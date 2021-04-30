import unittest
import calculator
# aby uruchomić: linia komend: python -m unittest test_calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """
        Is executed before every test method.
        """
        self.calc = calculator.Calculator(5, 1)
        print('setUp method')

    def tearDown(self):
        """
        Is executed after every test method.
        """
        self.calc = calculator.Calculator(1, 0)
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

    def test_multiply(self):
        """
        Tests for the multiply() function.
        """
        self.assertEqual(self.calc.multiply(), 5)
        self.calc.first = 8
        self.calc.second = 2
        self.assertEqual(self.calc.multiply(), 16)
        print('test_multiply method')

    def test_divide(self):
        """
        Tests for the divide() function.
        """
        self.assertEqual(self.calc.divide(), 5)
        self.calc.first = 0
        self.calc.second = 5
        self.assertEqual(self.calc.divide(), 0)
        self.calc = calculator.Calculator(1, 0)
        #self.assertEqual(self.calc.divide(), ZeroDivisionError)
        print('test_divide method')


if __name__ == "__main__":
    unittest.main()