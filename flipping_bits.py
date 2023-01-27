"""Solution to flipping bits problem."""


def flippingBits(n: int) -> int:
    """Bit flipping

    Args:
        n (int): Any integer.
    """
    bit_32 = "{:032b}".format(n)
    out = []
    for bit in bit_32:
        out.append("1") if bit == "0" else out.append("0")
    return int("".join(out), 2)


print(flippingBits(9))
