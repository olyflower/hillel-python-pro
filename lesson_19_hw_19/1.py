"""https://www.codewars.com/kata/546f922b54af40e1e90001da"""

import re


def alphabet_position(text):
    res = []
    ALPHABET = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    new_text = re.sub(r'[.,!?\'\"]', '', text.lower())
    for letter in new_text.replace(" ", ""):
        if letter in ALPHABET:
            res.append(ALPHABET.index(letter))

    return ' '.join(list(map(str, res)))
