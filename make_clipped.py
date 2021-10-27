#!python3
""" Clip /pad wav files to given length
"""

from pathlib import Path

from clip_wav import clip_wav

HERE = Path()

CLIP_LENGTH = 0.75

for pth in (HERE / 'originals').glob('*.wav'):
    out_fname = f'{pth.stem}_clipped.wav'
    clip_wav(pth, out_fname, CLIP_LENGTH)
