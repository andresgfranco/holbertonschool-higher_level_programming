#!/usr/bin/python3
""" Python script that fetches URL """
from urllib import request

with request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()

print("Body response:")
print("\t - type:", type(html))
print("\t - content:", html)
print("\t - utf8 content:", html.decode("utf-8"))
