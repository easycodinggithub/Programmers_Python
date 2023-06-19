def solution(before, after):
    b = list(before)
    a = list(after)
    for i in b:
        for j in a:
            if (i == j):
                a.remove(i)
                break
    if (len(a) <= 0):
        return 1
    else:
        return 0