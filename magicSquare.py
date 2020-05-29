import math
import os
import random
import re
import sys


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    array = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]], [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
             [[4, 9, 2], [3, 5, 7], [8, 1, 6]], [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
             [[8, 3, 4], [1, 5, 9], [6, 7, 2]], [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
             [[4, 3, 8], [9, 5, 1], [2, 7, 6]], [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

    value = []
    for i in range(len(array)):
        second = []
        # defining rows
        for j in range(len(array[i])):
            third = []
            # defining columns
            for k in range(len(array[i][j])):
                third.append(abs(array[i][j][k] - s[j][k]))
            second.append(sum(third))
        value.append(sum(second))

    return int(min(value))


if __name__ == '__main__':
    s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
    result = formingMagicSquare(s)

    print(result)
