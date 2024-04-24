#!/usr/bin/python3
"""
def minOperations function
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    """
    minOper = 2
    totalOper = 0
    while n > 1:
        while n % minOper == 0:
            totalOper += minOper
            n /= minOper
        minOper += 1
    return totalOper
