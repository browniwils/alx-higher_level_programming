#!/usr/bin/python3
for n in range(10):
    for i in range(n + 1, 10):
        if n == 8 and i == 9:
            print("{}{}".format(n, i))
        else:
            print("{}{}".format(n, i), end=", ")
