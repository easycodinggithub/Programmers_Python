def solution(n):
    sb = ["수", "박"]
    result = []
    for i in range(n):
        result.append(sb[i % 2])
    return "".join(result)