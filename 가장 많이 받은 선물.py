def solution(friends, gifts):
    gift = {}
    giftv = {}
    answer = {}
    final = []
    for i in friends:
        giftv[i] = 0
        answer[i] = 0
        temp = {}
        for j in friends:
            temp[j] = 0
        gift[i] = temp
    for i in gifts:
        k, v = i.split(' ')
        gift[k][v] += 1
    for i in friends:
        for j in friends:
            giftv[i] += gift[i][j]
            giftv[i] -= gift[j][i]
    for i in friends:
        for j in friends:
            if i != j:
                if gift[i][j] > gift[j][i]:
                    answer[i] += 1
                elif gift[i][j] == gift[j][i]:
                    if giftv[i] > giftv[j]:
                        answer[i] += 1
    for i in answer:
        final.append(answer[i])
    return max(final)
                    