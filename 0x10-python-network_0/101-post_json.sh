#!/bin/bash
# Script that sends a JSON POST request to a URL
curl -$1 sX POST -H "Content-Type: application/json" -d @$2
