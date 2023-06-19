def solution(hp):
    count = 0
    while True:
        if hp < 5:
            break
        hp -= 5
        count += 1
    if (hp >= 3):
        hp -= 3
        count += 1 
    while True:
        if hp < 1:
            break
        hp -= 1
        count += 1
    return count