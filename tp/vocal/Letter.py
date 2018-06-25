from typing import List


class Letter:
    def __init__(self, char='', start=0.0, end=0.0):
        self.char = char.upper()
        self.start = start
        self.end = end


class Word:
    def __init__(self, letters=List[Letter]):
        self.letters = letters
        self.start = 0.0
        self.end = 0.0
        if len(letters) > 0:
            self.start = self.letters[0].start
            self.end = self.letters[-1].end

    def __str__(self):
        return "".join([l.char for l in self.letters])


LETTERS_POSITION = [
    # Por Gastón
    Letter('c', 0.5544, 0.5666),
    Letter('o', 0.5788, 0.6216),
    Letter('n', 0.6644, 0.8660),
    Letter('t', 0.9216, 0.9316),
    Letter('a', 0.9416, 0.9954),
    Letter('g', 1.0492, 1.2076),
    Letter('i', 1.2076, 1.2444),
    Letter('a', 1.2812, 1.3712),

    Letter('e', 1.3712, 1.4262),
    Letter('n', 1.4812, 1.5168),
    Letter('e', 1.5524, 1.6142),
    Letter('r', 1.6760, 1.7190),
    Letter('g', 1.7620, 1.8352),
    Letter('i', 1.9084, 1.9858),
    Letter('a', 2.0632, 2.1648),

    Letter('y', 2.1648, 2.2924),

    Letter('f', 2.2924, 2.3702),
    Letter('e', 2.4480, 2.4982),
    Letter('r', 2.5484, 2.6332),
    Letter('v', 2.7180, 2.7554),
    Letter('o', 2.7928, 2.8690),
    Letter('r', 2.9452, 3.1292),
]

WORDS = {
    "contagia": Word(LETTERS_POSITION[:8]),
    "energia": Word(LETTERS_POSITION[8:15]),
    "y": Word(LETTERS_POSITION[15:16]),
    "fervor": Word(LETTERS_POSITION[16:]),
}
