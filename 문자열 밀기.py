def solution(A, B):
    answer = A*2
    count = 0
    for i in range(len(A), 0, -1):
        if (answer[i:i+len(A)] == B):
            return count
        print(answer[i:i+len(A)])
        count += 1
    return -1