#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        str2 = str[:n] + str[n + 1:]
        return str2
    else:
        return str
