def to_base62(num):
    base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        num, remainder = divmod(num, 62)
        result = base62[remainder] + result
    return result
