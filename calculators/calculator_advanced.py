from interface.calculator_interface import Calculator


class AdvancedCalculator(Calculator):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def bitwise_and(self, a, b):
        return a & b

    def bitwise_or(self, a, b):
        return a | b
