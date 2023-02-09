"""https://www.codewars.com/kata/5266876b8f4bf2da9b000362"""


def likes(names):
    if len(names) == 0:
        return f"no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) > 3:
        count = len(names) - 2
        return f"{names[0]}, {names[1]} and {count} others like this"


