def solution(rank, attendance):
    answer = []
    for i in range(0, len(rank), 1):
        if (attendance[i] == True):
            answer.append(rank[i])
    answer = sorted(answer)
    return rank.index(answer[0])*10000+rank.index(answer[1])*100+rank.index(answer[2])