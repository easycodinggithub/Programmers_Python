def solution(arr):
    answer = [[]]
    im = len(arr)
    jm = len(arr[0])
    
    if (im > jm):
        for i in arr:
            for j in range(im-jm):
                i.append(0)
    elif (jm > im):
        for i in range(jm-im):
            arr.append([0 for i in range(jm)])
    return arr