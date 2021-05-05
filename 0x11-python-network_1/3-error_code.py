#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and manage an exception"""
from urllib import request, parse, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as exception:
        print("Error code:", exception.code)
