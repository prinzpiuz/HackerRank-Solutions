"""Solution for mars exploration problem."""


def marsExploration(s: str) -> int:
    """To find the varied sos signal recieved on earth.

    Args:
        s (str): String as received on Earth.

    Returns:
        int: Deviated chars count

    """
    count = 0
    parsed_message = ""
    message = "SOS"
    for i, let in enumerate(s, start=1):
        parsed_message += let
        if i % 3 == 0:
            if parsed_message == message:
                parsed_message = ""
                continue
            for k, j in enumerate(parsed_message):
                if j == message[k]:
                    continue
                count += 1
            parsed_message = ""
    return count


print(marsExploration("SOSOOSOSOSOSOSSOSOSOSOSOSOS"))
