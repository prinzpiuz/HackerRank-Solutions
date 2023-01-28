"""Solution to the diagonal difference problem."""


def diagonalDifference(arr: list) -> int:
    """Difference between the diagonals of a square matrix.

    Args:
        arr (list): Square matrix array.

    Returns:
        int: Difference between the sum of diagonals.

    """
    square_size = len(arr)
    d1_sum = d2_sum = 0
    for i, _ in enumerate(arr):
        d1_sum += arr[i][i]
        d2_sum += arr[square_size - 1 - i][i]
    return abs(d1_sum - d2_sum)


print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
