def solution(s, skip, index):
    alpha = []
    answer = []
    for i in range(97, 123, 1):
        check = 0
        for j in list(skip):
            if (chr(i) == j):
                check = 1
        if (check == 0):
            alpha.append(chr(i))
    
    for i in s:
        for j in range(0, len(alpha), 1):
            if (i == alpha[j]):
                temp = j+index
                while True:
                    if (temp >= len(alpha)):
                        temp -= len(alpha)
                    else:
                        break
                answer.append(alpha[temp])
                break
    return "".join(answer)