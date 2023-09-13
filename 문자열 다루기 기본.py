def solution(s):
    if (len(s) == 4 or len(s) == 6) and str.isdigit(s):
        return True
    else:
        return False