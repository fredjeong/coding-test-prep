def solution(s):
    count = 0
    zeros = 0
    while s != "1":
        count += 1
        old_length = len(s)
        s = s.replace("0","")
        new_length = len(s)
        zeros += old_length - new_length
        s = bin(len(s))[2:]
    answer = [count, zeros]
    return answer