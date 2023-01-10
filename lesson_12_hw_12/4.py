"""Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words reversed
(Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"""


def spin_words(sentence):
    new_sentence = []
    for i in sentence.split():
        if len(i) <= 4:
            new_sentence.append(i)
        else:
            new_sentence.append(''.join(reversed(i)))
    result = ' '.join(new_sentence)
    return result


print(spin_words("Hey fellow warriors"))
