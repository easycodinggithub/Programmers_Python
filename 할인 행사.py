def solution(want, number, discount):
    temp = []
    answer = 0
    
    for i in range(0, len(discount)-9, 1):
        temp.append(discount[i:i+10])
    
    for a in temp:
        tempn = [0 for i in range(len(number))]
        for i in a:
            if i in want:
                tempn[want.index(i)] += 1
        check = 0
        for i in range(0, len(number), 1):
            if number[i] != tempn[i]:
                check = 1
        if check == 0:
            answer += 1
    return answer
    