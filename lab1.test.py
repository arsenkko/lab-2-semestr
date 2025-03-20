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

class TestZigzag(unittest.TestCase):
    def test_matrix(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        expected = [4, 8, 12, 16, 15, 11, 7, 3, 2, 6, 10, 14, 13, 9, 5, 1]
        self.assertEqual(zigzag(matrix), expected)

if __name__ == "__main__":
    unittest.main()

