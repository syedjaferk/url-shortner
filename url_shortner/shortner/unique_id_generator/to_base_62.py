def to_base62(num):
    """    Convert a given number to its base-62 representation.

    This function takes a positive integer and converts it to its base-62 representation using the characters
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.

    Args:
        num (int): A positive integer to be converted to base-62 representation.

    Returns:
        str: The base-62 representation of the input number.
    """

    base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        num, remainder = divmod(num, 62)
        result = base62[remainder] + result
    return result
