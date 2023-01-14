"""Write an algorithm that takes an array and moves all of the zeros to the end, preserving
the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]"""


def move_zeros(lst):
    new_lst = []
    for i in lst:
        if i != 0:
            new_lst.append(i)
    number_zeros = len(lst) - len(new_lst)
    new_lst.extend([0] * number_zeros)
    return new_lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
