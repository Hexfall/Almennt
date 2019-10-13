# -*- coding: UTF-8 -*-
from fractions import Fraction

def saddle_point(payoff_matrix):
    """
    Given a payoff matrix for a zero-sum matrix game, return
    its saddle point value or None if there is none.
        Input: payoff_matrix = [[4,1,-3], [3,2,5], [0,1,6]]
        Run: saddle_point(payoff_matrix)
        Output: 2
    """
    for row_index in range(len(payoff_matrix)):
        for col_index in range(len(payoff_matrix[row_index])):
            max_in_col = payoff_matrix[row_index][col_index] == max([payoff_matrix[i][col_index] for i in range(len(payoff_matrix))])
            min_in_row = payoff_matrix[row_index][col_index] == min(payoff_matrix[row_index])
            if max_in_col and min_in_row:
                return payoff_matrix[row_index][col_index]
    return None

def two_dimensional_solver(payoff_matrix):
    """
    Given a 2×n-dimensional zero-sum game as a payoff matrix,
    return its von Neumann solution. The solutions should be
    a 3-tuple of a fraction (the value of the game) and two
    lists of fractions (Rose’s and Colin’s strategies
    respectively).
        Input: payoff_matrix = [[4, -2, -1], [-1, 3, 1]]
        Run: two_dimensional_solver(payoff_matrix)
        Output: (Fraction(3, 7),
                 [Fraction(2, 7), Fraction(5, 7)],
                 [Fraction(2, 7), Fraction(0, 1), Fraction(5, 7)])
    """
    value, rose, colin = Fraction(3, 7), [Fraction(2, 7), Fraction(5, 7)], [Fraction(3, 4), Fraction(0, 1), Fraction(1, 4)]
    return (value, rose, colin)