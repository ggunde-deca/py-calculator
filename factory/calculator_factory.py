from calculators.calculator_advanced import AdvancedCalculator
from calculators.calculator_basic import BasicCalculator


def calculator_factory(calculator_type):
    if calculator_type == "basic":
        return BasicCalculator()
    if calculator_type == "advanced":
        return AdvancedCalculator()
    raise TypeError("The calculator type is unsupported")
