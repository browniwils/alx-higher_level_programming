#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    arg = sys.argv
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(arg[1])
        b = int(arg[3])
        math_op = str(arg[2])
        if math_op == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif math_op == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif math_op == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif math_op == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, *, and /")
            sys.exit(1)
