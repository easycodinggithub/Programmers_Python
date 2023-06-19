def solution(id_pw, db):
    idCheck = 0
    for i in range(-1, len(db)-1, 1):
        if (id_pw[0] == db[i][0] and id_pw[1] == db[i][1]):
            return "login"
        elif (id_pw[0] == db[i][0]):
            idCheck += 1
    if (idCheck > 0):
        return "wrong pw"
    else:
        return "fail"