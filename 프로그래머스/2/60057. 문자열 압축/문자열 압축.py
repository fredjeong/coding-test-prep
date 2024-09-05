def solution(s):
    answer = []

    length = 1
    while length < len(s) // 2 + 1:
        # length 단위로 반복되는 것 확인
        new_str = ""
        counter = 1
        for i in range(0, ((len(s)//length)-1) * length + 1, length):
            if s[i:i+length] == s[i+length:i+length*2]:
                counter += 1
            else:
                if counter == 1:
                    new_str += s[i:i+length]
                else:
                    new_str += str(counter) + s[i:i+length]
                    counter = 1
        new_str += s[((len(s)//length)) * length:]

        answer.append(len(new_str))
        length += 1
    
    if len(answer) == 0:
        return 1
    else:
        return min(answer)