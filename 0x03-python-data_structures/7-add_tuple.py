#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2:
        if len_a == 1:
            a_first = tuple_a[0]
            a_second = 0
        else:
            a_first = 0
            a_second = 0
    else:
        a_first = tuple_a[0]
        a_second = tuple_a[1]
    if len_b < 2:
        if len_b == 1:
            b_first = tuple_b[0]
            b_second = 0
        else:
            b_first = 0
            b_second = 0
    else:
        b_first = tuple_b[0]
        b_second = tuple_b[1]
    my_tuple = ((a_first+b_first), (a_second+b_second))
    return my_tuple
