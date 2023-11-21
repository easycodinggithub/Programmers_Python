def solution(food):
    answer1 = []
    for i in range(1, len(food), 1):
        answer1.append(str(i) * int(food[i]//2))
    answer2 = list(reversed(answer1))
    return "".join(answer1 + ["0"] + answer2)