def solution(A,B):
    answer = 0

    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(0, len(A), 1):
        answer += A[i] * B[i]

    return answer