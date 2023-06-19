def solution(n):
    maxnum = n//10
    for i in range(1, maxnum, 1):
        if (i*i==n):
            return 1
    return 2