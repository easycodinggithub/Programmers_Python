def solution(quiz):
    temp = []
    answer = []
    print(len(quiz))
    for i in range(0, len(quiz), 1):
        temp = quiz[i].split(" ")
        if (temp[1] == "+"):
            if (int(temp[0]) + int(temp[2]) == int(temp[4])):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if (int(temp[0]) - int(temp[2]) == int(temp[4])):
                answer.append("O")
            else:
                answer.append("X")
    return answer