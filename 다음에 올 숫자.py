def solution(common):
    count = 1
    while True:
        add = []
        sub = []
        mul = []
        div = []
        mulminus = []
        divminus = []
        for i in range(0, len(common)-1, 1):
            if (common[i]+count == common[i+1]):
                add.append(1)
            if (common[i]-count == common[i+1]):
                sub.append(1)
            if (common[i]*count == common[i+1]):
                mul.append(1)
            if (common[i]*count*-1 == common[i+1]):
                mulminus.append(1)
            if (common[i]//count*-1 == common[i+1]):
                divminus.append(1)
            if (len(common) == len(add)+1):
                return common[-1]+count
            elif (len(common) == len(sub)+1):
                return common[-1]-count
            elif (len(common) == len(mul)+1):
                return common[-1]*count
            elif (len(common) == len(div)+1):
                return common[-1]//count
            elif (len(common) == len(mulminus)+1):
                return common[-1]*count*-1
            elif (len(common) == len(divminus)+1):
                return common[-1]//count*-1
            else:
                count += 1