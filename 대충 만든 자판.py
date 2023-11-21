def solution(keymap, targets):
    answer = []
    for i in targets:
        sum = 0
        for j in i:
            temp = []
            for k in range(0, len(keymap), 1):
                temp.append(keymap[k].find(j))  
            if max(temp) < 0:
                sum = -1
                break
            else:
                if min(temp) < 0:
                    ttemp = []
                    for i in temp:
                        if i != -1:
                            ttemp.append(i)
                    sum += min(ttemp)+1
                else:
                    sum += min(temp)+1
        if sum < 0:
            answer.append(-1)
        else:
            answer.append(sum)
    return answer