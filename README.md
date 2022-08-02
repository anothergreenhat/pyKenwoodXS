# KenwoodXS in Python

## Setup 

`read_data.py` is meant to run on a Raspberry Pi (mine is a Model 2B) and use GPIO pins 23 and 24 for the CTRL (white/left) and SDAT (red/right) signals respectively. I also wired the ground wire on the 3.5 mm cord (headphone/aux cord: see data/XS-Connection.jpg) to a ground GPIO pin on the Raspberry Pi. Please feel free to clone this repo and change those pin numbers to whatever your configuration wishes are!

## How to Use

Run `read_data.py` using `$ python3` on the Linux command line or any Python 3 interpretting interface you have!

## Table of Results

The below table makes pretty the data recorded at the top of KenwoodXS.ino

| Button | Received Code |
| --- | --- |
| Miscellaneous |  |
| :--- | ---: |
| Toggle Power (On) | 181 |
| Toggle Power (Off) | 185 |
| Band (Tuner AM/FM) | 123 |
| Num Pad +10 | 164 |
| --- | --- |
| Input | |
