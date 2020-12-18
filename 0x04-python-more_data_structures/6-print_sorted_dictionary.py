#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print(str(i) + ": " + str(a_dictionary[i]))
