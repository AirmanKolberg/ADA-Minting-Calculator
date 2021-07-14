#!/bin/bash

git status

# Wait five seconds for user's viewing pleasure
sleep 5

git add data.json

sleep 1

git commit -m "💽  Freebee Starting Data"

sleep 1

git push https://github.com/AirmanKolberg/ADA-Minting-Calculator.git