def solution(s):
    idx = []
    answer = []
    s = list(s)
    for i in s:
        idx = list(filter(lambda x: s[x] == i, range(len(s))))
        print(idx)
        if (len(idx) == 1):
            answer.append(s[idx[0]])
    answer.sort()
    return "".join(answer)