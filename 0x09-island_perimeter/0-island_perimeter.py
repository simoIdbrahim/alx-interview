#!/usr/bin/python3
""" Create a function def island_perimeter(grid) """


def island_perimeter(grid):
    """
      returns the perimeter of the island described in grid
    """
    len = len(grid)
    bre = len(grid[0])
    perimeter = 0
    for i in range(len):
        for j in range(bre):
            if grid[i][j] == 1:
                perimeter += 4
                if (j < bre - 1 and grid[i][j + 1] == 1):
                    perimeter -= 2
                if (i < len - 1 and grid[i + 1][j] == 1):
                    perimeter -= 2
    return perimeter
