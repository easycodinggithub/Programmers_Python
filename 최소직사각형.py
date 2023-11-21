def solution(sizes):
    maxarr = []
    minarr = []
    for i in sizes:
        maxarr.append(max([i[0], i[1]]))
        minarr.append(min([i[0], i[1]]))
    return max(maxarr) * max(minarr)
        