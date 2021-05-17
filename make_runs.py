"""
* Two tones – low frequency (500 Hz) and high frequency (2000 Hz)
* Tone duration 250 msec
* Random gap between tones of 2-3 seconds.
* Number of tones: 25 of each one
* Number of trials: 50
* Random presentation
* Trial type: 40 valid or 10 invalid
* Experiment starts with “keypress” SPACE
* Every 25 trials, stop presentation and wait for “keypress” SPACE to continue
"""

import numpy as np
import numpy.random as npr

import pandas as pd


def make_run():
    # Valid trials
    types = np.repeat(['valid', 'invalid'], [40, 10])
    tones1 = np.repeat(['tone_500', 'tone_2000'], [20, 20])
    tones2 = tones1.copy()
    tones1 = np.append(tones1, ['tone_500'] * 5)
    tones2 = np.append(tones2, ['tone_2000'] * 5)
    tones1 = np.append(tones1, ['tone_2000'] * 5)
    tones2 = np.append(tones2, ['tone_500'] * 5)
    df = pd.DataFrame()
    df['type'] = types
    df['tone1'] = tones1
    df['gap'] = npr.randint(2000, 3000, size=len(df))
    df['tone2'] = tones2
    return df.sample(len(df))


for i in range(1, 11):
    df = make_run()
    df.to_csv(f'run_{i:03d}.csv', index=None)