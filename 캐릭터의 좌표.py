def solution(keyinput, board):
    position = {
        "up" : [0, 1],
        "down" : [0, -1],
        "left" : [-1, 0],
        "right" : [1, 0]
    }
    sx = 0
    sy = 0
    bxmax = board[0]//2
    bxmin = board[0]//2*-1
    bymax = board[1]//2
    bymin = board[1]//2*-1
    
    for i in keyinput:
        x = position[i][0]
        y = position[i][1]
        sx += x
        sy += y
        if (sx > bxmax):
            sx -= 1
        if (sx < bxmin):
            sx += 1
        if (sy > bymax):
            sy -= 1
        if (sy < bymin):
            sy += 1
    return [sx, sy]
            
        
    