# Do NOT use any external libraries

def solve(A, b):
    """A is a m x n matrix, and b is an n x 1 vector.
    returns: x, where x is the solution to the equation Ax = b
    if no solution exists, return -1
    if infinite solutions exist, return -2"""
    x = [0] * len(A[0]) 
    return x
    m = len(A)
    n = len(A[0])

    if len(b) != n:
        return -1

    augmented_matrix = [row[:] + [bi] for row, bi in zip(A, b)]

    for i in range(n):
        if augmented_matrix[i][i] == 0:
            for k in range(i + 1, m):
                if augmented_matrix[k][i] != 0:
                    augmented_matrix[i], augmented_matrix[k] = augmented_matrix[k], augmented_matrix[i]
                    break
            else:
                return -1

        pivot = augmented_matrix[i][i]
        for j in range(i, n + 1):
            augmented_matrix[i][j] /= pivot
        for k in range(m):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(i, n + 1):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    for i in range(m):
        if all(augmented_matrix[i][j] == 0 for j in range(n)) and augmented_matrix[i][n] != 0:
            return -2

    return [row[-1] for row in augmented_matrix]



def det(A):
    """calculates the determinant of A
    if A is not a square matrix, return 0"""
    n = len(A)

    if not all(len(row) == n for row in A):
        return 0

    if n == 1:
        return A[0][0]

    determinant = 0
    sign = 1

    for j in range(n):
        submatrix = [row[:j] + row[j + 1:] for row in A[1:]]
        determinant += sign * A[0][j] * det(submatrix)
        sign *= -1

    return determinant
