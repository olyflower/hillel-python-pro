"""Convert strings to how they would be written by Jaden Smith.
The strings are actual quotes from Jaden Smith, but they are not capitalized
in the same way he originally typed them.

Example:
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"""


def to_jaden_case(string):
    lst = list(map(lambda item: item.capitalize(), string.split()))
    result = ' '.join(lst)
    return result


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
