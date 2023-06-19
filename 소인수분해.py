def solution(n):
    pnum = []
    for i in range(2, n+1, 1):
        if (n % i == 0 and primary(i)):
            pnum.append(i)
    return pnum

def primary(i):
    for j in range(2, i, 1):
        if (i % j == 0):
            return False
    return True