def solution(n):
    count = 0
    if (n % 2 == 0):
        for i in range(2, n+1, 2):
            count += i*i
    else:
        for i in range(1, n+1, 2):
            count += i
    return count
