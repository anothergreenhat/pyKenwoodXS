# KenwoodXS in Python

## Setup 

`read_data.py` is meant to run on a Raspberry Pi (mine is a Model 2B) and use GPIO pins 23 and 24 for the CTRL (white/left) and SDAT (red/right) signals respectively. I also wired the ground wire on the 3.5 mm cord (headphone/aux cord: see `./data/XS-Connection.jpg`) to a ground GPIO pin on the Raspberry Pi. Please feel free to clone this repo and change those pin numbers to whatever your configuration wishes are!

## How to Use

Run `read_data.py` using `python3` on the Linux command line or any Python 3 interpretting interface you have!

## Table of Results

The below table makes pretty the data recorded at the top of KenwoodXS.ino

| Button | Received Code |
| --- | --- |
| **Miscellaneous** |
| `POWER` (On) | 181 |
| `POWER` (Off) | 185 |
| `BAND` (Tuner AM/FM)<sup>1</sup> | 123 |
| `+10` | 164 |
| **Input** |
| `TAPE 2` (toggle on) | 20 |
| `TAPE 2` (toggle off) | 24 |
| `VIDEO 2` | 113 |
| `PHONO` | 115 |
| `TAPE 1` | 121 |
| `VIDEO 1` | 122 |
| `TUNER`<sup>1</sup> | 123 |
| `CD` | 125 |
| **Tape A** |
| `>>` (fast forward) | 67 |
| `[]` (stop) | 69 |
| `>` (play) | 71 |
| `*` (record) | 73 |
| `<<` (rewind) | 75 |
| `\|\|` (pause) | 77 |
| `<` (rewind slow?) | 79 |
| **Tape B** |
| `>>` | 66 |
| `[]` | 68 |
| `>` | 70 |
| `*` | 72 |
| `<<` | 74 |
| `\|\|` | 76 |
| `<` | 78 |
| **CD** | 
| `>/\|\|` (toggle play/pause | 194 |
| `[]` | 198 |
| `DISC` (change disc) | 174 |
| `>>`<sup>2</sup> | 161 |
| `<<`<sup>2</sup> | 169 |
| `>>\|`<sup>2</sup> | 192 |
| `\|<<`<sup>2</sup> | 200 |
| (stop scrubbing/release fwd/rwd) | 177 |

<sup>1</sup> The behavior of these buttons appear to be identical from this code extraction... but the actual behavior on the device changes to the `TUNER` input if the `TUNER` button is pressed, and switches between AM and FM if the `BAND` button is pressed. While they output the same code, I'm not sure how the receiver would be able to tell that the `BAND` button was pressed versus the `TUNER` button? There must be a bug in the code somewhere...

<sup>2</sup> All of these buttons send their listed code on press (and hold) of the button, and then send the stop code (177) on release of the button. I haven't tested this yet, as I do not own any Kenwood CD players or devices that support Kenwood XS other than this receiver, but I think I can safely suspect that this is meant to "scrub" through the CD (`>>` and `<<` through the current track with volume, `>>|` and `|<<` track by track).


