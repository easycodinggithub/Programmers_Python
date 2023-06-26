def solution(myString):
    answer = list(myString)
    result = []
    for i in range(0, len(answer), 1):
        if (answer[i] == 'a' or answer[i] == 'A'):
            result.append('A')
        else:
            result.append(answer[i].lower())
    return "".join(result)