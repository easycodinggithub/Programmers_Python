def solution(s):
    ss = s.split(" ")
    answer = ""
    for i in range(0, len(ss)):
        for j in range(0, len(ss[i])):
            if ss[i][j] == " ":
                answer += " "
            elif (j+2) % 2 == 0:
                answer += ss[i][j].upper()
            else:
                answer += ss[i][j].lower()
        answer += " "
    return answer[:-1]
    