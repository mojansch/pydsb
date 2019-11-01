# pydsb
Python API for DSBmobile

## Installation

    pip install pydsb

## Usage

    import pydsb
    
    dsb = pydsb.PyDSB("username", "password")
    dsb.login()
    
    print(dsb.get_plans())
    print(dsb.get_news())
