#!/usr/bin/python3
import sys


def infinite_add():
    args = len(sys.argv)
    result = 0
    for i in range(1, args):
        result += int(sys.argv[i])
    print(result)


if __name__ == "__main__":
    infinite_add()
