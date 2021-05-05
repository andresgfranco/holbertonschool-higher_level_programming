#!/usr/bin/python3
""" Python script that takes in a URL, sends  request to the URL
and displays the value of the variable X-Request-Id"""
import requests
import sys

if __name__ == "__main__":
    reply = requests.get(sys.argv[1])
    print(reply.headers.get("X-Request-Id"))
