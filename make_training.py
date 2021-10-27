"""
* Two tones – low frequency (500 Hz) and high frequency (2000 Hz)
* 5 of each
* 2 second gap
"""

import numpy as np

import pandas as pd


def make_run():
    # Valid trials
    tones1 = np.repeat(['tone_500.wav', 'tone_2000.wav'], [5, 5])
    df = pd.DataFrame()
    df['tone1'] = tones1
    df['relax'] = 5000
    # Randomize the order of the trials.
    return df.sample(len(df))


for i in range(1, 11):
    df = make_run()
    df.to_csv(f'train_{i:03d}.csv', index=None)
