def solution(myString, pat):
    for i in range(0, len(myString)-len(pat)+1, 1):
        if ((myString[i:i+len(pat)]).lower() == pat.lower()):
            return 1
    return 0