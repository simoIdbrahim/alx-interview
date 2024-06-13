#!/usr/bin/python3
""" Create a function def island_perimeter(grid) """


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    length = len(grid)
    bre = len(grid[0])
    perimeter = 0
    for i in range(length):
        for j in range(bre):
            if grid[i][j] == 1:
                perimeter += 4
                if (j < bre - 1 and grid[i][j + 1] == 1):
                    perimeter -= 2
                if (i < length - 1 and grid[i + 1][j] == 1):
                    perimeter -= 2
    return perimeter
