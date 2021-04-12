#!/usr/bin/python3
""" Python script that takes in a URL and an email address, sends a request
to the URL and displays the body of the response"""
import requests
import sys

if __name__ == "__main__":
    reply = requests.get(sys.argv[1])

    if reply.status_code >= 400:
        print("Error code:", reply.status_code)
    else:
        print(reply.text)
