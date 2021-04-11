#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL
curl -s -d "email=hr@holbertonschool.com&subject=I will%20always%20be%20here%20for%20PLD" -X POST $1
