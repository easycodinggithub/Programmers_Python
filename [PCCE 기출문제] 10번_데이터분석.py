def solution(data, ext, val_ext, sort_by):
    answer = []
    s = ["code", "date", "maximum", "remain"]
    e = s.index(ext)
    b = s.index(sort_by)
    
    for i in range(0, len(data), 1):
        if data[i][e] <= val_ext:
            answer.append(data[i])
    
    answer.sort(key=lambda x:x[b])
    return answer
            
            
        