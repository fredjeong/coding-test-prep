def solution(s):
    answer = [-1]
    for i in range(1,len(s)):
        character = s[i]
        temp = s[:i]
        if character in temp:
            index = temp.rindex(character)
            answer.append(i - index)
        else:
            answer.append(-1)
    return answer