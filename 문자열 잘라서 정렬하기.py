def solution(myString):
    answer = myString.split('x')
    result = []
    for i in answer:
        if (len(i) > 0):
            result.append(i)
    result.sort()
    return result