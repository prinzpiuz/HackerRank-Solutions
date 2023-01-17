"""Solution for sparse arrays problem
"""

# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#


def matchingStrings(strings, queries):
    """To matching numbers.

    Args:
        strings (list): List of strings.
        queries (list): List of query string that need to be checked against strings.

    Returns:
        list: Cout of matched string as an array.
        
    """
    out = [x * 0 for x in range(len(queries))]
    for index, item in enumerate(queries):
        for string in strings:
            if item == string:
                out[index] += 1
    return out


if __name__ == "__main__":
    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    print(res)
