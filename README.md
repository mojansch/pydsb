# pydsb 2.1.0
pydsb provides a Python API for DSBmobile.

Heinekingmedia (the creators of DSBmobile) shut down the API pydsb was previously using so I had to use the app-API. That required a complete rewrite so some features are currently not implemented yet. See below for the current featureset.
I strongly reccomend that users of version 1.0 upgrade to 2.0, because it doesn't work anymore. Some syntax has changed too, so be aware of that.

## Features

- [x] Getting plans
- [x] Getting news (maybe not always working due to limited sample data)
- [x] Getting postings (Aushänge)

## Installation

    pip install -U --user pydsb

## Usage

    import pydsb
    
    dsb = pydsb.PyDSB("username", "password")
    
    print(dsb.get_plans())
