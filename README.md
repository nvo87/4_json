# Prettify JSON

This module contains functions to prettify JSON data from .json file on your hard drive.
Prettify means to output json not only in single string, but in read-friendly format,  with line breaks and indents.

# Quickstart

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>


```
For example, `$ python pprint_json.py alco_shops.json` gets you in terminal:

```
{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
     ...
     ...
```
**If you need to output result to file**, just add `-f` key: `$ python pprint_json.py alco_shops.json -f`. It creates output.json in pretty print format.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
