def solution(n):
    answer = 1
    sum = 1
    while True:
        sum *= answer
        if (sum > n):
            break
        answer += 1
    return answer-1