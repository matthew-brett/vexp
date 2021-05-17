""" Make clip with different frequencies
"""

import numpy as np
import scipy.io.wavfile as siow


clips = {'tone_500': {'freq': 500,
                      'duration': 250},
         'tone_2000': {'freq': 2000,
                       'duration': 250}}


def make_tone(freq, duration, rate=44100):
    secs = duration / 1000
    print(freq)
    n_samps = int(rate * secs)
    t = np.linspace(0., secs, n_samps)
    amplitude = np.iinfo(np.int16).max
    return amplitude * np.sin(2. * np.pi * freq * t)


def write_tone(fname, cdict, rate=44100):
    tone = make_tone(rate=rate, **cdict)
    siow.write(fname, rate, tone)


for cname, cdict in clips.items():
    write_tone(cname + '.wav', cdict)
