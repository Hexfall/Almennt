def win_nim(position):
    '''
    Teach a computer how to play Nim perfectly. If the computer starts at a type N
    position then no matter how the opponent plays, the computer will always
    win. A Nim-position is represented as a tuple of integers, e.g. (a, b, c),
    represents the position *a + *b + *c. The output should be a tuple of
    non-negative integers corresponding to a type P position.
    If the input is a type P position the program should output -1.
    '''
    return tuple()

def pick_up_bricks_nimber(position):
    '''
    Given a position in pick-up-bricks, return its equivalent nimber. A pick-up-bricks
    position is represented here by an integer.
        Input: position = 7
        Run: pick_up_bricks_nimber(position)
        Output: 1
    '''
    return position % 3

def pick_up_bricks_nimber_sum(position):
    '''
    Given a sum of positions in pick-up-bricks, return its equivalent
    nimber. The sum of positions is represented as a tuple of integers.
        Input: position = (7, 3, 4)
        Run: pick_up_bricks_nimber_sum(position)
        Output: 2
    '''
    return -1

if __name__ == "__main__":
    # You can test things here
    print(win_nim((3,4,5)))
    print(pick_up_bricks_nimber(7))
    print(pick_up_bricks_nimber_sum((7,3,4)))