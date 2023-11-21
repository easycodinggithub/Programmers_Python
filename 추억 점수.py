def solution(name, yearning, photo):
    score = {}
    answer = []
    for i in range(0, len(name), 1):
        score[name[i]] = yearning[i]
    for i in photo:
        temp = 0
        for j in i:
            if j in score:
                temp += score[j]
        answer.append(temp)
    return answer
    