def solution(numbers, hand):

    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [100, 0, 200]]
    answer = ""
    rh = [3, 2]
    lh = [3, 0]
    
    for i in numbers:
        
        rt = 0
        lt = 0
        
        if i == 1 or i == 4 or i == 7:
            lh[0] = ((i+2)//3)-1
            lh[1] = 0
            answer += 'L'
            
        elif i == 3 or i == 6 or i == 9:
            rh[0] = (i//3)-1
            rh[1] = 2
            answer += 'R'
            
        else:
            if i == 2: 
                p = [0, 1]
            elif i == 5:
                p = [1, 1]
            elif i == 8:
                p = [2, 1]
            elif i == 0:
                p = [3, 1]
                
            rt += max([p[0], rh[0]])-min([p[0], rh[0]])
            rt += max([p[1], rh[1]])-min([p[1], rh[1]])
            lt += max([p[0], lh[0]])-min([p[0], lh[0]])
            lt += max([p[1], lh[1]])-min([p[1], lh[1]])
            
            if rt == lt:
                if hand == "right":
                    rh[0] = p[0]
                    rh[1] = p[1]
                    answer += "R"
                else:
                    lh[0] = p[0]
                    lh[1] = p[1]
                    answer += "L"
            else:
                if rt < lt:
                    rh[0] = p[0]
                    rh[1] = p[1]
                    answer += "R"
                else:
                    lh[0] = p[0]
                    lh[1] = p[1]
                    answer += "L"
            
    return answer