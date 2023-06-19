def solution(n, t):
    answer = n
    for i in range(0, t, 1):
        answer *= 2
    return answer