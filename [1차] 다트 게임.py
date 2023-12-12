def solution(dartResult):
    score = [0, 0, 0]
    sp = 0
    for j in range(3):
        for i in range(sp, len(dartResult), 1):
            if dartResult[i].isdigit() == True:
                if dartResult[i] == '1' and dartResult[i+1] == '0':
                    score[j] += int(dartResult[i:i+2])
                    sp = i+2
                else:
                    score[j] += int(dartResult[i])
                    sp = i+1
                break
                    
    print(score)
    
    sp = 0
    minus = 1
    for i in dartResult:
        if i == 'S':
            score[sp] = score[sp]**1
            sp += 1
        elif i == 'D':
            score[sp] = score[sp]**2
            sp += 1
        elif i == 'T':
            score[sp] = score[sp]**3
            sp += 1
        elif i == '*':
            ssp = 0
            if sp >= 3:
                ssp = 1
            for j in range(ssp, sp, 1):
                score[j] *= 2
        elif i == '#':
            score[sp-1] *= -1
                
                
                    
    return sum(score)
    