#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request to URL
with the letter as a parameter"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": ""}
    if len(sys.argv) == 1:
        print("No result")
        quit()
    data["q"] = sys.argv[1]
    req = requests.post(url, data=data)
    try:
        dict_req = req.json()
    except:
        print("Not a valid JSON")
    else:
        if dict_req == {}:
            print("No result")
        else:
            print("[{}] {}".format(dict_req.get("id"), dict_req.get("name")))
