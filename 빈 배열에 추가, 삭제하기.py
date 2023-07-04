def solution(arr, flag):
    answer = []
    for i in range(0, len(arr), 1):
        if (flag[i] == True):
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()   
    return answer