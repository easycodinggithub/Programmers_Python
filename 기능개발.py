def solution(progresses, speeds):
    day = []
    s = 0
    while True:
        f = 0
        for i in range(s, len(progresses), 1):
            progresses[i] += speeds[i]
        for i in range(s, len(progresses), 1):
            if progresses[i] >= 100:
                f += 1
                s += 1
            else:
                break
        if f > 0:
            day.append(f)
        if s >= len(progresses):
            break
    return day