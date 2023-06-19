def solution(numlist, n):
    answer = []
    final = []
    reanswer = []
    same = []
    bignum = []
    for i in numlist:
        answer.append(max([i, n])-min(i, n)) 
    print(answer)
    reanswer = sorted(answer, reverse=False)
    print(reanswer)
    for i in reanswer:
        for j in range(len(answer)-1, -1, -1):
            if (i == answer[j]):
                if (answer.count(i) >= 2):
                    same = list(filter(lambda e:answer[e] == i, range(len(answer))))
                    bignum = max([numlist[same[0]], numlist[same[1]]])
                    print(bignum)
                    final.append(bignum)
                    answer[numlist.index(bignum)] = -1
                else:
                    final.append(numlist[j])
                    answer[j] = -1
    return final