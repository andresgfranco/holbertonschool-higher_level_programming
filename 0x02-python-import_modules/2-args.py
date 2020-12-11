#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv)
    if i == 1:
        print("0 arguments.")
    else:
        print("{} argument{}.".format(i - 1, "s" if i > 2 else ""))
        for counter in range(1, i):
            print("{}: {}".format(counter, argv[counter]))
