#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMATRIX = [list(map(lambda j:j*j, i)) for i in matrix]
    return (newMATRIX)
