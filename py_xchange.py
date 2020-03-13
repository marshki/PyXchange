#!/usr/bin/env python 3

"""Currency conversion utility (in progress).
"""

import argparse
from forex_python.converter import get_rate

EUR_TO_USD = get_rate('EUR', 'USD')

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

def parse_cli_args():
    """Define parser w/arguments.
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--usd-to-eur", help="USD to EUR", nargs='+', type=float)
    group.add_argument("--eur-to-usd", help="EUR to USD", nargs='+', type=float)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_cli_args()

    if args.usd_to_eur:
        args.usd_to_eur, convert_usd_to_eur, 'usd', 'eur'
    elif args.convert_eur_to_usd:
        args.convert_eur_to_usd, convert_eur_to_usd, 'eur', 'usd'
