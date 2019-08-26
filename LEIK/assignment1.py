
def pick_up_bricks_type(position):
    """
    Given an arbitrary position in pick up bricks return its
    type. A pick-up bricks position will be represented by an integer corresponding to
    the number of bricks in the pile. You should output the character N, L, R or P.
        Input: position = 6
        Run: pick_up_bricks_type(position)
        Output: "P"
    """
    pass

def chop_type(position):
    """
    Given an arbitrary position in chop return its type. A
    chop position will be represented as a tuple, e.g. (3,4) corresponds to the position
    consisting of a 3  4 plank. You should output the character N, L, R or P.
        Input: position = (2, 3)
        Run: chop_type(position)
        Output: "N"
    """
    pass

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
    pass

if __name__ == "__main__":
    # You can test things here
    position = 6
    print(pick_up_bricks_type(position))

    position = (2, 3)
    print(chop_type(position))

    position = [(2,2),(2,1)]
    print(cut_cake_type(position))