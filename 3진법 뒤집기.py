def solution(n):
    answer = list(convert_iter(n, 3))
    result = [answer[i] for i in range(len(answer)-1, -1, -1)]
    return int(''.join(result), 3) 
    
def convert_iter(num, base):
    power = 0
    tmp = ''
    while num:
        tmp = str(num%base) + tmp
        num //= base
    return tmp