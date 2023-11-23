def solution(k, tangerine):
    c = {}
    count = 0
    for i in tangerine:
        if i not in c:
            c[i] = 1
        else:
            c[i] += 1
    cc = sorted(c.items(), key= lambda item:item[1], reverse=True)
    # print(cc)
    for i, j in cc:
        if k-j <= 0:
            count += 1
            break
        else:
            k -= j
            count += 1
    return count
        
    