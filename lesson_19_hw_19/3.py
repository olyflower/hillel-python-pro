"""https://www.codewars.com/kata/52774a314c2333f0a7000688"""


def valid_parentheses(string):
    parentheses_counter = 0
    for i in string:
        if i == '(':
            parentheses_counter += 1
        if i == ')':
            parentheses_counter -= 1
        if parentheses_counter < 0:
            return False
    if parentheses_counter == 0:
        return True
    else:
        return False
