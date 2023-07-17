def solution(num):
    if (num == 1):
        return 0
    count = 1
    n = num
    for i in range(500):
        n = f(n)
        if (n == 1):
            return count
        count += 1
    return -1

def f(n):
    if (n % 2 == 0):
        return n//2
    else:
        return n*3+1