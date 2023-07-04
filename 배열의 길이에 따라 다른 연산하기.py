def solution(arr, n):
    answer = arr
    if (len(answer) % 2 == 0):
        for i in range(1, len(answer)+1, 2):
            answer[i] += n
    else:
        for i in range(0, len(answer), 2):
            answer[i] += n
    return answer