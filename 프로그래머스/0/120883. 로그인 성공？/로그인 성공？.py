def solution(id_pw, db):
    answer = 'fail'
    for id, pw in db:
        if id == id_pw[0] and pw == id_pw[1]:
            answer = 'login'
            break
        elif id == id_pw[0] and pw != id_pw[1]:
            answer = 'wrong pw'
            break
        else:
            pass
    return answer