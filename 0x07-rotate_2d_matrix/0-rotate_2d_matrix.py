#!/usr/bin/python3
""" Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """ 2D matrix, rotate it 90 degrees clockwise """
    ind = 0
    for v in list(zip(*matrix)):
        matrix[ind][:] = v[::-1]
        ind += 1
