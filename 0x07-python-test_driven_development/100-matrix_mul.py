#!/usr/bin/python3
"""
This module multiplies 2 matrices
Both matrices must be of type list and can not be empty
All rows must be the same size
"""


def matrix_mul(m_a, m_b):
    """ Checks for list type of each matrix, multiply one matrix by second """
    if isinstance(m_a, list) is False:
        raise TypeError('m_a must be a list')
    if isinstance(m_b, list) is False:
        raise TypeError('m_b must be a list')
    if isinstance(m_a[0], list) is False:
        raise TypeError('m_a must be a list of lists')
    if isinstance(m_b[0], list) is False:
        raise TypeError('m_b must be a list of lists')
    if m_a is None or m_a[0] is None:
        raise ValueError('m_a can\'t be empty')
    if m_b is None or m_b[0] is None:
        raise ValueError('m_b can\'t be empty')
    for row in m_a:
        for x in row:
            if isinstance(x, (int, float)) is False:
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        for y in row:
            if isinstance(y, (int, float)) is False:
                raise TypeError('m_b should contain only integers or floats')
    for row in m_a:
        if len(m_a[0]) != len(row):
            raise TypeError('each row of m_a must be of the same size')
    for row in m_b:
        if len(m_b[0]) != len(row):
            raise TypeError('each row of m_b must be of the same size')
    if m_a == [] and m_a == [[]] and m_b == [] and m_b == [[]]:
        raise ValueError('m_a and m_b can\'t be multiplied')
    M = [[0 for col in range(len(m_b[0]))] for row in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_a[0])):
                M[i][j] += m_a[i][k] * m_b[k][j]
    return M
