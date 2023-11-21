def solution(answers):
    length = len(answers)
    
    first = []
    second = []
    third = []
    
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    report = [0, 0, 0]
    
    count = 0
    for i in range(0, length+1, 1):
        if (i % 5 == 0):
            count = 0
        first.append(s1[count])
        count += 1
    count = 0
    for i in range(0, length+1, 1):
        if (i % 8 == 0):
            count = 0
        second.append(s2[count])
        count += 1
    count = 0
    for i in range(0, length+1, 1):
        if (i % 10 == 0):
            count = 0
        third.append(s3[count])
        count += 1
    for i in range(0, length, 1):
        if (first[i] == answers[i]):
            report[0] += 1
        if (second[i] == answers[i]):
            report[1] += 1
        if (third[i] == answers[i]):
            report[2] += 1
    
    
    print(first)
    print(second)
    print(third)
    
# 세명이 1등인 경우
    if (max(report) == min(report)):
        return [1, 2, 3]
# 두명이 1등인 경우
    elif (max(report) == report[0] and report[0] == report[1]):
        return [1, 2]
    elif (max(report) == report[1] and report[1] == report[2]):
        return [2, 3]
    elif (max(report) == report[0] and report[0] == report[2]):
        return [1, 3]
# 한명이 1등인 경우
    else:
        return [report.index(max(report))+1]
    
    