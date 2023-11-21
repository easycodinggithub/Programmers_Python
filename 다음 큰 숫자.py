def solution(n):
    a = list(bin(n)[2:]).count('1')
    answer = n+1
    while True:
        b = list(bin(answer)[2:]).count('1')
        if (a == b):
            break
        answer += 1
    return answer
        