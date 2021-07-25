#!/bin/bash

# Rename estimations_log.json
mv estimations_log_example.json estimations_log.json

# Install all required dependencies
pip3 install -r requirements.txt

clear
echo "Everything installed and ready to go!"
sleep 2
clear
exit