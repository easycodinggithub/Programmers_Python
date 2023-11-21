def solution(d, budget):
    answer = sorted(d)
    sum = 0
    count = 0
    for i in answer:
        sum += i
        count += 1
        if (sum > budget):
            return count-1
    return count
    