def solution(s):
    temp = []
    answer = []
    for i in list(s):
        check = 0
        count = 0
        for j in range(len(temp)-1, -1, -1):
            if (i == temp[j]):
                check = count+1
                break
            count += 1
        if (check > 0):
            answer.append(check)
        else:
            answer.append(-1)
        temp.append(i)
    return answer