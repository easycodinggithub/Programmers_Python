def solution(x, n):
    answer = []
    if (x == 0):
        for i in range(n):
            answer.append(0)
        return answer
    limitn = 0
    if (x*n < 0):
        limitn = (x*n)-1
    else:
        limitn = (x*n)+1
    for i in range(x, limitn, x):
        answer.append(i)
    return answer