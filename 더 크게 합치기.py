def solution(a, b):
    big1 = str(a)+str(b)
    big2 = str(b)+str(a)
    return max(int(big1), int(big2))