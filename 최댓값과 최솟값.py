def solution(s):
    slist = s.split()
    result = []
    for i in slist:
        result.append(int(i))
    return str(min(result))+" "+str(max(result))