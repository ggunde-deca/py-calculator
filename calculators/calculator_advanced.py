from interface.calculator_interface import Calculator


class AdvancedCalculator(Calculator):
    def __init__(self) -> None:
        super().__init__()
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        self.result = a / b
        return self.result

    def bitwise_and(self, a, b):
        self.result = a & b
        return self.result

    def bitwise_or(self, a, b):
        self.result = a | b
        return self.result
