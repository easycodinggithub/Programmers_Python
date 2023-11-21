def solution(N, stages):
    score = {}
    temp = []
    answer = []
    for i in range(1, N+1, 1):
        score[str(i)] = ""
    
    for i in range(1, N+1, 1):
        n = 0
        m = 0
        for j in stages:
            if (i == j):
                n += 1
                m += 1
            elif (i < j):
                m += 1
        if (m > 0 and n > 0):
            score[str(i)] = n/m
        else:
            score[str(i)] = 0
            
    temp = sorted(score.items(), key=lambda x: x[1], reverse=True)
    for i in temp:
        answer.append(int(i[0]))
    return answer
        