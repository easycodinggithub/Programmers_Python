def solution(s):
    answer = s.split(" ")
    count = 0
    for i in range(0, len(answer), 1):
        if (answer[i] == 'Z'):
            count -= int(answer[i-1])
            continue
        count += int(answer[i])
    return count