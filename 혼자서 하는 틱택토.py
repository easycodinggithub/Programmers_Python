def solution(board):

    oc = 0
    xc = 0
    og = 0
    xg = 0
    
    for i in range(0, len(board), 1):
        r1 = board[i]
        r2 = board[0][i] + board[1][i] + board[2][i]
        
        if r1 == "OOO":
            og += 1
        elif r1 == "XXX":
            xg += 1
        if r2 == "OOO":
            og += 1
        elif r2 == "XXX":
            xg += 1
        
        for j in board[i]:
            if j == 'O':
                oc += 1
            elif j == 'X':
                xc += 1
        
    if board[0][0] + board[1][1] + board[2][2] == "OOO":
        og += 1
    elif board[0][0] + board[1][1] + board[2][2] == "XXX":
        xg += 1
    
    if board[0][2] + board[1][1] + board[2][0] == "OOO":
        og += 1
    elif board[0][2] + board[1][1] + board[2][0] == "XXX":
        xg += 1
    
    if og > 0 and xg > 0:
        return 0
    
    if og > 0 and oc-xc != 1:
        return 0
    
    if xg > 0 and oc != xc:
        return 0
    
    if oc-xc != 0 and oc-xc != 1:
        return 0
    
    return 1
    
            