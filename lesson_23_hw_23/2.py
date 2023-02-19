import random

from english_words import get_english_words_set

word_set = get_english_words_set(['web2'], lower=True)


def words(number):
    return [random.choice(list(word_set)) for _ in range(number)]


print(words(10))
