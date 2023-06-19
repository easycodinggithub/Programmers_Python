def solution(a, d, included):
    sum = 0
    for i in range(0, len(included), 1):
        if (included[i]):
            sum += a + d * i 
    return sum