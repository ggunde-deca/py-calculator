from factory.calculator_factory import calculator_factory


def test_add():
    calculator_var = calculator_factory("basic")

    sum_var = calculator_var.add(5, 6)
    assert sum_var == 11


def test_subtract():
    calculator_var = calculator_factory("basic")

    difference = calculator_var.subtract(5, 6)
    assert difference == -1


def test_multiply():
    calculator_var = calculator_factory("basic")

    multiply = calculator_var.multiply(5, 6)
    assert multiply == 30


def test_divide():
    calculator_var = calculator_factory("basic")

    divide = calculator_var.divide(5, 6)
    assert (int)(divide) == 0
