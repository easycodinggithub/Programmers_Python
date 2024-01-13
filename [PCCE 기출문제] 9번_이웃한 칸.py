def solution(board, h, w):
    x = board[h][w]
    c = 0
    if h-1 >= 0 and x == board[h-1][w]:
        c += 1
    if h+1 < len(board) and x == board[h+1][w]:
        c += 1
    if w-1 >= 0 and x == board[h][w-1]:
        c += 1
    if w+1 < len(board[0]) and x == board[h][w+1]:
        c += 1
    return c