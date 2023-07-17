def solution(n):
    answer = list(str(n))
    result = []
    for i in range(len(answer)-1, -1, -1):
        result.append(int(answer[i]))
    return result
    