def solution(n):
    answer = [[0 for i in range(n)] for j in range(n)]
    index = 0
    for i in range(0, len(answer), 1):
        for j in range(0, len(answer[i]), 1):
            if (i == index and j == index):
                answer[i][j] = 1
                index += 1
    return answer