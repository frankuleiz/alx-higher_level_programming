#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argc[2]
    a = int(argc[1])
    b = int(argc[3]
    if operator == "+":
        print("{} + {} = {}".format(a,b, add(a, b))
    elif operator == "-":
        print("{} - {} = {}".format(a,b, sub(a, b))
    elif operator == "*":
        print("{} * {} = {}".format(a,b, mul(a, b))
    if operator == "/":
        print("{} + {} = {}".format(a,b, div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")

