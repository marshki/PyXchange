#!/usr/bin/env/python 3

"""Placholder.
"""

EUR_TO_US = 1.11

def convert_usd_to_euro(usd):
    """Convert USD to EURO.
    """
    return round(usd/1.11, 4)

print(convert_usd_to_euro(.01))
print(convert_usd_to_euro(.05))
print(convert_usd_to_euro(.10))
print(convert_usd_to_euro(.25))
print(convert_usd_to_euro(1))
print(convert_usd_to_euro(5))
print(convert_usd_to_euro(10))
print(convert_usd_to_euro(20))
print(convert_usd_to_euro(50))
print(convert_usd_to_euro(100))
