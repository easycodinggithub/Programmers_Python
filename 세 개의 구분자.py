def solution(myStr):
    result = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    result2 = result.split(' ')
    answer = []
    for i in result2:
        if (i != ""):
            answer.append(i)
    if (len(answer) <= 0):
        return ["EMPTY"]
    return answer