"""Solution for counting valleys problem

NB: This is not solution i found
"""


def countingValleys(steps: int, path: str) -> int:
    """To find the valleys travesed from the string path.

    Args:
        steps (int): Total no of steps taken.
        path (str): Path String.

    Returns:
        int: Count of valleys traversed.
        
    """
    height = 0
    valleys = 0
    for step in path:
        if step == "D" and height == 0:
            height -= 1
            valleys += 1
        elif step == "D":
            height -= 1
        else:
            height += 1
    return valleys
