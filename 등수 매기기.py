def solution(score):
    avg = []
    sortavg = []
    answer = []
    for i in score:
        avg.append(sum(i)/2)
    sortavg = sorted(avg, reverse=True)
    print(avg)
    for i in sortavg:
        if (sortavg.count(i) >= 2 and i >= 0):
            for j in range(1, sortavg.count(i), 1):
                sortavg[sortavg.index(i)+j] = -1
    print(sortavg)
    for i in avg:
        answer.append(sortavg.index(i)+1)
    return answer