def solution(board):
    answer = 0
    for i in range(0, len(board), 1):
        for j in range(0, len(board[i]), 1):
            if (board[i][j] == 1):
                for x in range(-1, 2, 1):
                    for y in range(-1, 2, 1):
                        if (i+x >= 0 and i+x < len(board) and 
                            j+y >= 0 and j+y < len(board[i]) and
                            board[i+x][j+y] == 0):
                            board[i+x][j+y] = 2
    for i in board:
        for j in i:
            if (j == 0):
                answer += 1
    return answer
                            