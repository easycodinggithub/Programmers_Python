def solution(q, r, code):
    answer = []
    for i in range(0, len(code), 1):
        if (i % q == r):
            answer.append(code[i])
    return "".join(answer)