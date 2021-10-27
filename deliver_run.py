#!/usr/bin/env python3
""" Deliver stimulus run
"""

import os.path as op
import time

from argparse import ArgumentParser, RawDescriptionHelpFormatter

import numpy as np
import pandas as pd

from playsound import playsound

import keyboard


def deliver_run(run_fname):
    run_df = pd.read_csv(run_fname)
    for i, row in run_df.iterrows():
        for v in np.array(row):
            if isinstance(v, str):
                if op.isfile(v):
                    playsound(v)
            elif isinstance(v, (int, float)):
                time.sleep(v / 1000)
        if i == 24:
            print('Press space to continue')
            keyboard.wait(" ")


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('run_fname',
                        help='CSV file defining run')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    print('Press Cntl-C to stop the run')
    deliver_run(args.run_fname)


if __name__ == '__main__':
    main()
