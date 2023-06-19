def solution(x1, x2, x3, x4):
    xy1 = (x1 or x2)
    xy2 = (x3 or x4)
    xy = (xy1 and xy2)
    return xy
    