def solution(array, n):
    check = []
    array.append(n)
    array.sort()
    for i in range(0, len(array), 1):
        if (array[i] == n):
            if (i == 0):
                return array[i+1]
            elif (i == len(array)-1):
                return array[i-1]
            check.append(array[i-1])
            check.append(array[i+1])
            break
    print(check)
    cmin = n - check[0]
    cmax = check[1] - n
    if (cmin <= cmax):
        return check[0]
    else:
        return check[1]
    