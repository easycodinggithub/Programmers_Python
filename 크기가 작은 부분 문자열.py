def solution(t, p):
    arr = []
    answer = []
    count = 0
    tarr = list(t)
    for i in range(0, len(tarr), 1):
        if (len(tarr[i:i+len(p)]) == len(p)):
            arr.append(tarr[i:i+len(p)])
    for i in arr:
        answer.append(int("".join(i)))
    for i in answer:
        if (int(p) >= i):
            count += 1
    return count
            