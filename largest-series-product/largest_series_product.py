def largest_product(series, size):
    if series == "" and size != 0:
        raise ValueError("span must be smaller than string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must be smaller than string length")

    max_mul = 0
    for i in range(0, len(series) - size + 1):
        mul = 1
        for j in range(i, i + size):
            if not series[j].isdigit():
                raise ValueError("digits input must only contain digits")
            mul *= int(series[j])
        if mul > max_mul:
            max_mul = mul
    return max_mul
