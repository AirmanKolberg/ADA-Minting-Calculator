#!/bin/bash

git status

# Wait five seconds for user's viewing pleasure
sleep 5

git add data.json
git commit -am "💽  Freebee Starting Data"
git push https://github.com/AirmanKolberg/ADA-Minting-Calculator.git