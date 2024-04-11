#!/usr/bin/python3
"""
Create a function def pascal_triangle(n):
that returns a list of lists of
integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """Generates a Pascal's triangle of size n."""

    if n <= 0:
        return []

    triangle = []
    triangle.append([1])

    for i in range(1, n):
        previous_row = triangle[i - 1]
        current_row = []

        current_row.append(1)

        for j in range(1, i):
            current_row.append(previous_row[j - 1] + previous_row[j])

        current_row.append(1)

        triangle.append(current_row)

    return triangle

