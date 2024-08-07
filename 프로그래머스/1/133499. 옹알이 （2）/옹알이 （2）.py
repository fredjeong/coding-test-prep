def solution(babbling):
    answer = 0
    vocab = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for voca in vocab:
            if voca in babbling[i]:
                if voca+voca not in babbling[i]:
                    babbling[i] = babbling[i].replace(voca, ' ')
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace(' ', '')
    
    
    for i in babbling:
        if i == '':
            answer += 1
    return answer
