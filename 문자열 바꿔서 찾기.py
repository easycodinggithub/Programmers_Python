def solution(myString, pat):
    answer = []
    for i in myString:
        if (i == 'A'):
            answer.append('B')
        else:
            answer.append('A')
    if ("".join(answer).find(pat) >= 0):
        return 1
    return 0