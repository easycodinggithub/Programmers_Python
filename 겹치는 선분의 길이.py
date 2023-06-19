def solution(lines):
    answer = [0 for i in range(-100, 101, 1)]
    count = 0
    for i in lines:
        for j in range(100+i[0], 100+i[1], 1):
            answer[j] += 1
    for i in answer:
        if (i > 1):
            count += 1
    return count