def solution(num, k):
    numlist = list(str(num))
    for i in range(0, len(numlist), 1):
        if (numlist[i] == str(k)):
            return i+1
    return -1