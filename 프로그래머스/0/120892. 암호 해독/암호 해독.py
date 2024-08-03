def solution(cipher, code):
    answer = ''
    index = 1
    for k in cipher:
        if index % code == 0:
            answer += cipher[index - 1]
            index += 1
        else:
            index += 1
    return answer