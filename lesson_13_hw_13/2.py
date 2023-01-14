"""Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.
Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""


import string


def pig_it(text):
    new_text = []
    for word in text.split():
        if word not in string.punctuation:
            new = word[1:] + word[0] + 'ay'
            new_text.append(new)
        else:
            new_text.append(word)
    return ' '.join(new_text)


print(pig_it('Hello world !'))
