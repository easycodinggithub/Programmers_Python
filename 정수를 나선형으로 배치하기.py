def solution(n):
    answer = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        answer[0][i] = i+1
    m = n-1
    c = 1
    
    x = n
    y = 0
    s = n
    for i in range(n-1):
        for j in range(2):
            if (c >= 5):
                c = 1
            # print(m)
            if (c == 1):
                x -= 1
                y += 1
                # print("y 축 밑으로")
                for i in range(m):
                    print("x 는 ", x, "y 는 ", y)
                    s += 1
                    answer[y][x] = s
                    y += 1
                
            elif (c == 2):
                x -= 1
                y -= 1
                # print("x 축 왼쪽으로")
                for i in range(m):
                    print("x 는 ", x, "y 는 ", y)
                    s += 1
                    answer[y][x] = s
                    x -= 1
            elif (c == 3):
                x += 1
                y -= 1
                # print("y 축 위로")
                for i in range(m):
                    print("x 는 ", x, "y 는 ", y)
                    s += 1
                    answer[y][x] = s
                    y -= 1
            elif (c == 4):
                x += 1
                y += 1
                # print("x 축 오른쪽으로")
                for i in range(m):
                    print("x 는 ", x, "y 는 ", y)
                    s += 1
                    answer[y][x] = s
                    x += 1
            
            # print("변경", c)
            c += 1
        m -= 1
    return answer
        