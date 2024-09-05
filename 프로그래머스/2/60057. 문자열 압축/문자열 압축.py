def solution(s):
    #answer = len(s)
    answer = []
    # 압축한 문자열 중 가장 짧은 것의 길이 리턴
    length = 1
    while length < len(s) // 2 + 1:
        # length 단위로 반복되는 것 확인
        new_str = ""
        # s = aabbaccc
        # len(s) = 8
        # length = 1
        # 0 / 1 / 2 / 3 / 4 / 5 / 6 / 7 
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
        #print(new_str)
        
        # length가 이전보다 길면 break
        answer.append(len(new_str))
#        if len(new_str) > answer:
#            break
#        else:
#            answer = len(new_str)
        length += 1
    
    if len(answer) == 0:
        return 1
    else:
        return min(answer)