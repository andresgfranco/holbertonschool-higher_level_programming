#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    hidden_list = dir(hidden_4)
    for i in hidden_list:
        if i[0] != "_":
            print("{}".format(i))
