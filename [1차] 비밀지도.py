def solution(n, arr1, arr2):
    answer = []
    result = []
    for i in range(0, len(arr1), 1):
        temp = "".join(list(str(bin(arr1[i]|arr2[i])))[2:]).zfill(n)
        answer.append(list(temp))
    for i in answer:
        arr = ''
        for j in i:
            if (j == '1'):
                arr += '#'
            else:
                arr += ' '
        result.append(arr)
    return result
            
    