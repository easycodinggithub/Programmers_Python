def solution(n):
    answer = list(str(n))
    count = 0
    for i in answer:
        count += int(i)
    return count