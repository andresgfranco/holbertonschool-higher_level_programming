#!/usr/bin/python3
""" Python script that takes your GitHub credentials(username and pass) and
uses the GitHub API to display your id"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get("https://api.github.com/user",
                        auth=(sys.argv[1], sys.argv[2]))
    
    print(req.json().get("id"))
