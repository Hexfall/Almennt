def split_matrix_game(matrix_game):
    '''
    Problem 1(2 points).
    Given a matrix game as a list of rows, return Rose’s and Colin’s payoff matrices.
    Input: matrix_game = ([[(1, 4), (2, 4), (3, 3)],[(3, 0), (1, 2), (2, 1)]])
    Run: split_matrix_game(matrix_game)
    Output: ([[1, 2, 3], [3, 1, 2]], [[4, 4, 3], [0, 2, 1]])
    '''
    rose = [[column[0] for column in row] for row in matrix_game]
    coln = [[column[1] for column in row] for row in matrix_game]
    return (rose, coln)

def roses_best_pure_responses(matrix_and_strategy):
    '''
    Problem 2(15 points).
    Given a tuple of a matrix game and a mixed strategy for Colin, return a set of indices indicating Rose’s best pure responses.
    Note that the matrix game is a list of rows and that we zero-index in python/sage.
    Also note that Colin’s input strategy is a transpose of the actual column vector he uses.
    Hint: Start your code matrix_game, colins_strategy = matrix_and_strategy
    Input: matrix_and_strategy = ([[(1, 4), (2, 4), (3, 3)],[(3, 0), (1, 2), (2, 1)]],[1/2, 0, 1/2])
    Run: roses_best_pure_responses(matrix_and_strategy)
    Output: set([0])
    '''
    pass

def colins_best_pure_responses(matrix_and_strategy):
    '''
    Problem 3(10 points).
    Given a tuple of a matrix game and a mixed strategy for Rose, return a set of indices indicating Colin’s best pure responses.
    Note that the matrix game is a list of rows and that we zero-index in python.
    Hint: Start your codematrix_game, roses_strategy = matrix_and_strategy
    Input: matrix_and_strategy = ([[(1, 4), (2, 4), (3, 3)],[(3, 0), (1, 2), (2, 1)]],[1, 0])
    Run: colins_best_pure_responses(matrix_and_strategy)
    Output: set([0, 2])
    '''
    pass

def pure_nash_equilibria(matrix_and_strategy):
    '''
    Problem 4(15 points).
    Given a matrix game, return the matrix indicative of its pure nash equilibria.
    The matrix answer: The matrix returned should have the same size as the matrix game. 
    Each entry[i][j] of the matrix should be True if a pure strategy for Rose calling on row i and a pure strategy for Colin calling on column j form a pure nash equilibrium. 
    Note that the matrix game is a list of rows and that we zero-index in python.

    Input: matrix_game = [[(1, 4), (2, 4), (3, 3)],[(3, 0), (1, 2), (2, 1)]]
    Run: pure_nash_equilibria(matrix_and_strategy)
    Output: [[False, True, False], [False, False, False]]

    Input: matrix_game = [[(2, 1), (0, 0)], [(0, 0), (1, 2)]]
    Run: pure_nash_equilibria(matrix_and_strategy)
    Output: [[True, False], [False, True]]
    '''
    pass

def response_cardinality_matrix(matrix_and_strategy):
    '''
    Problem 5(8 points).
    Given a matrix game, return the matrix indicative of its number of mixed solutions.
    The matrix answer: The matrix returned should have the same size as the matrix game. 
    Each entry[i][j] of the matrix should be a tuple(a, b); where a is the total number of Rose’s best mixed responses to Colin’s pure strategy that calls on column j, and b is the total number of Colin’s best mixed responses to Rose’s pure strategy that calls on row i. 
    Note that the matrix game is a list of rows and that we zero-index in python.
    
    Input: matrix_game = [[(1, 4), (2, 4), (3, 3)],[(3, 0), (1, 2), (2, 1)]]
    Run: response_cardinality_matrix(matrix_and_strategy)
    Output: [[(1, +Infinity), (1, +Infinity), (1, +Infinity)],[(1, 1), (1, 1), (1, 1)]]

    Input: matrix_game = [[(2, 1), (0, 0)], [(0, 0), (1, 2)]]
    Run: response_cardinality_matrix(matrix_and_strategy)
    Output: [[(1, 1), (1, 1)], [(1, 1), (1, 1)]]
    '''
    pass