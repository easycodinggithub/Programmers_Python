def solution(arr):
    answer = []
    see = -1
    for i in arr:
        if i != see:
            answer.append(i)
            see = i
    return answer
        