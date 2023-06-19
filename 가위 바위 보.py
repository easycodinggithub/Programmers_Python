def solution(rsp):
    numbers = [5,0,0,0,0,2]
    answer = []
    robots = list(rsp)
    for i in robots:
        answer.append(numbers[int(i)])
    return "".join(map(str, answer))