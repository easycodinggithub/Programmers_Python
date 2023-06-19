def solution(sides):
    answer = sorted(sides, reverse=True)
    return (1 if answer[0] < (answer[1] + answer[2]) else 2)