def solution(spell, dic):
    for i in dic:
        count = 0
        for j in spell:
            if (i.find(j) < 0):
                count = 0
                break
            else:
                count += 1
        print(count)
        if (count >= len(i)):
            return 1
    return 2