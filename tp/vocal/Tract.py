import numpy as np


def PN(B, Fn, Fs):
    return np.exp(-2 * np.pi * B / Fs) * np.exp(1j * 2 * np.pi * Fn / Fs)


def generate(B, Fn, Fs):
    """
    :return: H(z)
    """
    pn = PN(B, Fn, Fs)
    pn_c = np.conj(pn)

    def H(z):
        d = (1 - pn / z) * (1 - pn_c / z)
        return 1 / d

    return H
