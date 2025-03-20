import unittest

def zigzag(matrix):
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    result = []

    for j in range(n-1, -1, -1):
        column = [matrix[i][j] for i in range(m)]  
        if (n - 1 - j) % 2 == 0:
            result.extend(column)
        else:
            result.extend(column[::-1]) 

    return result

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(zigzag(matrix))

