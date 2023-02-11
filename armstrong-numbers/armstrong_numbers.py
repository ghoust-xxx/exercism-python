def is_armstrong_number(number):
    p = len(str(number))
    cnt = 0
    for c in str(number):
        cnt += pow(int(c), p)
    return cnt == number
