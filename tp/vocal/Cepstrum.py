import numpy as np


def h1(x):
    s1 = np.fft.rfft(x)
    s2 = np.abs(s1)
    s2[s2 == 0] = 1
    return np.log(s2)


def h2(Y):
    return np.fft.irfft(Y)


def generate(x):
    """
    :param x: x[n]
    :return: c[n] = F^-1 {log(F{x[n]})}
    """
    return h2(h1(x))


