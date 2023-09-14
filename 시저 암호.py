def solution(s, n):
    small = [chr(i) for i in range(97, 123, 1)]
    big = [chr(i) for i in range(65, 91, 1)]
    ss = list(s)
    answer = ""
    for i in ss:
        if i==" ":
            answer += " "
        else:
            if ord(i) >= 97:
                if (ord(i)+n) > 122:
                    answer += chr(ord(i)+n-122+96)
                else:
                    answer += chr(ord(i)+n)
            else:
                if ord(i)+n > 90:
                    answer += chr(ord(i)+n-90+64)
                else:
                    answer += chr(ord(i)+n)
    return answer