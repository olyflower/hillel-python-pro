"""In some countries of former Soviet Union there was a belief about lucky tickets.
A transport ticket of any sort was believed to posess luck if sum of digits
on the left half of its number was equal to the sum of digits on the right half. Here are examples of such numbers:
003111    #             3 = 1 + 1 + 1
813372    #     8 + 1 + 3 = 3 + 7 + 2
17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number when adding the halves.
56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6"""


def luck_check(string):
    length = len(string)
    left_side = string[:length // 2]
    if string.isdigit():
        if len(string) % 2 == 0:
            right_side = string[length // 2:]
            left_sum = sum(list(map(int, list(left_side))))
            right_sum = sum(list(map(int, list(right_side))))
            if left_sum == right_sum:
                return True
        if len(string) % 2 != 0:
            right_side = string[length // 2+1:]
            left_sum = sum(list(map(int, list(left_side))))
            right_sum = sum(list(map(int, list(right_side))))
            if left_sum == right_sum:
                return True
        return False
    raise Exception("Invalid input")


print(luck_check('683179'))
