def solution(n):
    answer = [2]
    
    for i in range(2, n+1, 1):
        check = 0
        for j in answer:
            if j > i**0.5:
                break
            if i % j == 0:
                check = 1
                break
        if check == 0:
            answer.append(i)
    return len(answer)-1