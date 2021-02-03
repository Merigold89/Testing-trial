class Calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        """ Addition """
        return self.first + self.second # przy zamianie na "+" na "-" pojawią się błędy w test_calculator.py


    def multiply(self):
        """ Multiplication """
        return self.first * self.second


    def subtract(self):
        """ Subtraction """
        return self.first - self.second


    def divide(self):
        """ Division """
        if self.second == 0:
            raise ValueError('Can not divide by zero!')
        return self.first / self.second
