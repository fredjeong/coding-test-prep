def solution(spell, dic):
    answer = 2
    temp = 0
    for word in dic:
        for character in spell:
            if word.count(character) >= 1:
                temp += 1
                if temp == len(spell):
                    answer = 1
        temp = 0
        
    return answer