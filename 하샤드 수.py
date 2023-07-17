def solution(x):
    n = list(str(x))
    sum = 0
    for i in n:
        sum += int(i)
    if (x % sum == 0):
        return True
    return False