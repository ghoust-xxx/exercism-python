def sum_of_multiples(limit, multiples):
    mult = {}
    for i in multiples:
        tmp = i
        if tmp == 0:
            continue
        while tmp < limit:
            mult[tmp] = True
            tmp += i

    res = 0
    for i in mult:
        res += i

    return res
