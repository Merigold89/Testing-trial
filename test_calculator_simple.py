import unittest
import calculator_simple
# aby uruchomić: linia komend: python -m unittest test_calculator lub dodać ostatni fragment kodu
# plik test_calclator.py i calculator.py muszą być w jednym folderze
class TestCalculator(unittest.TestCase):  # a test case for the calculator.py module

    def test_add(self):
        """
        Tests for the add() function.

        assertEqual - sprawdza, czy 2 podane argumenty są sobie równe: 2 zmienne ajko argumenty
        dla funkcji oraz oczekiwany wynik, dodatkowo komentarz w sypadku fail testu
        """
        self.assertEqual(calculator_simple.add(6, 4), 10, 'Error when adding two positive numbers')
        self.assertEqual(calculator_simple.add(6, -4), 2, 'Error when adding two positive and negative numbers')
        self.assertEqual(calculator_simple.add(-6, 4), -2, 'Error when adding two negative and positive numbers')
        self.assertEqual(calculator_simple.add(-6, -4), -10, 'Error when adding two negative numbers')

    def test_multiply(self):
        """
        Tests for the multiply() function.
        """
        self.assertEqual(calculator_simple.multiply(6, 4), 24)
        self.assertEqual(calculator_simple.multiply(6, -4), -24)
        self.assertEqual(calculator_simple.multiply(-6, 4), -24)
        self.assertEqual(calculator_simple.multiply(-6, -4), 24)

    def test_subtract(self):
        """
        Tests for the subtract() function.
        """
        self.assertEqual(calculator_simple.subtract(6, 4), 2)
        self.assertEqual(calculator_simple.subtract(6, -4), 10)
        self.assertEqual(calculator_simple.subtract(-6, 4), -10)
        self.assertEqual(calculator_simple.subtract(-6, -4), -2)

    def test_divide(self):
        """
        Tests for the divide() function.
        """
        self.assertEqual(calculator_simple.divide(10, 2), 5)
        self.assertEqual(calculator_simple.divide(10, -2), -5)
        self.assertEqual(calculator_simple.divide(-10, 2), -5)
        self.assertEqual(calculator_simple.divide(-10, -2), 5)

        self.assertRaises(ValueError, calculator_simple.divide, 5, 0)  # 1 metoda, ValueError jest wartością oczekiwaną, potem argumenty
        with self.assertRaises(ValueError):  # 2 metoda wywołujemy błąd
            calculator_simple.divide(5, 0)
        #self.assertEqual(calculator.divide(10, 0), 0)  # zamiast litery F zwóci literę E,
        #test zgłasza wyjątek inny niż błąd AssertionError (ValueError) - nieprawidłowość jest, ale nie uważa się, aby test został oblany

if __name__ == "__main__":  # jeśli nie chcemy odpalać z linii komend
    unittest.main()
