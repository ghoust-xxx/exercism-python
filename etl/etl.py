def transform(legacy_data):
    res = {}
    for x in legacy_data:
        for val in legacy_data[x]:
            res[val.lower()] = x
    return res
