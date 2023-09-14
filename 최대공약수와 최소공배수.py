def solution(n, m):
    nmax,nmin,mmax,mmin = [],[],[],[]
    answer = [0, 0]
    
    for i in range(1, n+1):
        if (n % i == 0):
            nmax.append(i)
    for i in range(1, m+1):
        if (m % i == 0):
            mmax.append(i)
    for i in nmax:
        for j in mmax:
            if i==j:
                answer[0] = i
    for i in range(n, n*m+1, n):
        nmin.append(i)
    for i in range(m, n*m+1, m):
        mmin.append(i)
    nmin.sort(reverse=True)
    mmin.sort(reverse=True)
    for i in nmin:
        for j in mmin:
            if i==j:
                answer[1] = i
    return answer