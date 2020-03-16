#!/usr/bin/env python 3

"""Currency conversion utility w/argument parsing.
"""

import argparse
from forex_python.converter import get_rate

EUR_TO_USD = get_rate('EUR', 'USD')

def convert_usd_to_eur(usd):
    """Convert USD to EUR.
    """
    return usd/EUR_TO_USD

def convert_eur_to_usd(eur):
    """Convert EUR to USD.
    """
    return eur*EUR_TO_USD

def parse_cli_args():
    """Define command line parser w/arguments.
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--usd-to-eur", help="convert usd to eur", nargs='+', type=float)
    group.add_argument("--eur-to-usd", help="convert eur to usd", nargs='+', type=float)
    args = parser.parse_args()
    return args

def conversion_table(col1, col2_func, c1_hdr, c2_hdr):
    """Formatted table with two (2) columns and two (2) headers.
    """

    print('+------------+------------+')
    print('| {:^10} | {:^10} |'.format(c1_hdr, c2_hdr))
    print('+============+============+')
    for x_value in col1:
        y_value = col2_func(x_value)
        print('| {:10.4f} | {:10.4f} |'.format(x_value, y_value))
    print('+------------+------------+')

if __name__ == '__main__':
    args = parse_cli_args()

    if args.usd_to_eur:
        conversion_table(args.usd_to_eur, convert_usd_to_eur, 'usd', 'eur')
    else:
        conversion_table(args.eur_to_usd, convert_eur_to_usd, 'eur', 'usd')
