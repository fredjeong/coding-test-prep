def solution(word):
    dic = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5} 
    scores = {}
    # 길이 1
    for char_1 in list(dic.keys()):
        result = char_1
        score = 0
        for i in range(len(result)):
            score += 10 ** (-1 * i) * dic[result[i]]
        scores[result] = -score
    
    
    # 길이 2
    for char_1 in list(dic.keys()):
        for char_2 in list(dic.keys()):
            result = char_1 + char_2
            score = 0
            for i in range(len(result)):
                score += 10 ** (-1 * i) * dic[result[i]]
            scores[result] = -score
    
    # 길이 3
    for char_1 in list(dic.keys()):
        for char_2 in list(dic.keys()):
            for char_3 in list(dic.keys()):
                result = char_1 + char_2 + char_3
                score = 0
                for i in range(len(result)):
                    score += 10 ** (-1 * i) * dic[result[i]]
                scores[result] = -score
    # 길이 4
    for char_1 in list(dic.keys()):
        for char_2 in list(dic.keys()):
            for char_3 in list(dic.keys()):
                for char_4 in list(dic.keys()):
                    result = char_1 + char_2 + char_3 + char_4
                    score = 0
                    for i in range(len(result)):
                        score += 10 ** (-1 * i) * dic[result[i]]
                    scores[result] = -score
                    
    # 길이 5
    for char_1 in list(dic.keys()):
        for char_2 in list(dic.keys()):
            for char_3 in list(dic.keys()):
                for char_4 in list(dic.keys()):
                    for char_5 in list(dic.keys()):
                        result = char_1 + char_2 + char_3 + char_4 + char_5
                        score = 0
                        for i in range(len(result)):
                            score += 10 ** (-1 * i) * dic[result[i]]
                        scores[result] = -score
    scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    arr = []
    for i in range(len(scores)):
        arr.append(scores[i][0])
    
    # 인덱스 구하고 + 1
    answer = arr.index(word) + 1
    return answer
    