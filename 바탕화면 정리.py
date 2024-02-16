def solution(wallpaper):
    sy = 0
    sx = 0
    ey = len(wallpaper)
    ex = len(wallpaper[0])
    
    # sy
    for i in wallpaper:
        c = 0
        for j in i:
            if j == '#':
                c += 1
        if c > 0:
            break
        else:
            sy += 1
    
    # sx
    for i in range(0, len(wallpaper[0]), 1):
        c = 0
        for j in range(0, len(wallpaper), 1):
            if wallpaper[j][i] == '#':
                c += 1
        if c > 0:
            break
        else:
            sx += 1
    
    # ey
    for i in range(len(wallpaper)-1, -1, -1):
        c = 0
        for j in wallpaper[i]:
            if j == '#':
                c += 1
        if c > 0:
            break
        else:
            ey -= 1
    
    # ex
    for i in range(len(wallpaper[0])-1, -1, -1):
        c = 0
        for j in range(0, len(wallpaper), 1):
            if wallpaper[j][i] == '#':
                c += 1
        if c > 0:
            break
        else:
            ex -= 1
    
    return [sy, sx, ey, ex]