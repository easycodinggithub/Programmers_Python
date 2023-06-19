def solution(sides):
    answer = 0
    for i in range(1, sum(sides), 1):
        print(i)
        if (max([ sides[0], sides[1], i]) < sum([ sides[0], sides[1], i]) - max([ sides[0], sides[1], i])):
            answer += 1
    return answer