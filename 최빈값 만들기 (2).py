def solution(numbers):
    minusnum = []
    plusnum = []
    for i in numbers:
        if (i < 0):
            minusnum.append(i)
        else:
            plusnum.append(i)
    minusnum.sort(reverse=True)
    plusnum.sort(reverse=True)
    print(minusnum)
    print(plusnum)
    mnum = -100000000
    pnum = -100000000
    if (len(minusnum) >= 2):
        mnum = minusnum[0]*minusnum[1]
    if (len(plusnum) >= 2):
        pnum = plusnum[0]*plusnum[1]
    return max([mnum, pnum])