def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1, 1):
        count = 0
        for j in range(1, int(i**0.5)+1, 1):
            if (i % j == 0):
                count += 2
        if i ** 0.5 % 1 == 0:
            count -= 1
        if count <= limit:
            answer += count
        else:
            answer += power
    return answer