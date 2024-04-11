#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    Generates a Pascal's triangle of size n.

    Args:
        n: An integer representing the number of rows in the triangle.

    Returns:
        A list of lists of integers representing the Pascal's triangle of size n.
        An empty list if n <= 0.
    """

    if n <= 0:
        return []

    triangle = []
    # Create the first row (always [1])
    triangle.append([1])

    # Iterate for subsequent rows (from row 2 to n)
    for i in range(1, n):
        previous_row = triangle[i - 1]
        current_row = []

        # First element of each row is always 1
        current_row.append(1)

        # Calculate elements in the middle based on previous row
        for j in range(1, i):
            current_row.append(previous_row[j - 1] + previous_row[j])

        # Last element of each row is always 1
        current_row.append(1)

        # Add the current row to the triangle
        triangle.append(current_row)

    return triangle

