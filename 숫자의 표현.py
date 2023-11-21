def solution(n):
    answer = 1
    for i in range(1, n//2+1, 1):
        total = 0
        j = i
        while True:
            if total == n:
                answer += 1
                break
            if total > n:
                break
            total += j
            j += 1
    return answer
            
            
                