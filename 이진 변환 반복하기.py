def solution(s):
    ss = s
    total = 0
    answer = 0
    while True:
        if (ss == "1"):
            break
        sss = int("".join(sorted(list(ss))))
        total += len(ss)-len(str(sss))
        ssss = bin(len(str(sss)))
        ss = ssss[2:]
        answer += 1
    
    return [answer, total]