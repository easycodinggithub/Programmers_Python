def solution(a, b):
    plus = int(str(a)+str(b))
    mult = 2*a*b
    return max(plus, mult)