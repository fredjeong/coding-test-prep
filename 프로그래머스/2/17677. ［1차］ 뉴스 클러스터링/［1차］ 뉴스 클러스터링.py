def solution(str1, str2):
    dic_1 = {}
    dic_2 = {}
    temp = ""
    for char in str1:
        temp += char
        if len(temp) == 2:
            if temp.isalpha():
                temp = temp.lower()
                if temp in dic_1:
                    dic_1[temp] += 1
                else:
                    dic_1[temp] = 1
            temp = temp[1]
    
    temp = ""
    for char in str2:
        temp += char
        if len(temp) == 2:
            if temp.isalpha():
                temp = temp.lower()
                if temp in dic_2:
                    dic_2[temp] += 1
                else:
                    dic_2[temp] = 1
            temp = temp[1]
            
    # 교집합 구하기
    intersection = set(dic_1) & set(dic_2)
    num_1 = 0
    for i in intersection:
        num_1 += min(dic_1[i], dic_2[i])
    
    # 합집합 구하기
    union = set(dic_1) | set(dic_2)
    num_2 = 0
    for i in union:
        if i in set(dic_1) and i in set(dic_2):
            num_2 += max(dic_1[i], dic_2[i])
        elif i in set(dic_1) and i not in set(dic_2):
            num_2 += dic_1[i]
        elif i not in set(dic_1) and i in set(dic_2):
            num_2 += dic_2[i]
    
    if num_2 == 0:
        similarity = 1
    else:
        similarity = num_1 / num_2
    
    answer = int(similarity * 65536)
    
    return answer