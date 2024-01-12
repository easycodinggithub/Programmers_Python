def solution(n, m, section):
    standard = section[0]
    count = 1
    for i in section:
        if standard + (m-1) < i:
            standard = i
            count += 1
    return count