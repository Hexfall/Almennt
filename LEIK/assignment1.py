from math import log2, floor

def pick_up_bricks_type(position):
    """
    Given an arbitrary position in pick up bricks return its
    type. A pick-up bricks position will be represented by an integer corresponding to
    the number of bricks in the pile. You should output the character N, L, R or P.
        Input: position = 6
        Run: pick_up_bricks_type(position)
        Output: "P"
    """
    if position % 3:
        return 'N'
    return 'P'

def chop_type(position):
    """
    Given an arbitrary position in chop return its type. A
    chop position will be represented as a tuple, e.g. (3,4) corresponds to the position
    consisting of a 3  4 plank. You should output the character N, L, R or P.
        Input: position = (2, 3)
        Run: chop_type(position)
        Output: "N"
    """
    if position[0] == position[1]:
        return 'P'
    return 'N'

def cut_cake_type(position):
    """
    Given an arbitrary position in cut-cake return its type.
    A cut-cake position will be represented as a list of tuples, e.g. [(1,2),(3,4)]
    corresponds to the position consisting of 1  2 and 3  4 pieces of cake. You should
    output the character N, L, R or P.
        Input: position = [(2,2),(2,1)]
        Run: cut_cake_type(position)
        Output: "R"
    """
    def louise_moves(position):
        if position == [] or not [True for i in position if i[0] != 1]:
            return {'R'}
        moves = set()
        for i in position:
            for j in range(i[1]-1):
                new_position = [position[cake] for cake in range(len(position)) if cake != i]
                if not (i[0] == 1 and (i[1] - (j + 1)) == 1):
                    new_position.append((i[0], i[1] - (j + 1)))
                if not (i[0] == 1 and (j + 1) == 1):
                    new_position.append((i[0], j + 1))
                moves.add(richard_moves(new_position))
        return moves

    def richard_moves(position):
        if position == [] or not [True for i in position if i[1] != 1]:
            return {'L'}
        moves = set()
        for i in position:
            for j in range(i[0]-1):
                new_position = [position[cake] for cake in range(len(position)) if cake != i]
                if not (i[1] == 1 and (i[0] - (j + 1)) == 1):
                    new_position.append((i[1] - (j + 1), i[1]))
                if not (i[1] == 1 and (j + 1) == 1):
                    new_position.append((j + 1, i[1]))
                moves.add(richard_moves(new_position))
        return moves

    l = louise_moves(position)
    r = richard_moves(position)
    print((l, r))

def cut_cake_score(position):
    RScore, LScore = 0, 0
    for i in position:
        if i[0] == 1 and i[1] == 1:
            continue
        if i[1] == 1:
            RScore += i[0] - 1
        elif i[0] == 1:
            LScore += i[1] - 1
        else:
            RScore += int(floor(log2(i[0])))
            LScore += int(floor(log2(i[1])))
    if RScore == LScore:
        return 'P'
    if RScore < LScore:
        return 'L'
    return 'R'

if __name__ == "__main__":
    # You can test things here
    position = 6
    print(pick_up_bricks_type(position))

    position = (2, 3)
    print(chop_type(position))

    position = [(2,2),(2,1)]
    print(cut_cake_type(position))
    print(cut_cake_score(position))