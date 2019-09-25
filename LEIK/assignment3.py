from fractions import Fraction
from math import ceil

def log2(num):
    if num == 1:
        return 0
    return 1 + log2(num // 2)

def dyadic_birthday(num):
    '''
    Given a dyadic number, return its birthday.
    Input: dyadic_number = -291/256
    Run: dyadic_birthday(dyadic_number)
    Output: 10
    '''
    offset = ceil(abs(num))
    log = log2(num.denominator)
    return offset + log


def dyadic_birthday_floating_point(num, current = 0, jump = 1):
    if num < 0:
        num = 0 - num
    if num == current:
        return 0
    if current + jump > num:
        return 1 + dyadic_birthday_floating_point(num, current, jump / 2)
    return 1 + dyadic_birthday_floating_point(num, current + jump, jump)

def simplicity_principle(moves):
    '''
    Given a position in a partizan game, return the dyadic number of its equivalent dyadic position.
    The position of the game is given as a tuple of two lists.
    They are the dyadic numbers associated with the positions Louiseand Richard can move to.
    Return None if the simplicity principle cannot be applied.
    Hint: start off your function with:louises_moves, richards_moves = position.
    Input: position = ([1/4], [1, 3/2])
    Run: simplicity_principle(position)
    Output: 1/2
    '''
    def oldest_between(lower, upper):
        def find_oldest(lower, upper, current = 0, step = 1):
            if lower < current + step < upper:
                return current + step
            if upper <= current + step:
                return find_oldest(lower, upper, current, step/2)
            return find_oldest(lower, upper, current + step, step)

        if lower < 0 < upper or upper < 0 < lower:
            return 0
        sign = 1
        if lower < 0:
            sign = -1
            lower = -lower
            upper = -upper
        if upper < lower:
            temp = lower
            lower = upper
            upper = temp
        return sign * find_oldest(lower, upper)
    if moves[0] == []:
        moves[0].append(-float('inf'))
    if moves[1] == []:
        moves[1].append(float('inf'))
    if max(moves[0]) > min(moves[1]):
        return None
    return oldest_between(max(moves[0]), min(moves[1]))