def solution(park, routes):
    si = 0
    sj = 0
    parks = []
    
    for i in range(0, len(park), 1):
        tmp = []
        for j in range(0, len(park[0]), 1):
            tmp.append(0)
        parks.append(tmp)
        
    for i in range(0, len(park), 1):
        for j in range(0, len(park[i]), 1):
            if park[i][j] == "S":
                si, sj = i, j
                
            parks[i][j] = park[i][j]
    
    for i in routes:
        check = 0
        d, l = i.split()
        l = int(l)
        if d == "N":
            if si-l < 0 or si-l >= len(park):
                continue
            else:
                for k in range(1, l+1, 1):
                    if parks[si-k][sj] == "X":
                        check = 1
                if check == 0:
                    si -= l
        elif d == "S":
            if si+l < 0 or si+l >= len(park):
                continue
            else:
                for k in range(1, l+1, 1):
                    if parks[si+k][sj] == "X":
                        check = 1
                if check == 0:
                    si += l
        elif d == "W":
            if sj-l < 0 or sj-l >= len(park[0]):
                continue
            else:
                for k in range(1, l+1, 1):
                    if parks[si][sj-k] == "X":
                        check = 1
                if check == 0:
                    sj -= l
        elif d == "E":
            if sj+l < 0 or sj+l >= len(park[0]):
                continue
            else:
                for k in range(1, l+1, 1):
                    if parks[si][sj+k] == "X":
                        check = 1
                if check == 0:
                    sj += l
    return [si, sj]