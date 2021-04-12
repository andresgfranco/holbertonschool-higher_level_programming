#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request to URL
with the letter as a parameter"""
import requests
import sys

if __name__ == "__main__":
    url = "https://0.0.0.0:5000/search_user"
    data = {"q": ""}
    if len(sys.argv) == 2:
        data["q"] = sys.argv[1]

    try:
        req = requests.post(url, data=data)
        dict_req = req.json()

        if dict_req = {}:
            print("No result")
        else:
            print("[{}] {}".format(dict_req.get("id"), dict_req.get("name")))
    except:
        print("Not a valid JSON")
