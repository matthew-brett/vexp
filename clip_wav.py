#!/usr/bin/env python3
""" Clip wav file
"""

import os.path as op
from argparse import ArgumentParser, RawDescriptionHelpFormatter

import numpy as np
import scipy.io.wavfile as siow


def clip_wav(wav_fname, out_fname, clip_length):
    samplerate, data = siow.read(str(wav_fname))
    # Scale to max
    data = data.astype(np.float32)
    data = data / np.max(np.abs(data))
    if data.ndim == 2:
        data = np.mean(data, axis=1)
    desired_n = int(samplerate * clip_length)
    out_data = np.zeros(desired_n, dtype=data.dtype)
    out_n = np.min([desired_n, len(data)])
    out_data[:out_n] = data[:out_n]
    siow.write(out_fname, samplerate, out_data)


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('wav_fname',
                        help='Wav file to clip')
    parser.add_argument('clip_length', type=float,
                        help='Clip length in seconds')
    parser.add_argument('--out-fname', '-o',
                        help='Output filename (default is input with '
                        '"_clipped" suffix')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.out_fname is None:
        pth, ext = op.splitext(args.wav_fname)
        args.out_fname = f'{pth}_clipped{ext}'
    clip_wav(args.wav_fname, args.out_fname, args.clip_length)


if __name__ == '__main__':
    main()
