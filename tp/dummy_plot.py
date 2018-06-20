from scipy.io import wavfile
from scipy import signal
from tp.vocal import Letter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def ej1():
    (FS, Y) = wavfile.read("res/hh15.WAV")

    # Duracion
    L = len(Y) / FS
    print("Rate: {} | Muestras: {} | Duracion {}s | Duracion/Muestras = {}".format(FS, len(Y), L, L / len(Y)))

    X = np.arange(0, len(Y)) / FS
    Y = Y / max(Y)  # Y normalizado
    plt.title('Senal de audio con fonemas', fontsize=20)
    plt.plot(X, Y)
    plt.xticks(np.arange(min(X), max(X), 0.2))

    UMBRAL = 0.05
    inicia_mudo = False
    for x, v in zip(X, Y):
        v = abs(v)
        if inicia_mudo and v > UMBRAL:
            plt.axvline(x=x, alpha=0.05, color="red")
            inicia_mudo = False
        if v <= UMBRAL and not inicia_mudo:
            # plt.axvline(x=x, linestyle='dotted', alpha=0.2, color="red")
            inicia_mudo = True

    red_patch = mpatches.Patch(color='red', label='Sonoros')
    white_patch = mpatches.Patch(color='white', label='Sordos')
    plt.legend(handles=[red_patch, white_patch])

    plt.xlabel('tiempo (s)')
    plt.ylabel('intensidad')

    for l in Letter.LETTERS_POSITION:
        y = 0.9
        x = l.start + 0.009
        plt.text(x, y, l.char)
        plt.axvline(x=l.start, color="yellow")

    plt.show()


def ej7():
    sample_rate, samples = wavfile.read('tp/res/hh15.WAV')

    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

    plt.specgram(frequencies, times)
    plt.imshow(spectrogram)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()


def main():
    # ej1()
    ej7()


if __name__ == "__main__":
    main()
