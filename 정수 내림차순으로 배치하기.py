def solution(n):
    answer = list(str(n))
    answer = sorted(answer, reverse=True)
    return int("".join(answer))