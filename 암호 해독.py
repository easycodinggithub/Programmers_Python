def solution(cipher, code):
    answer = []
    for i in range(code-1, len(list(cipher)), code):
        answer.append(cipher[i])
    return "".join(answer)