from factory.calculator_factory import calculator_factory


def main():
    calculator_var = calculator_factory("basic")

    print("The addition result is: {}".format(calculator_var.add(5, 6)))
    print("The subtraction result is: {}".format(calculator_var.subtract(5, 6)))
    print("The multiply result is: {}".format(calculator_var.multiply(5, 6)))
    print("The division result is: {}".format(calculator_var.divide(5, 6)))


if __name__ == "__main__":
    main()
