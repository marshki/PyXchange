#!/usr/bin/env python 3

"""Currency conversion utility (in progress).
"""

from forex_python.converter import get_rate

EUR_TO_USD=get_rate('EUR', 'USD')

# Sample exchange rate.
# EUR_TO_USD = 1.11

def convert_usd_to_eur(usd):
    """Convert USD to EUR.
    """
    return round(usd/EUR_TO_USD, 4)

def convert_eur_to_usd(eur):
    """Convert EUR to USD.
    """
    return round(eur*EUR_TO_USD, 4)

print(convert_usd_to_eur(.25))
print(convert_usd_to_eur(1))
print(convert_usd_to_eur(10))
print(convert_usd_to_eur(20))

print(convert_eur_to_usd(.25))
print(convert_eur_to_usd(1))
print(convert_eur_to_usd(10))
print(convert_eur_to_usd(20))
