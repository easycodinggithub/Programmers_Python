def solution(n):
    if (n == 1):
        return 4
    for i in range(1, n//2, 1):
        if (i*i==n):
            return (i+1)**2
    return -1