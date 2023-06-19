def solution(l, r):
    answer = [5]
    result = []
    up = 0
    while True:
        x = answer[up]*10
        y = x+5
        if (x > r or y > r):
            break
        answer.append(x)
        answer.append(y)
        up += 1
    for i in answer:
        if (i >= l and i <= r):
            result.append(i)
        
    if (len(result) <= 1):
        return [-1]
    return result
        
        