#!/usr/bin/python3
""" Python script that fetches URL """
import request


if __name__ == "__main__":
    html = requests.get("https://intranet.hbtn.io/status").text

    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
