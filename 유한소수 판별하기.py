from math import gcd
def solution(a, b):
    aa = a//gcd(a, b)
    bb = b//gcd(a, b)
    
    p = []
    
    # 기약 분수로 나타내기
    print(aa)
    print(bb) 
    
    # 1부터 20까지 전달
    for i in range(2, bb+1, 1):
        # bb 의 인수를 소수 함수로 전달
        if (bb % i == 0):
            if (primary(i)):
                p.append(i)
    for i in p:
        if (i != 2 and i != 5):
            return 2
    return 1

# 소수인지 아닌지 확인하는 함수
def primary(i):
    for j in range(2, i, 1):
        if (i % j == 0):
            return False
    return True