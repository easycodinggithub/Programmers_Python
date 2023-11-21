def solution(i, j, k):
    answer = ""
    count = 0
    for n in range(i, j+1, 1):
        answer += str(n)
    for u in list(answer):
        if (u == str(k)):
            count += 1
    return count