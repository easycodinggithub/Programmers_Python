def solution(n, k):
    s = 0
    if (n >= 10):
        s = n//10
    return n*12000+k*2000-s*2000