"""Given a lottery ticket (ticket), represented by an array of 2-value arrays,
you must find out if you've won the jackpot. If your total is more than or equal to (win),
return 'Winner!'. Else return 'Loser!'.
Example ticket:
[ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]"""


def bingo(ticket, win):
    rez = 0
    for i in ticket:
        for j in i[0]:
            if ord(j) == i[1]:
                rez += 1
    if rez >= win:
        return 'Winner!'
    return 'Loser!'


print(bingo([['ABC', 65], ['BEE', 66], ['ATY', 74]], 1))
