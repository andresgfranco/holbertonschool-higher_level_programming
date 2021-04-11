#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me
curl -s -X PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"
