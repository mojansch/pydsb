# pydsb
Python API for DSBmobile

## Installation

    pip install pydsb

## Usage

    import pydsb
    
    dsb = pydsb.PyDSB("username", "password")
    dsb.login()
    
    dsb.get_items()
