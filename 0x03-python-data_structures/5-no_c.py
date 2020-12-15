#!/usr/bin/python3
def no_c(my_string):
    c = 0
    for i in my_string:
        if i == 'c' or i == 'C':
            my_string = my_string[:c] + my_string[c + 1:]
            continue
        c += 1
    return my_string
