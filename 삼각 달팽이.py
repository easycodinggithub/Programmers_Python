def solution(n):
    answer = []
    temp = []
    for i in range(n):
        temp2 = []
        for j in range(0, i+1, 1):
            temp2.append(0)
        temp.append(temp2)
    
    limit = n
    change = 1
    
    i = -1
    j = 0
    
    s = 0
    while True:
        if limit <= 0:
            break
        if change > 3:
            change = 1
            
        if change == 1:
            # 1번 규칙
            for k in range(limit):
                s += 1
                i += 1
                temp[i][j] = s
            # print(temp)
        elif change == 2:
            # 2번 규칙
            for k in range(limit):
                s += 1
                j += 1
                temp[i][j] = s
            # print(temp)
        else:
            # 3번 규칙
            for k in range(limit):
                s += 1
                i -= 1
                j -= 1
                temp[i][j] = s
            # print(temp)
        change += 1
        limit -= 1
    
    for i in temp:
        for j in i:
            answer.append(j)
    return answer
        