"""def new_format(string):
   # code here"""


def new_format(value):
    format_value = [value[0]]
    for i in range(1, len(value)):
        if (len(value) - i) % 3 == 0:
            format_value.append('.')
        format_value.append(value[i])
    return ''.join(format_value)


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
