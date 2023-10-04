def solution(arr):
    first = 0
    last = 0
    for i in range(0, len(arr), 1):
        if (arr[i] == 2):
            first = i
            break
    for i in range(len(arr)-1, -1, -1):
        if (arr[i] == 2):
            last = i
            break
    if (first == 0 and last == 0):
        return [-1]
    if (fsirst == last):
        return [2]
    print(first, last)

    return arr[first:last+1]