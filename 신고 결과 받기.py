def solution(id_list, report, k):
    r = {}
    ru = []
    answer = {}
    final = []
    for i in id_list:
        r[i] = 0
        answer[i] = 0
    report = list(set(report))
    for i in report:
        t, v = i.split(' ')
        r[v] += 1
    for i in r:
        if r[i] >= k:
            ru.append(i)
    for i in report:
        t, v = i.split(' ')
        if v in ru:
            answer[t] += 1
    for i in answer:
        final.append(answer[i])
    return final