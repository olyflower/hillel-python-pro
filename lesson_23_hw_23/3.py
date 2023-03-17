import random
from nltk.corpus import words


def english_words(n):
    return [random.choice(words.words()) for _ in range(n)]


print(english_words(10))
