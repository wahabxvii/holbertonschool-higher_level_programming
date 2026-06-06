#!/usr/bin/python3
import sys


def print_args():
    args = len(sys.argv)
    if args - 1 == 0:
        print("{0} argument.".format(args - 1))
    elif args - 1 == 1:
        print("{0} argument:".format(args - 1))
    else:
        print("{0} arguments:".format(args - 1))
    for i in range(1, args):
        print("{0}: {1}".format(i, sys.argv[i]))


if __name__ == "__main__":
    print_args()
