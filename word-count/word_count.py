def count_words(sentence):
    sent = sentence.lower()
    res = {}
    word = False
    quote = False
    one = ""
    for c in sent:
        if c.isalpha() or c.isdigit():
            if quote:
                one += "'"
                quote = False
            one += c
            if word:
                continue
            else:
                word = True
                quote = False
            continue
        if c == "'":
            if word:
                quote = True
                continue
        if word:
            res[one] = res.get(one, 0) + 1
            one = ""
            word = False
        quote = False

    if word:
        res[one] = res.get(one, 0) + 1

    return res
