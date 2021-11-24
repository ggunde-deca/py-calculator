from calculators.calculator_basic import BasicCalculator
from calculators.calculator_advanced import AdvancedCalculator


def calculator_factory(calculator_type):
    if calculator_type == "basic":
        return BasicCalculator()
    elif calculator_type == "advanced":
        return AdvancedCalculator()
    else:
        raise TypeError("The calculator type is unsupported")
