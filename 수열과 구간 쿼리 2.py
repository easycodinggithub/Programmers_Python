def solution(arr, queries):
    result = []
    for i in queries:
        mins = []
        for j in range(0, len(arr), 1):
            if (j >= i[0] and j <= i[1] and arr[j] > i[2]):
                mins.append(arr[j])
        if (len(mins) <= 0):
            result.append(-1)
        else:
            result.append(min(mins))
    return result   