# ADA Minting Calculator
> When will the last ADA be minted on the Cardano network?
> (All 45 billion)

This quick project I made was intended to help approximate the date and time
at which all ADA (on the Cardano network) will be minted.  ADA is minted, much
like any Proof-of-Stake system, through staking.

## What We Know

- ADA is of limited supply, and the maximum amount of ADA that will ever exist is
45 billion ADA.
- New blocks are minted 24/7, and therefore the number of ADA that exist will
certainly change constantly.
- The amount of ADA produced over time may or may not change.  If it does change,
it most likely be changing in one direction over time (either increasing or
decreasing).

## Steps to Take

1. Whether it be `pip` or `pip3`, be sure to install all dependencies with a:
`pip install -r requirements.txt`
2. Run the `ada_supply.py` file in the Terminal emulator with either:
   `python ada_supply.py` -or- `python3 ada_supply.py`

###### *Note: If you do not wish to collect the data on the backend yourself, my `data.json` file will be updated on GitHub at least every 6 hours.*

This script will, every 20 minutes, check how much ADA is in circulation, and then
saves this data to a file called `data.json` for later retrieval by other apps.

###### *Note: The data in `data.json` is currently in the MST (U.S.) timezone*

2. Once you've collected a good amount of data (of course this should, in theory,
become more accurate over time), run the `main.py` file in the same manner.

This file will take in all of the data from the `data.json` file, calculate the
amount of ADA that was created over time, calculate the average amount of ADA
minted per minute, average out all of those data, and then project that average
into the future to get an estimated time and date the last ADA will be minted.

In the case of any errors (since this is using the cryptocompare API), they will
all be logged to a file called `errors.json`.

A data.json file is already provided to you from my data collection adventures.
Enjoy, and add more data if you can, please!

###### *Note: In future, for better accuracy, I will need to incorporate a forecast model to estimate the changes in ADA production, if any are detected...*

---

### Donations!
Consider donating, though of course not necessary!  :)

Cardano (ADA):
addr1q9jxsfd87g4f9rcl7x43lwxnkmklek279yw0fhwrsm3pjjal23me7f9yesnhs2fhpf05xd0deta3csgn4z433rze7yjsav8ejn


BitCoin (BTC): 
33XbUGgEGx3oQ8wZEsdWBtZ6jncTPWoNtq


Etherium (ETH): 
0x68D8928631f697820cf2bd9B275e5b39D6Cba020


Dogecoin (DOGE):
DNJoCDAwwVcpRMH3wCeeCwRMpzUHW6uvbH


Ripple (XRP):
rahunjARy7sb2AEc75xdzqSRuMeUPqXxF2


VeChain (VET):
0xeD36284Fb479F15620f5c8Af0996A723c6b5dc43