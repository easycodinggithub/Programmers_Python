def solution(n):
    i = 1
    number3 = 1
    while (True):
        if (number3 % 3 == 0 or '3' in str(number3)):
            number3 += 1
            continue
        if (i >= n):
            break
        number3 += 1
        i += 1
    return number3 