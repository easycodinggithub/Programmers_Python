def solution(numLog):
    result = []
    for i in range(0, len(numLog)-1, 1):
        if (numLog[i] == numLog[i+1]+1):
            result.append('s')
        elif (numLog[i] == numLog[i+1]-1):
            result.append('w')
        elif (numLog[i] == numLog[i+1]+10):
            result.append('a')
        elif (numLog[i] == numLog[i+1]-10):
            result.append('d')
    return "".join(result)
            