def solution(a, b, n):
    answer = 0
    while True:
        if (n < a):
            break
        n -= a
        answer += b
        n += b
    return answer
        
        
        
    