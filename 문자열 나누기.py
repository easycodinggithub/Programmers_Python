def solution(s):
    s = list(s)
    answer = []
    while True:
        f = s[0]
        fc = 0
        ec = 0
        check = 0
        if len(s) < 1:
            break
        for i in range(0, len(s), 1):
            if s[i] == f:
                fc += 1
            else:
                ec += 1
            if fc == ec and i+1 < len(s):
                answer.append("".join(s[0:i+1]))
                del s[0:i+1]
                check = 1
                break
        if check == 0:
            answer.append("".join(s))
            break
    return len(answer)
                