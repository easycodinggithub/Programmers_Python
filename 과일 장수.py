def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    for i in range(0, len(score)//m):
        answer += min(score[i*m:(i+1)*m])*m
    return answer