def solution(arr):
    for i in range(0, len(arr), 1):
        for j in range(0, len(arr[i]), 1):
            if (arr[i][j] != arr[j][i]):
                return 0
    return 1