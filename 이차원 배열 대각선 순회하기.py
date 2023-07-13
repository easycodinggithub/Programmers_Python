def solution(board, k):
    answer = 0
    for i in range(0, len(board), 1):
        for j in range(0, len(board[i]), 1):
            if (i + j <= k):
                answer += board[i][j]
    return answer