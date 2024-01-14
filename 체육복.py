def solution(n, lost, reserve):
    s = [i for i in range(1, n+1, 1)]
    m = 0
    
    for i in range(0, len(lost), 1):
        for j in range(0, len(reserve), 1):
            if lost[i] == reserve[j]:
                lost[i] = 0
                reserve[j] = 0
    
    lost2 = []
    reserve2 = []
    for i in lost:
        if i > 0:
            lost2.append(i)
    for i in reserve:
        if i > 0:
            reserve2.append(i)
    
    lost2.sort()
    reserve2.sort()
    
    for i in lost2:
        if (i-1 in reserve2):
            reserve2.remove(i-1)
        elif (i+1 in reserve2):
            reserve2.remove(i+1)
        else:
            m += 1
    return n-m