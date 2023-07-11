def solution(myString):
    answer = ""
    for j in myString:
        if (ord(j) < ord('l')):
            answer += 'l'
        else:
            answer += j
    return answer