def solution(s):
    answer = ''
    if len(s)%2 == 1:
        index = (len(s)-1)//2
        answer += s[index]
    else:
        index = len(s)//2
        answer += s[index - 1:index + 1]
    return answer