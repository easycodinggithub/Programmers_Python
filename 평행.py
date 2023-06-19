def solution(dots):
    vs1 = [[0, 1], [0, 2], [0, 3]]
    vs2 = [[2, 3], [1, 3], [1, 2]]
    for i in range(3):
        vsxmax1 = max(dots[vs1[i][0]][0], dots[vs1[i][1]][0])
        vsxmin1 = min(dots[vs1[i][0]][0], dots[vs1[i][1]][0])
        vsymax1 = max(dots[vs1[i][0]][1], dots[vs1[i][1]][1])
        vsymin1 = min(dots[vs1[i][0]][1], dots[vs1[i][1]][1])
        
        vsx = (vsymax1-vsymin1)/(vsxmax1-vsxmin1)
        
        vsxmax2 = max(dots[vs2[i][0]][0], dots[vs2[i][1]][0])
        vsxmin2 = min(dots[vs2[i][0]][0], dots[vs2[i][1]][0])
        vsymax2 = max(dots[vs2[i][0]][1], dots[vs2[i][1]][1])
        vsymin2 = min(dots[vs2[i][0]][1], dots[vs2[i][1]][1])
        
        vsy = (vsymax2-vsymin2)/(vsxmax2-vsxmin2)
        
        if (vsx == vsy):
            return 1
    else:  
        return 0
