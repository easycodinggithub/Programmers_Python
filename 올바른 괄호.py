def solution(s):
    answer = list(s)
    i = 0
    check = 0
    if (len(answer) % 2 != 0) or (answer[0] == ')') or (answer[-1] == '(') or (answer.count('(') != answer.count(')')):
        return False
    while True:
        if (i >= len(answer)-1):
            return True
        
        if (answer[i] == '('):
            check += 1
        else:
            check -= 1
            
        if (check >= 0):
            i += 1
        else:
            return False