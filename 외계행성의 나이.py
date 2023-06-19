def solution(age):
    alpa = [chr(i) for i in range(ord('a'), ord('j')+1)]
    nums = list(str(age))
    return "".join([alpa[int(i)] for i in nums])