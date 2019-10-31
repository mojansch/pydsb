**Currently not working because Heinekingmedia removed an API. I'm currently working on an update using another API**

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
