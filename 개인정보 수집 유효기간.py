def solution(today, terms, privacies):
    y, m, d = today.split('.')
    y, m, d = int(y), int(m), int(d)
    limit = {}
    answer = []
    for i in terms:
        k, v = i.split(' ')
        limit[k] = int(v)
    for i in range(1, len(privacies)+1, 1):
        k, v = privacies[i-1].split(' ')
        yy, mm, dd = k.split('.')
        yy, mm, dd = int(yy), int(mm), int(dd)
        mm += limit[v]
        if mm > 12:
            if mm % 12 == 0:
                yy += (mm//12)-1
                mm = 12
            else:
                yy += mm//12
                mm = mm%12
        if yy < y or (yy == y and mm < m) or (yy == y and mm == m and dd <= d):
            answer.append(i)
    return answer
            