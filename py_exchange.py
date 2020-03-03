#!/usr/bin/env/python 3

"""Placholder.
"""

EUR_TO_US = 1.11

def convert_usd_to_eur(usd):
    """Convert USD to EUR.
    """
    return round(usd/EUR_TO_US, 4)

def convert_eur_to_usd(eur):
    """Convert EUR to USD.
    """
    return round(eur*EUR_TO_US, 4)

print(convert_usd_to_eur(.25))
print(convert_usd_to_eur(1))
print(convert_usd_to_eur(10))
print(convert_usd_to_eur(20))

print(convert_eur_to_usd(.25))
print(convert_eur_to_usd(1))
print(convert_eur_to_usd(10))
print(convert_eur_to_usd(20))
