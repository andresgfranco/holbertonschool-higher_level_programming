#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    i = len(argv)
    for counter in range(1, i):
        sum += int(argv[counter])
    print("{}".format(sum))
