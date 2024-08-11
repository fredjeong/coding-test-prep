def solution(s):
    answer = True
    check = 0
    if len(s) % 2 == 1:
        answer = False
    else:
        if s[0] != "(" or s[-1] != ")":
            answer = False
        else:
            for i in range(len(s)):
                if s[i] == "(":
                    check += 1
                else:
                    check -= 1
                
                if check < 0:
                    answer = False
                    break
                    
                if i == len(s) - 1:
                    if check != 0:
                        answer = False
                        break
    return answer