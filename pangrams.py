"""Solution for pangrams problem"""

import string


def pangrams(s: str) -> str:
    """Check wheather the given string is pangram or not.

    Args:
        s (str): Input string.

    Returns:
        str: Returns either `pangram` or `not pangram`.
        
    """
    contained_letters = []
    for letter in s.replace(" ", ""):
        letter = letter.lower()
        if not letter in contained_letters:
            contained_letters.append(letter)
    contained_letters.sort()
    if contained_letters == list(string.ascii_lowercase):
        return "pangram"
    return "not pangram"


print(pangrams("We promptly judged antique ivory buckles for the next prize"))
