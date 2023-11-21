def solution(babbling):
    answer = 0
    say = ["aya", "ye", "woo", "ma"]
    for i in range(0, len(babbling), 1):
        for j in range(0, len(say), 1):
            babbling[i] = babbling[i].replace(say[j], str(j))
    for i in babbling:
        try:
            int(i)
            check = 0
            for j in range(0, 10, 1):
                if str(i).count(str(j)*2) >= 1:
                    check = 1
            if check == 0:
                answer += 1
        except:
            continue
    return answer