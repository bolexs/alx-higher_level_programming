#!/bin/bash
# Script sends a POST request to the url and displays the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
