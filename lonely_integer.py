"""Solution for lonly integer problem.
"""


def lonelyinteger(a: list) -> int:
    """To find the integer which only occur once.

    Args:
        a (list): Integer list.

    Returns:
        int: Lonely integer.

    """
    count_dict = {}
    for val in a:
        if count_dict.get(val, True):
            count_dict[val] = 0
        else:
            count_dict[val] = count_dict[val] + 1
    for key, val in count_dict.items():
        if val == 0:
            return key


print(
    lonelyinteger(
        [34, 95, 34, 64, 45, 95, 16, 80, 80, 75, 3, 25, 75, 25, 31, 3, 64, 16, 31]
    )
)
