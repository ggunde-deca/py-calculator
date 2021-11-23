import calculator


def test_add():
    sum = calculator.add(5, 6)
    assert sum == 11


def test_subtract():
    difference = calculator.subtract(5, 6)
    assert difference == -1


def test_multiply():
    multiply = calculator.multiply(5, 6)
    assert multiply == 30


def test_divide():
    divide = calculator.divide(5, 6)
    assert (int)(divide) == 0
