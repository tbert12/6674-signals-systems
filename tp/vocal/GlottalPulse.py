import numpy as np


def generate(Tp, Tn, P0):
    def _glottal_pulse(t):
        if 0 <= t <= Tp:
            return (P0 / 2.0) * (1 - np.cos((t / Tp) * np.pi))
        if Tp < t <= Tp + Tn:
            return P0 * np.cos(((t - Tp) * np.pi) / (Tn * 2))
        return 0

    return _glottal_pulse
